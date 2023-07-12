from PIL import Image
import os

def rotate_images(folder_path):
    # List all files in the folder
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        if file_name.lower().endswith('.png'):
            # Open the image file
            image_path = os.path.join(folder_path, file_name)
            image = Image.open(image_path)

            # Rotate the image
            rotated_image = image.rotate(-90, expand=True)

            # Save the rotated image
            rotated_image.save(image_path)

            print(f"Rotated: {file_name}")

# Specify the folder path where PNG files are located
# Still doing the odd thing where it wants me to specify the folder this file is already in
folder_path = 'images/test_scans/google/alzheimer'

# Call the rotate_images function
rotate_images(folder_path)
