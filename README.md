# Computer Vision Project
Detecting Traffic Law Violators Running through Red Light Using Pre-Trained YOLOv8 Model

---

## Pre-Requisites:
1. [Python 3.9](https://www.python.org/downloads/release/python-3913/)
2. Terminal (Windows PowerShell)
3. IDE ([Microsoft Visual Studio Code](https://code.visualstudio.com/download))

## How to Use This:
1. Clone this repository
   ```bash
   git clone git@github.com:AhdaArif/YOLOv8.git
   ```
2. Generate virtual environment
   ```bash
   py -3.9 -m venv Env
   ```
3. Activate the environment
   ```bash
   ./Env/Scripts/Activate.ps1
   ```
4. Install Numpy
   ```bash
   py install numpy
   ```
5. Downgrade the PIP to the version 21.1.1
   ```bash
   ./Env/Scripts/python.exe -m pip install pip==21.1.1
   ```
6. Install LAP
   ```bash
   pip install lap
   ```
7. Reupgrade the PIP to the latest
   ```bash
   ./Env/Scripts/python.exe -m pip install -U pip
   ```
8. Install PyTorch with CUDA support or not
   
   For CUDA-capable system:
   ```bash
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
   ```
   For just of CPU use, without GPU acceleration:
   ```bash
   pip install torch torchvision
   ```
9. Install Ultralytics
   ```bash
   pip install ultralytics
   ```