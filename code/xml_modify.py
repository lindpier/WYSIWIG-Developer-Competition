# Annotation XML 파일의 레이블 사이즈 조정
# XML 파일의 레이블 사이즈 업데이트 하여 저장

import xml.etree.ElementTree as ET
import os

for file in os.listdir("./xml_files"):
    file_path = os.path.join("./xml_files", file)
    tree = ET.parse(file_path)
    root = tree.getroot()

    if (os.path.isfile(file_path)):
        #L = ['size', 'bndbox']
        for size in root.iter('size'):
            re_size_width = str(int(int(size.find('width').text)/2))
            re_size_height = str(int(int(size.find('height').text)/2))
            size.find('width').text = re_size_width
            size.find('height').text = re_size_height

        #for object in root.iter('object'):
        for bndbox in root.iter('bndbox'):
            re_size_xmin = str(int(int(bndbox.find('xmin').text)/2))
            re_size_ymin = str(int(int(bndbox.find('ymin').text)/2))
            re_size_xmax = str(int(int(bndbox.find('xmax').text)/2))
            re_size_ymax = str(int(int(bndbox.find('ymax').text)/2))
            bndbox.find('xmin').text = re_size_xmin
            bndbox.find('ymin').text = re_size_ymin
            bndbox.find('xmax').text = re_size_xmax
            bndbox.find('ymax').text = re_size_ymax

    tree.write('resize_' + file)