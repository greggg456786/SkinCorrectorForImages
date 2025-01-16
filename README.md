<h1>Enhance Skin Tone and Color Contrast Adjuster</h1>
Overview

This project was originally created to boost the color contrast in images generated using AI, especially focusing on enhancing skin tones in portraits or similar images. AI-generated images can sometimes have unnatural skin colors or poor contrast, and this tool is designed to address that issue. By detecting and adjusting the skin regions in images, it helps make AI-generated visuals look more vibrant, realistic, and visually appealing.
How It Works

This script processes images to detect skin regions and adjusts the colors in those areas for better vibrancy and contrast. It uses the following steps:

    Detecting Skin Regions:
        The script first detects skin tones by analyzing the image in the HSV color space. This approach isolates skin tones based on a range of hue, saturation, and brightness values that match common skin color patterns.

    Adjusting Skin Tone:
        Once skin regions are detected, the script makes subtle adjustments to the saturation (for more vibrancy) and the brightness (for a more balanced look). This enhances the natural appearance of the skin while maintaining realism.

    Batch Processing:
        You can process multiple images at once by providing a folder of images. The script will automatically apply the skin tone adjustments to all supported image files in the folder.

    Saving the Processed Images:
        After processing, the adjusted images are saved in a new folder, allowing you to compare the original and modified images easily.

This script is especially useful for images generated using AI tools (like DALL·E, MidJourney, or Stable Diffusion) where skin tones may look artificial or unnatural.
Features

    Skin Tone Adjustment: Automatically detects and adjusts skin tones for better vibrancy and natural look.
    Batch Processing: Process all images in a folder, saving you time.
    Compatibility with Various Image Formats: Supports popular image formats like .png, .jpg, .jpeg, .bmp, .gif, .tiff.
    Easy to Use: A simple command-line interface that allows you to select input and output folders.

Installation

To get started with this project, you need to clone the repository and install the necessary dependencies.
1. Clone the repository:

git clone https://github.com/greggg456786/SkinCorrectorForImages
cd skin-tone-adjuster

2. Install dependencies:

You'll need Python (preferably version 3.6 or later) and some essential libraries. You can install them using pip:

pip install -r requirements.txt

requirements.txt includes:

    opencv-python: For image processing tasks like detecting skin tones.
    numpy: For working with arrays and image matrices.
    Pillow: For handling image file reading and saving.
    torch and torchvision: To allow for future deep learning enhancements (optional, not strictly necessary for basic functionality).
    tqdm: For displaying progress bars during batch processing.

3. (Optional) Install additional dependencies for advanced use cases:

If you want to extend this project with deep learning models or advanced features, you may need to install extra packages or frameworks (like PyTorch-based skin detection models). But for basic functionality, the dependencies listed in requirements.txt should be enough.
Usage

Once you’ve installed everything, you're ready to start processing your images! Here's how to use the script:

    Run the script:

    python app.py

    Provide Input and Output Folders:

    You'll be prompted to enter two folder paths:
        Input Folder: This should be the folder containing the images you want to adjust. The script will process all images in this folder (supports .png, .jpg, .jpeg, .bmp, .gif, .tiff).
        Output Folder: This is where the processed images will be saved. The script will add a processed_ prefix to each output image file.

    Check Processed Images:

    After processing, your adjusted images will be saved in the output folder. You can now view them and compare them with the original images.

Example

Let's say you have a folder of AI-generated portraits with unnatural skin tones. Simply run the script and specify the folder locations:

python adjust_skin_tones.py

Enter the input folder path (e.g., ./ai-generated-portraits) and output folder path (e.g., ./adjusted-portraits). The script will process the images and save them with enhanced skin tones and contrast in the adjusted-portraits folder.
Tips for Best Results

    Image Quality: The script works best with high-quality images where the skin regions are clearly visible. If the skin is hard to distinguish from the background, the adjustments may not be as effective.

    Skin Tone Variations: The default skin detection works for a wide range of skin tones, but if the results aren't perfect for some images (especially in complex lighting), you can tweak the lower_skin and upper_skin HSV ranges in the detect_skin function to better capture your desired skin tones.

    Adjusting Saturation/Contrast: The code applies fixed values for saturation and brightness adjustments. For more control, you could modify these values based on the specific characteristics of your images.

    Batch Processing Large Datasets: If you have a large number of images, the batch processing can take a while. Consider splitting the task into smaller batches or using multi-threading for faster processing.

Future Improvements

This script is a basic implementation for skin tone enhancement and contrast boosting. Future versions might include:

    Machine Learning-based Skin Detection: Integrating deep learning models for more accurate skin segmentation.
    Customization Options: Allowing users to control the level of saturation/brightness adjustments interactively.
    Multi-threading or Parallel Processing: To speed up processing for large datasets.

Contributing

If you find bugs, have suggestions, or want to add new features, feel free to create an issue or submit a pull request. Contributions are welcome!
License

This project is licensed under the MIT License – see the LICENSE file for details.
Acknowledgements

    This project uses OpenCV for image processing.
    Thanks to the creators of tqdm for the progress bar functionality.

Feel free to modify and adjust this README as needed. It provides a clear, engaging explanation of the code's purpose and functionality while making it easy for users to understand how to use the tool and contribute.
