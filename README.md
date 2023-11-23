
# Stable Diffusion Video Generative Models Setup Guide

This guide provides instructions on how to set up the Stable Diffusion Video Generative Models repository using two different methods: a Batch file for Windows users and a Python script for cross-platform compatibility (Windows, macOS, and Linux).

## Prerequisites

Before proceeding, ensure you have the following installed:

-   Git
-   Python (3.6 or newer)
-   pip (Python package installer)

## Method 1: Using Batch File (Windows Only)

### Step 1: Download the Batch File

Download the `setup-generative-models.bat` file from the repository.

### Step 2: Run the Batch File

Double-click on the `install-sd-video.bat` file to run it. This script will:

-   Clone the generative-models repository
-   Download necessary files and scripts
-   Create a Python virtual environment
-   Install required dependencies
-   Prepare the system to run the Streamlit application

### Step 3: Activate the Virtual Environment

After the script execution, navigate to the repository's root directory and activate the virtual environment:

bashCopy code

`cd generative-models
venv\Scripts\activate` 

### Step 4: Run the Application

With the virtual environment activated, start the Streamlit application:

arduinoCopy code

`streamlit run video_sampling.py` 

## Method 2: Using Python Script (Cross-Platform)

### Step 1: Download the Python Script

Download the `install-sd-video.py` file from the repository.

### Step 2: Run the Python Script

Execute the script using Python:

Copy code

`python python install-sd-video.py` 

This script performs similar tasks as the batch file but is compatible with multiple operating systems.

### Step 3: Activate the Virtual Environment

After the script execution, follow the printed instructions to activate the virtual environment and install the required dependencies.

### Step 4: Run the Application

Once the dependencies are installed, start the Streamlit application:

arduinoCopy code

`streamlit run video_sampling.py` 

## Troubleshooting

If you encounter any issues during the installation or execution process, ensure all prerequisites are correctly installed and up-to-date. For further assistance, consult the official documentation or reach out to the support community.
