from pathlib import Path
from PIL import Image
import numpy as np
import pandas as pd

image_dir = Path("cropped_faces")
imgs=[]
for img_path in sorted(image_dir.glob("*.jpg")):
    img = Image.open(img_path).convert('L')
    pixel_arr = np.array(img).flatten()
    imgs.append(pixel_arr)

df = pd.DataFrame(imgs)
df.to_csv("faces.csv", header=False, index = False)