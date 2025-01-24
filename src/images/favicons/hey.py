from PIL import Image
import os

def create_favicons(input_image_path, output_dir):
    """
    Generates a set of favicons and app icons from a single input image.

    Args:
        input_image_path: Path to the input image (ideally a square image, at least 512x512).
        output_dir: Directory to save the generated icons.
    """
    try:
        img = Image.open(input_image_path)
    except FileNotFoundError:
        print(f"Error: Input image not found at {input_image_path}")
        return
    except Exception as e:
        print(f"An error occurred while opening the image: {e}")
        return

    # Android icons
    android_sizes = [36, 48, 72, 96, 144, 192]
    for size in android_sizes:
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
        filename = f"android-icon-{size}x{size}.png"
        resized_img.save(os.path.join(output_dir, filename), "PNG")

    # Apple icons
    apple_sizes = [57, 60, 72, 76, 114, 120, 144, 152, 180]
    for size in apple_sizes:
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
        filename = f"apple-icon-{size}x{size}.png"
        resized_img.save(os.path.join(output_dir, filename), "PNG")

    # Default apple-icon
    resized_img = img.resize((180, 180), Image.Resampling.LANCZOS)
    resized_img.save(os.path.join(output_dir, "apple-icon.png"), "PNG")

    # Favicons
    favicon_sizes = [16, 32, 48, 64, 128, 256]
    for size in favicon_sizes:
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
        filename = f"favicon-{size}x{size}.png"
        resized_img.save(os.path.join(output_dir, filename), "PNG")

    # Create favicon.ico (multiple sizes in one file)
    favicon_ico_sizes = [(16, 16), (32, 32), (48, 48)]
    resized_imgs = [img.resize(size, Image.Resampling.LANCZOS) for size in favicon_ico_sizes]
    try:
        resized_imgs[0].save(
            os.path.join(output_dir, "favicon.ico"),
            format="ICO",
            sizes=favicon_ico_sizes,
        )
    except Exception as e:
        print(f"An error occurred while saving favicon.ico: {e}")

    # Microsoft icons
    ms_sizes = [70, 144, 150, 310]
    for size in ms_sizes:
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
        filename = f"ms-icon-{size}x{size}.png"
        resized_img.save(os.path.join(output_dir, filename), "PNG")

    print("Favicons and app icons generated successfully!")

# --- Configuration ---
input_image_path = "/media/manideep-reddy/try/public/images1/icons/icon-512x512.png"  # **Change this to your input image path**
output_dir = "/media/manideep-reddy/try/src/images/favicons1"  # Output directory (will be created if it doesn't exist)
# --- End Configuration ---

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Call the function to generate the icons
create_favicons(input_image_path, output_dir)