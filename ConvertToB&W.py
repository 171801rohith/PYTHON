import os
from PIL import Image

input_folder = r'C:/Users/rohit/Downloads/ChallengersSeniors'
output_folder = r'C:/Users/rohit/Downloads/ChallengersSeniorsBW'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        bw = img.convert('L')

        save_path = os.path.join(output_folder, filename)
        bw.save(save_path)

print("All images have been converted and saved.")
