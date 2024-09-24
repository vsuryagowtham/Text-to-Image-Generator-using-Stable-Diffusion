"""
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from diffusers import StableDiffusionPipeline
import torch

# Function to generate image based on prompt
def generate_image(prompt, token):
    # Load the model from Hugging Face using your token
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        use_auth_token=token
    ).to("cuda" if torch.cuda.is_available() else "cpu")

    # Generate the image
    image = pipe(prompt).images[0]

    # Save the image
    image_path = "generated_image.png"
    image.save(image_path)
    
    return image_path

# Tkinter GUI App
class ImageGeneratorApp(tk.Tk):
    def __init__(self, token):
        super().__init__()
        self.token = token
        self.title("Image Generator using Stable Diffusion")
        self.geometry("600x600")
        
        # Label
        self.label = tk.Label(self, text="Enter Prompt:")
        self.label.pack(pady=10)
        
        # Text entry for prompt
        self.prompt_entry = tk.Entry(self, width=50)
        self.prompt_entry.pack(pady=10)
        
        # Generate button
        self.generate_button = tk.Button(self, text="Generate", command=self.generate_image)
        self.generate_button.pack(pady=10)
        
        # Label to display generated image
        self.image_label = tk.Label(self)
        self.image_label.pack(pady=10)

    def generate_image(self):
        prompt = self.prompt_entry.get()
        image_path = generate_image(prompt, self.token)
        
        # Display generated image
        img = Image.open(image_path)
        img = img.resize((400, 400), Image.LANCZOS)  # Resize image
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk


if __name__ == "__main__":
    token = "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"
    app = ImageGeneratorApp(token)
    app.mainloop()
"""

import tkinter as tk
import customtkinter as ctk 
from PIL import Image, ImageTk
from authtoken import auth_token
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline 

# Create the app
app = tk.Tk()
app.geometry("532x632")
app.title("Stable Bud") 
ctk.set_appearance_mode("dark") 

# Entry for the prompt with `app` as master
prompt = ctk.CTkEntry(master=app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white") 
prompt.place(x=10, y=10)

# Label to display the image
lmain = ctk.CTkLabel(master=app, height=512, width=512)
lmain.place(x=10, y=110)

# Set up the Stable Diffusion pipeline
modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token) 
pipe.to(device) 

# Function to generate the image
def generate(): 
    with autocast(device): 
        image = pipe(prompt.get(), guidance_scale=8.5).images[0]
    
    image.save('generatedimage.png')
    img = Image.open('generatedimage.png')
    img = img.resize((512, 512), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    lmain.configure(image=img_tk)
    lmain.image = img_tk  # Keep a reference to avoid garbage collection

# Generate button
trigger = ctk.CTkButton(master=app, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="blue", command=generate) 
trigger.configure(text="Generate") 
trigger.place(x=206, y=60) 

app.mainloop()
