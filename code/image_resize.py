# Cell 이미지 사이즈 조정

import xml.etree.ElementTree as ET
import csv
import os
from PIL import Image

for file in os.listdir("./jpg_files"):
    file_path = os.path.join("./jpg_files", file)


    if (os.path.isfile(file_path)):
        source_image = file_path
        target_image = 'resize_' + file
        image = Image.open(source_image)
        resize_image = image.resize((640, 480))
        resize_image.save(target_image, "JPEG", quality=95)
