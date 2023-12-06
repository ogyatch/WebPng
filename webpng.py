from PIL import Image
import sys

def convert_webp_to_png(webp_file_path):
    with Image.open(webp_file_path) as img:
        png_file_path = webp_file_path.rsplit('.', 1)[0] + '.png'
        img.save(png_file_path, 'PNG')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        convert_webp_to_png(sys.argv[1])
    else:
        print("Usage: python webpng.py <file_path>")
