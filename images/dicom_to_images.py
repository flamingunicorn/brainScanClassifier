import os
import pydicom
from PIL import Image
import numpy as np
import cv2

def convert_dcm_to_png(dcm_file, output_dir, index):
    # Load the DICOM file
    dcm = pydicom.dcmread(dcm_file)

    # Extract the pixel array from the DICOM file
    pixel_array = dcm.pixel_array

    # Rescale pixel values using Rescale Slope and Rescale Intercept
    if 'RescaleSlope' in dcm and 'RescaleIntercept' in dcm:
        slope = dcm.RescaleSlope
        intercept = dcm.RescaleIntercept
        pixel_array = pixel_array * slope + intercept

    # Normalize pixel values to 8-bit range (0-255)
    pixel_array = pixel_array.astype(np.uint8)

    # Check if the image contains a full head or is mostly black
    if not contains_full_head(pixel_array):
        return None

    # Convert and save the pixel array as PNG image
    image = Image.fromarray(pixel_array)
    image_path = os.path.join(output_dir, f"4_p_scan{index}.png")
    image.save(image_path)

    return image_path


def contains_full_head(pixel_array, threshold=50):
    # Calculate the mean intensity of the pixel array
    mean_intensity = np.mean(pixel_array)

    # Check if the mean intensity exceeds the threshold
    if mean_intensity > threshold:
        # Convert the pixel array to an 8-bit image
        pixel_array = pixel_array.astype(np.uint8)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(pixel_array, (11, 11), 0)

        # Apply Hough Circle Transform to detect circles
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=120, param1=70, param2=40, minRadius=30, maxRadius=110)

        # Check if circles are detected
        if circles is not None:
            return True

    return False

def convert_folder_dcm_to_png(input_folder, output_folder):
    # Get a list of all DICOM files in the input folder
    
    dcm_files = [f for f in os.listdir(input_folder) if f.endswith('.dcm')]

    # Convert each DICOM file to PNG and save in the output folder
    converted_images = []
    for i, dcm_file in enumerate(dcm_files):
        dcm_file_path = os.path.join(input_folder, dcm_file)
        converted_image_path = convert_dcm_to_png(dcm_file_path, output_folder, i)
        if converted_image_path is not None:
            converted_images.append(converted_image_path)

    return converted_images

# Paths (i have no idea why its only working when i put the images folder cause we are already in it)
input_folder = "images/PPMI/100018/3D_T2_FLAIR_ti1650_ND_MPR_Tra/2023-03-16_08_26_01.0/I1701007" # Update with the path to your input folder containing DICOM files

output_folder = "images/data/parkinson"  # Update with the desired output folder

converted_images = convert_folder_dcm_to_png(input_folder, output_folder)
print(f"Converted {len(converted_images)} DICOM images to PNG.")
