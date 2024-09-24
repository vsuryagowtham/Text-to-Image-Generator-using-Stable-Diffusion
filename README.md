# Text-to-Image-Generator-using-Stable-Diffusion
## Overview
This project implements a machine learning application that generates high-quality images from text prompts using the Stable Diffusion model. Built with Python, it features a graphical user interface (GUI) created using Tkinter. The application leverages the **Stable Diffusion Pipeline** from Hugging Face to generate images directly on a CUDA-enabled device.

## Features
- **Text-to-Image Generation**: Converts user-provided text prompts into visually appealing images using the power of deep learning and Stable Diffusion.
- **Real-Time Image Display**: After generating the image, it is automatically displayed within the application using the PIL (Python Imaging Library).
- **Simple GUI**: A Tkinter-based graphical interface allows easy input of prompts and viewing of generated images.
  
## Project Structure
```bash
Text-to-Image-Generator/
│
├── 1App.py                   # Main Python script for running the application
├── authtoken.py               # Authentication token for accessing Stable Diffusion API
├── README.md                  # Project documentation
└── requirements.txt           # List of dependencies for the project
```

## How It Works
-User Input: The user enters a text prompt into the application via the Tkinter interface.
-Image Generation: The Stable Diffusion model processes the text and generates an image that reflects the prompt.
-Display: The generated image is displayed directly in the application window.

## Installation and Setup
### Prerequisites
Ensure you have the following installed:
-Python 3.8+
-pip (Python package manager)
-CUDA-enabled GPU (for faster image generation using the GPU)

### Clone the Repository
```bash
git clone https://github.com/your-username/text-to-image-generator.git
cd text-to-image-generator
```
### Running the Application
To launch the application, run the following command:

```bash
Copy code
python 1App.py
```
