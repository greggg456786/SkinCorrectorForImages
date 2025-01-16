import cv2
import numpy as np
import torch
from torchvision import transforms
from PIL import Image
import os
import glob
from tqdm import tqdm

# Function to detect skin region in the image (using a heuristic approach)
def detect_skin(image):
    # Convert to HSV color space to isolate skin tones (heuristic approach)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Skin color range in HSV (this range can be adjusted)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Create a mask that captures only the skin areas
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Bitwise AND the mask with the image to keep only the skin regions
    skin = cv2.bitwise_and(image, image, mask=mask)
    return skin, mask

# Function to adjust the skin regions in the image
def adjust_skin_tones(image, mask):
    # Convert the image to HSV
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Split the image into H, S, and V channels
    h, s, v = cv2.split(img_hsv)

    # Step 1: Slightly increase the saturation to make the skin more vibrant
    s = cv2.add(s, 20)  # Add to the saturation channel for vibrance

    # Step 2: Adjust the value (brightness) of the skin
    v = cv2.add(v, 10)  # Slightly increase the brightness

    # Step 3: Merge the channels back and convert to BGR
    img_hsv = cv2.merge([h, s, v])
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    # Step 4: Mask the regions to adjust only the skin
    img_bgr[mask > 0] = img_bgr[mask > 0]

    return img_bgr

# Function to adjust the image (only skin regions) using Torch and OpenCV
def adjust_image(image_path):
    try:
        # Read the image with OpenCV
        img = cv2.imread(image_path)

        # Convert the image to RGB (OpenCV reads images in BGR by default)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Step 1: Detect skin regions
        skin, mask = detect_skin(img)

        # Step 2: Apply the skin tone correction (brightness, saturation)
        img_rgb = adjust_skin_tones(img_rgb, mask)

        # Step 3: Convert back to PIL Image for saving
        img_pil = Image.fromarray(img_rgb)

        return img_pil
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

# Batch process all images in a folder
def batch_process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Use glob to find all image files
    image_files = glob.glob(os.path.join(input_folder, "*.*"))
    
    # Filter image files (ensure we handle common image formats)
    image_files = [f for f in image_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff'))]

    print(f"Found {len(image_files)} image(s) to process...")

    # Iterate through all images and process them
    for image_path in tqdm(image_files, desc="Processing images"):
        filename = os.path.basename(image_path)
        processed_image = adjust_image(image_path)

        if processed_image:
            # Save the processed image
            output_path = os.path.join(output_folder, f"processed_{filename}")
            processed_image.save(output_path)
            print(f"Saved processed image to {output_path}")
        else:
            print(f"Skipping {filename} due to error during processing.")

    print("Batch processing complete!")

# Main function to run the process
def main():
    print("Welcome to the Batch Image Processor!")
    
    # Get input and output folder paths from user
    input_folder = input("Enter the full path to the folder with images to process: ").strip()
    if not os.path.isdir(input_folder):
        print("Invalid input folder path. Exiting...")
        return

    output_folder = input("Enter the full path to the folder where processed images should be saved: ").strip()
    if not os.path.isdir(output_folder):
        print("Invalid output folder path. Exiting...")
        return
    
    # Process images in the selected folder
    batch_process_images(input_folder, output_folder)

if __name__ == "__main__":
    main()
