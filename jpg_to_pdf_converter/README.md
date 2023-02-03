# Jpg to pdf converter

A python script for converting all .jpg files in a directory to .pdf. This script will take all ".jpg" files in the directory where this script is called, fuse them and save them as a single pdf file. It assumes that the files are named in the following way : "name-x.jpg" where x is a number. The name part cannot have a - in it.

I mainly use it to create a pdf out of a Goodnotes file by exporting all pages as image, and then merging them into a single pdf. It is useful if your file is long and has a lot of pasted images in it, since sometimes the pdf conversion will bug out.

## Usage

1. Create a folder with the name of the pdf you want to create in a folder containing the script. For example, if you want to create a pdf called "my_pdf", create a folder called "my_pdf".
2. Inside of this put all of your images. Each image should be named in the following way : "name-x.jpg" where x is a number. The name part cannot have a - in it.
3. Execute the script. It will create a pdf file called "my_pdf.pdf" in the same folder as the script.

The script will search all subdirectories for images, so you can have a folder structure like this :

```
my_pdf1
|- image1-1.jpg
|- image1-2.jpg
|- ...
my_pdf2
|- image2-1.jpg
|- image2-2.jpg
|- ...
script.py
```

And it will create two pdf files : "my_pdf1.pdf" and "my_pdf2.pdf".
