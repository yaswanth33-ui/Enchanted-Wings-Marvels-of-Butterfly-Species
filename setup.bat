@echo off
echo Setting up Butterfly Classification Project...
echo.

echo Step 1: Installing Python dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Step 2: Checking if PyTorch is properly installed...
python -c "import torch; print(f'PyTorch version: {torch.__version__}')" 2>nul
if %errorlevel% neq 0 (
    echo Warning: PyTorch installation failed. Installing CPU version...
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
)

echo.
echo Step 3: Checking if all dependencies are working...
python -c "from server.utils import ML_AVAILABLE; print(f'ML Libraries Available: {ML_AVAILABLE}')"

echo.
echo Setup complete!
echo.
echo To start the application:
echo   For full AI functionality: python server/app.py
echo   For demo mode: python server/app_simple.py
echo.
echo Then open http://localhost:5000 in your browser
pause
