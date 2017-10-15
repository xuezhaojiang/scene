import numpy as np
import json
import os
import shutil
import argparse

def picture_classify(images_dir, label_path, target_dir):
  data_dict = {}
  with open(label_path, "r") as label_file:
    label_list = json.load(label_file)
  for image_info in label_list:
    data_dict[image_info["image_id"]] = int (image_info["label_id"])
  for image_file in os.listdir(images_dir):
    label_id = data_dict[image_file]
    if not os.path.exists(os.path.join(target_dir, str(label_id))):
      os.makedirs(os.path.join(target_dir, str(label_id)))
    shutil.copyfile(os.path.join(images_dir, image_file), os.path.join(target_dir, str(label_id), image_file))

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--images_dir", 
                         type = str, 
                       default = "scene_train_images_20170904", 
                       help = "input the dir where the images in")
  parser.add_argument("--label_path",
                          type = str,
                          default = "scene_train_annotations_20170904.json",
                          help = "input the label file")
  parser.add_argument("--target_dir",
                          type = str,
                          default = "images_classified",
                          help = "input the dir where the result output")

  args = parser.parse_args()

  if not os.path.exists(args.target_dir):
    os.makedirs(args.target_dir)

  picture_classify(args.images_dir, args.label_path, args.target_dir)


if __name__ == "__main__":
  main()
