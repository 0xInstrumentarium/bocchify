import os
import random
from PIL import Image

input_dir = "output"  # Folder from rembg p
final_output_dir = "final"
target_size = (1280, 720)

os.makedirs(final_output_dir, exist_ok=True)

files = sorted(
    [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
)

for idx, filename in enumerate(files, start=1):
    img_path = os.path.join(input_dir, filename)
    img = Image.open(img_path).convert("RGBA")

    # Create 1280x720 transparent background
    canvas = Image.new("RGBA", target_size, (0, 0, 0, 0))

    # Resize original image if it's too big
    scale = min(target_size[0] // 2 / img.width, target_size[1] // 2 / img.height, 1.0)
    new_size = (int(img.width * scale), int(img.height * scale))
    img.resize(new_size, Image.Resampling.LANCZOS)

    # Random position: bottom-left or bottom-right
    x = 0 if random.choice([True, False]) else target_size[0] - new_size[0]
    y = target_size[1] - new_size[1]

    # Paste image onto canvas
    canvas.paste(img, (x, y), img)

    # Save output as numbered PNG
    output_filename = f"{idx}.png"
    output_path = os.path.join(final_output_dir, output_filename)
    canvas.save(output_path)

print(f"Processed {len(files)} images into '{final_output_dir}' folder.")
