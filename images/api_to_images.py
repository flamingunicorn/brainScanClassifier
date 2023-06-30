import requests
import os

# NeuroVault API endpoint for images
api_url = 'http://neurovault.org/api/images/'

# Query parameters to filter images (e.g., Alzheimer's-related)
query_params = {
    'name': 'Alzheimer',  # Example: searching for images with "Alzheimer" in their name
    # Add more query parameters as needed to narrow down the search
}

# Send GET request to the API endpoint
response = requests.get(api_url, params=query_params)

if response.status_code == 200:
    # Successful request
    data = response.json()

    # Create the folder to save the images
    folder_name = 'practice_images'
    os.makedirs(folder_name, exist_ok=True)

    # Iterate over the retrieved images
    for image in data['results']:
        # Access the desired information for each image
        image_id = image['id']
        image_name = image['name']
        image_file = image['file']

        # Download the image file
        file_url = image_file
        file_name = f"{image_id}_{image_name}.nii.gz"  # Customize the file naming as desired
        file_path = os.path.join(folder_name, file_name)

        response = requests.get(file_url)
        with open(file_path, 'wb') as file:
            file.write(response.content)

        # Print or perform further processing with the image details
        print(f"Image ID: {image_id}")
        print(f"Image Name: {image_name}")
        print(f"Image File: {file_name}")
        print(f"File saved to: {file_path}")
        print()

else:
    # Error handling for failed request
    print(f"Request failed with status code: {response.status_code}")
