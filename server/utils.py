import os
from base64 import b64decode
import torch 
import torch.nn as nn
from pathlib import Path
import json
from torchvision import transforms
from PIL import Image
import io
import numpy as np
import joblib
import torchvision.models as models
import sys

# Add the project root to the path so we can import from model directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from model.efficientnet_classifier import EfficientNetClassifier

MODEL_PATH = os.path.join(PROJECT_ROOT, "server","artifacts", 'butterfly_classifier_joblib.pkl')



def decode_base64_string(encoded_string: str) -> bytes:
    return b64decode(encoded_string)

def load_model_from_joblib(filepath, device):
    """
    Load model from joblib file
    """
    try:
        # Load the data - joblib handles basic objects, but state_dict needs special handling
        model_data = joblib.load(filepath)
        
        # Recreate model architecture
        model = EfficientNetClassifier(model_data['num_classes']).to(device)
        
        # Load weights with proper device mapping
        state_dict = model_data['model_state_dict']
        if device == 'cpu' and torch.cuda.is_available() == False:
            # If state_dict was saved on CUDA but we're on CPU, map it properly
            if isinstance(state_dict, dict):
                # Map tensors to CPU
                cpu_state_dict = {}
                for key, value in state_dict.items():
                    if torch.is_tensor(value):
                        cpu_state_dict[key] = value.cpu()
                    else:
                        cpu_state_dict[key] = value
                model.load_state_dict(cpu_state_dict)
            else:
                model.load_state_dict(state_dict)
        else:
            model.load_state_dict(state_dict)
        
        model.eval()
        
        return model, model_data
        
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        return None, None
class ConvertToRGB:
    def __call__(self, img):
        if img.mode != 'RGB':
            img = img.convert('RGB')
        return img
    
transform = transforms.Compose([
    ConvertToRGB(),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Global variables to store loaded model and classes
_model = None
_classes = None
_device = None

def initialize_model():
    """Initialize model once at startup"""
    global _model, _classes, _device
    
    _device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Initializing model on device: {_device}")
    
    _model, model_info = load_model_from_joblib(MODEL_PATH, _device)
    
    if _model is not None and model_info is not None:
        _classes = model_info.get('classes', None)
        print("Model initialized successfully!")
    else:
        print("Failed to initialize model!")

def preprocess_image(image_data: bytes) -> torch.Tensor:
    image = Image.open(io.BytesIO(image_data))
    image = transform(image)
    image = image.unsqueeze(0) 
    image = image.to(_device)
    return image

def classify_image(image_data):
    global _model, _classes, _device
    
    # Initialize model if not already loaded
    if _model is None:
        initialize_model()
    
    if _model is None:
        return {"error": "Failed to load model"}
    
    if _classes is None:
        return {"error": "No classes found in model"}
    
    image = preprocess_image(image_data)
    pred = _model(image)
    pred_val = torch.argmax(pred, dim=1).item()
    confidence = torch.nn.functional.softmax(pred, dim=1)
    pred_class = _classes[pred_val]
    data = {
        "class": pred_class,
        "confidence":  np.round(float(confidence[0][pred_val].item())*100, 2),
    }
    return data

# Initialize model when module is imported
initialize_model()