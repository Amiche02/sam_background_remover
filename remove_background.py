import os
import cv2
import numpy as np
from PIL import Image
from rembg import remove
from segment_anything import sam_model_registry, SamPredictor, SamAutomaticMaskGenerator
import torch
import argparse

def save_image(image, fp):
    image.save(fp)
    print(f"Saved image to {fp}")

def initialize_sam(checkpoint_path):
    try:
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        model_type = "vit_h"
        sam = sam_model_registry[model_type](checkpoint=checkpoint_path).to(device)
        print("SAM initialized successfully")
        return SamPredictor(sam), SamAutomaticMaskGenerator(sam)
    except Exception as e:
        print(f"Error initializing SAM: {e}")
        return None, None

def preprocess_and_segment(predictor, mask_generator, input_image_path):
    try:
        print(f"Processing image: {input_image_path}")
        image_bgr = cv2.imread(input_image_path)
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        
        # Automatic mask generation
        masks = mask_generator.generate(image_rgb)
        print(f"Generated {len(masks)} masks")
        
        # Assuming you want to return the first mask for demonstration purposes
        mask = masks[0]['segmentation']
        mask_image = Image.fromarray(mask.astype(np.uint8) * 255)
        return mask_image
    except Exception as e:
        print(f"Error during image processing and segmentation: {e}")
        return None

def process_images(input_path, output_dir, checkpoint_path):
    predictor, mask_generator = initialize_sam(checkpoint_path)
    if not predictor or not mask_generator:
        print("SAM initialization failed")
        return

    if os.path.isdir(input_path):
        input_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    else:
        input_files = [input_path]

    for file_path in input_files:
        if file_path.endswith(('.png', '.jpg', '.jpeg')):
            processed_image = preprocess_and_segment(predictor, mask_generator, file_path)
            if processed_image:
                base_name = os.path.splitext(os.path.basename(file_path))[0]
                output_file_path = os.path.join(output_dir, f"{base_name}_segmented.png")
                save_image(processed_image, output_file_path)
            else:
                print(f"Segmentation failed for {file_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Remove background from images using SAM.")
    parser.add_argument("--input_dir", type=str, help="Directory containing input images.")
    parser.add_argument("--input_image", type=str, help="Path to a single input image file.")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to save the output images.")
    parser.add_argument("--checkpoint_path", type=str, required=True, help="Path to the SAM checkpoint file.")
    args = parser.parse_args()

    input_path = args.input_image if args.input_image else args.input_dir
    process_images(input_path, args.output_dir, args.checkpoint_path)
