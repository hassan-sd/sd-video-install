@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

:: Clone the generative-models repository
git clone https://github.com/Stability-AI/generative-models.git

:: Change directory to generative-models
cd generative-models

:: Download additional files
powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/hassan-sd/sd-video-install/main/video_sampling.py' -OutFile 'video_sampling.py'"
powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/hassan-sd/sd-video-install/main/streamlit_helpers.py' -OutFile 'scripts\demo\streamlit_helpers.py'"

:: Create a folder called "Checkpoints"
mkdir Checkpoints

:: Download files to the Checkpoints folder
powershell -Command "Invoke-WebRequest -Uri 'https://huggingface.co/stabilityai/stable-video-diffusion-img2vid/resolve/main/svd.safetensors?download=true' -OutFile 'Checkpoints\svd.safetensors'"
powershell -Command "Invoke-WebRequest -Uri 'https://huggingface.co/stabilityai/stable-video-diffusion-img2vid/resolve/main/svd_image_decoder.safetensors?download=true' -OutFile 'Checkpoints\svd_image_decoder.safetensors'"
powershell -Command "Invoke-WebRequest -Uri 'https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/resolve/main/svd_xt.safetensors?download=true' -OutFile 'Checkpoints\svd_xt.safetensors'"
powershell -Command "Invoke-WebRequest -Uri 'https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/resolve/main/svd_xt_image_decoder.safetensors?download=true' -OutFile 'Checkpoints\svd_xt_image_decoder.safetensors'"

:: Download the requirements.txt file to the /requirements directory
mkdir requirements
powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/hassan-sd/sd-video-install/main/requirements.txt' -OutFile 'requirements\requirements.txt'"

:: Create a virtual environment called venv
python -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate.bat

:: Install all requirements
pip install -r requirements\requirements.txt

:: Run the Streamlit application
streamlit run video_sampling.py
