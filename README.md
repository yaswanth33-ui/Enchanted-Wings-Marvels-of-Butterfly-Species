# Butterfly Classification 

A modern web application that uses deep learning to classify butterfly species from images. Built with PyTorch, Flask, and a beautiful frontend interface.

## Features

- 🦋 **AI-Powered Classification**: Uses EfficientNet deep learning model for accurate butterfly species identification
- ⚡ **Fast Processing**: Real-time image classification with confidence scores
- 🎨 **Modern UI**: Beautiful, responsive web interface with drag-and-drop functionality
- 📊 **High Accuracy**: State-of-the-art neural network architecture for reliable predictions
- 💾 **Data Storage**: SQLite database to store images and classification results

## Project Structure

```
ButterflyClassification/
├── frontend/              # Web interface
│   ├── index.html        # Main HTML page
│   ├── styles.css        # CSS styling
│   └── script.js         # JavaScript functionality
├── server/               # Backend API
│   ├── app.py           # Flask application
│   ├── database.py      # Database operations
│   └── utils.py         # Image processing and ML utilities
├── model/               # Machine learning models
│   ├── efficientnet_classifier.py
│   └── model.ipynb      # Training notebook
├── dataset/             # Data and trained models
│   ├── butterfly_classifier_joblib.pkl
│   ├── train/           # Training images
│   └── test/            # Test images
└── requirements.txt     # Python dependencies
```

## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd ButterflyClassification
   ```

2. **Quick Setup (Windows)**

   ```bash
   setup.bat
   ```

   Or manually:

3. **Install Python dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **If you encounter PyTorch/NumPy compatibility issues:**

   ```bash
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
   ```

5. **Verify the model file exists**
   Make sure `dataset/butterfly_classifier_joblib.pkl` exists in your project.

## Usage

### Full AI Classification (Recommended)

1. **Start the Flask server**
   ```bash
   cd server
   python app.py
   ```   

2. **Open the web interface**

   - Open your web browser
   - Navigate to `http://localhost:5000`
   - The beautiful home page will load automatically

3. **Classify butterflies**
   - Click "Start Classifying" or scroll to the classification section
   - Drag and drop an image or click "Choose File" to upload
   - Click "Classify Image" to get the prediction
   - View the species name and confidence score

## API Endpoints

- `GET /` - Serves the frontend home page
- `POST /predict` - Classifies an uploaded image
  ```json
  {
    "image_data": "base64_encoded_image"
  }
  ```
  Response:
  ```json
  {
    "class": "Butterfly Species Name",
    "confidence": 85.99
  }
  ```

## Technologies Used

- **Backend**: Python, Flask, PyTorch, SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Machine Learning**: EfficientNet, Transfer Learning
- **Image Processing**: PIL, OpenCV
- **Database**: SQLite

## Model Architecture

The classification model uses EfficientNet-B0 as the backbone with a custom classifier head:

- Pre-trained EfficientNet-B0 (frozen backbone)
- Custom classifier with dropout for regularization
- Optimized for butterfly species classification

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the [MIT License](LICENSE).

## Support

If you encounter any issues:

1. Make sure all dependencies are installed
2. Check that the model file exists
3. Verify the Flask server is running
4. Check browser console for JavaScript errors

For additional help, please create an issue in the repository.

## Troubleshooting

### Common Issues:

1. **PyTorch/NumPy compatibility error**

   ```
   AttributeError: module 'numpy' has no attribute 'ndarray'
   ```

   **Solution:** Install compatible versions:

   ```bash
   pip uninstall torch torchvision numpy
   pip install numpy==1.24.4
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
   ```

2. **Model file not found**

   - Make sure `server/artifacts/butterfly_classifier_joblib.pkl` exists
   - Check the file path in `server/utils.py`

3. **Import errors**
git push -u origin main
   - Check that all dependencies are installed: `pip list`

4. **Server won't start**

   - Make sure port 5000 is available
   - Try running on a different port: `app.run(port=5001)`

5. **Frontend not loading**
   - Check that the `frontend/` directory exists
   - Verify all files (index.html, styles.css, script.js) are present

### Testing without ML Libraries

If you're having trouble with PyTorch/ML dependencies, you can test the frontend using the simple server:

```bash
cd server
python app.py
```

This will run the application with mock predictions, allowing you to test the beautiful UI while you resolve the ML library issues.
