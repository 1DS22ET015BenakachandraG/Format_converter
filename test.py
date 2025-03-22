import os
# from format_imageben import convert_format
from format_imageben.main import convert_format


def test_image_conversion():
    input_image = "input/images.jpeg"  # Change this to a valid test image path
    output_formats = ["png", "jpg", "bmp", "webp"]
    
    for fmt in output_formats:
        print(f"Testing conversion to {fmt}...")
        output_path = convert_format(input_image, fmt)
        
        # Check if file was created
        if os.path.exists(output_path):
            print(f"✅ Test passed: {output_path} exists")
        else:
            print(f"❌ Test failed: {output_path} was not created")

if __name__ == "__main__":
    test_image_conversion()