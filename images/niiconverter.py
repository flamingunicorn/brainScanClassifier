import nibabel as nib
import numpy as np
from PIL import Image

import cv2

def check_full_brain(scan_data, threshold=50):
    # Calculate the mean intensity of the scan data
    mean_intensity = np.mean(scan_data)

    # Check if the mean intensity exceeds the threshold
    if mean_intensity > threshold:
        # Convert the scan data to an 8-bit image
        scan_data = scan_data.astype(np.uint8)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(scan_data, (11, 11), 0)

        # Apply Hough Circle Transform to detect circles
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=120, param1=70, param2=40, minRadius=30, maxRadius=110)

        # Check if circles are detected
        if circles is not None:
            return True

    return False

def brain_scan(nii_data):
    # Iterate over each scan in the NIfTI data
    for scan_index in range(nii_data.shape[-1]):
        # Extract the scan data
        scan_data = nii_data[..., scan_index]

        # Replace invalid values with the minimum and maximum values
        scan_data = np.nan_to_num(scan_data, nan=np.min(scan_data), posinf=np.max(scan_data), neginf=np.min(scan_data))

        # Normalize the scan data to [0, 255]
        scan_data = (scan_data - np.min(scan_data)) / (np.max(scan_data) - np.min(scan_data)) * 255

        # Check if the scan contains a full brain
        has_full_brain = check_full_brain(scan_data)
        
        if has_full_brain:
            image = Image.fromarray(scan_data)
            image = image.convert("L")
            image.save(f'practice_images/alzheimer/a_scan_{scan_index}.png')  # Change the file extension as needed


# Specify the path to the NIfTI file
nii_path = 'practice_images/71_MNI 1mm.nii.gz'
# Parkinson images
# nitrc/guest-20230622_221143/p06871/dwi_1000/NIfTI/p06871_bmatrix_1000.nii
# nitrc\guest-20230622_221143\p06871\dwi_1000\NIfTI
# Control images
# ida_control_autism/ABIDE/50050/MP-RAGE/2000-01-01_00_00_00.0/I328317/control.nii


# Load the NIfTI file
nii_img = nib.load(nii_path)

# Access the image data as a NumPy array
nii_data = nii_img.get_fdata()

# Iterate over each scan in the NIfTI data
brain_scan(nii_data)


