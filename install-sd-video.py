import os
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# Clone the generative-models repository
run_command(["git", "clone", "https://github.com/Stability-AI/generative-models.git"])

# Change directory to generative-models
os.chdir("generative-models")

# Download additional files
run_command(["curl", "-LJO", "https://raw.githubusercontent.com/hassan-sd/sd-video-install/main/video_sampling.py"])
run_command(["curl", "-LJO", "https://raw.githubusercontent.com/hassan-sd/sd-video-install/main/streamlit_helpers.py", "-o", "scripts/demo/streamlit_helpers.py"])

# Create a folder called "Checkpoints"
os.makedirs("Checkpoints", exist_ok=True)

# Download files to the Checkpoints folder
checkpoint_urls = [
    "https://huggingface.co/stabilityai/stable-video-diffusion-img2vid/resolve/main/svd.safetensors?download=true",
    "https://huggingface.co/stabilityai/stable-video-diffusion-img2vid/resolve/main/svd_image_decoder.safetensors?download=true",
    "https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/resolve/main/svd_xt.safetensors?download=true",
    "https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/resolve/main/svd_xt_image_decoder.safetensors?download=true"
]

for url in checkpoint_urls:
    run_command(["curl", "-L", url, "-o", os.path.join("Checkpoints", os.path.basename(url).split("?")[0])])

# Download the requirements.txt file to the /requirements directory
os.makedirs("requirements", exist_ok=True)
run_command(["curl", "-LJO", "https://raw.githubusercontent.com/hassan-sd/sd-video-install/main/requirements.txt", "-o", "requirements/requirements.txt"])

# Create a virtual environment called venv
run_command([sys.executable, "-m", "venv", "venv"])

# Activate the virtual environment
# This step is platform dependent
if sys.platform == "win32":
    activate_script = os.path.join("venv", "Scripts", "activate")
else:
    activate_script = os.path.join("venv", "bin", "activate")

print(f"Please activate the virtual environment by running 'source {activate_script}'.")
print("Then run 'pip install -r requirements/requirements.txt'.")
print("After installing the requirements, install xformers using 'pip install -U xformers --index-url https://download.pytorch.org/whl/cu121'.")
print("Finally, run 'streamlit run video_sampling.py' to open the tool.")
