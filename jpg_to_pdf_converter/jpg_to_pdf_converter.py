import os
from PIL import Image

def jpg_to_pdf(path):
    # Get all of the .jpg files in the specified directory
    jpg_files = [f for f in os.listdir(path) if f.endswith('.jpg')]
  
    # Sort the files by page number
    jpg_files.sort(key=lambda x: int(x.split('-')[-1].split('.')[0]))
   
    # Create a list to hold the image objects
    images = []
   
    # Open each image and add it to the list
    for jpg_file in jpg_files:
        images.append(Image.open(os.path.join(path, jpg_file)))
   
    # Save the images as a PDF
    images[0].save(os.path.join(path, 'output.pdf'), save_all=True, append_images=images[1:])

jpg_to_pdf('./')