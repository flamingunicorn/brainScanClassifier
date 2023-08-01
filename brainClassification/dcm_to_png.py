import os
import pydicom
from PIL import Image
import numpy as np
import cv2

# ================== conversion with OUT filtering =======================

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
    pixel_array = pixel_array.astype(np.float32)
    pixel_array = ((pixel_array - np.min(pixel_array)) / (np.max(pixel_array) - np.min(pixel_array))) * 255
    pixel_array = pixel_array.astype(np.uint8)

    # Convert and save the pixel array as PNG image
    image = Image.fromarray(pixel_array)
    image_path = os.path.join(output_dir, f"ppmicontrol_1_scan{index}.png")
    image.save(image_path)

    return image_path

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


# ================== conversion with filtering =======================

""" def convert_dcm_to_png(dcm_file, output_dir, index):
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
    pixel_array = pixel_array.astype(np.float32)
    pixel_array = ((pixel_array - np.min(pixel_array)) / (np.max(pixel_array) - np.min(pixel_array))) * 255
    pixel_array = pixel_array.astype(np.uint8)

    # Check if the image is mostly black or has a small brain
    if np.sum(pixel_array <= black_threshold) == pixel_array.size or np.sum(pixel_array > brain_threshold) < brain_pixels_threshold:
        return None

    # Convert and save the pixel array as PNG image
    image = Image.fromarray(pixel_array)
    image_path = os.path.join(output_dir, f"scan{index}.png")
    image.save(image_path)
    print(image_path)
    return image_path

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

# Parameters for filtering
black_threshold = 10  # Adjust this threshold value for black background
brain_threshold = 200  # Adjust this threshold value for small brain
brain_pixels_threshold = 500  # Adjust this threshold value for minimum number of brain pixels """