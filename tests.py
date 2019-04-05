import os

ROOT_DIR = os.path.abspath("../")
IMAGE_DIR = os.path.join(ROOT_DIR, "Mask_RCNN/images")
print(IMAGE_DIR)
file_names = next(os.walk(IMAGE_DIR))[2]
print(file_names)

