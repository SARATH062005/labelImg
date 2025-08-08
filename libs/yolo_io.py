#!/usr/bin/env python
# -*- coding: utf8 -*-
import codecs
import os

from libs.constants import DEFAULT_ENCODING

TXT_EXT = '.txt'
ENCODE_METHOD = DEFAULT_ENCODING

class YOLOWriter:
    """
    The YOLOWriter class creates a YOLO format annotation file (.txt).
    This format is compatible with YOLOv3, v5, v7, and v8.
    """

    def __init__(self, folder_name, filename, img_size, database_src='Unknown', local_img_path=None):
        self.folder_name = folder_name
        self.filename = filename
        self.database_src = database_src
        self.img_size = img_size
        self.box_list = []
        self.local_img_path = local_img_path
        self.verified = False

    def add_bnd_box(self, x_min, y_min, x_max, y_max, name, difficult):
        bnd_box = {'xmin': x_min, 'ymin': y_min, 'xmax': x_max, 'ymax': y_max}
        bnd_box['name'] = name
        bnd_box['difficult'] = difficult
        self.box_list.append(bnd_box)

    def bnd_box_to_yolo_line(self, box, class_list=[]):
        """
        This method correctly converts a bounding box to the YOLO format.
        """
        x_min = box['xmin']
        x_max = box['xmax']
        y_min = box['ymin']
        y_max = box['ymax']

        # The center coordinates are calculated and normalized.
        x_center = float((x_min + x_max)) / 2 / self.img_size[1]
        y_center = float((y_min + y_max)) / 2 / self.img_size[0]

        # The width and height are calculated and normalized.
        w = float((x_max - x_min)) / self.img_size[1]
        h = float((y_max - y_min)) / self.img_size[0]

        # The class name is looked up to find the correct index.
        box_name = box['name']
        if box_name not in class_list:
            class_list.append(box_name)

        class_index = class_list.index(box_name)

        return class_index, x_center, y_center, w, h

    def save(self, class_list=[], target_file=None):
        """
        Saves the YOLO formatted bounding boxes to a .txt file.
        It also creates a `classes.txt` file for reference.
        """
        out_file = None  # Update yolo .txt
        out_class_file = None   # Update class list .txt

        if target_file is None:
            out_file = open(
            self.filename + TXT_EXT, 'w', encoding=ENCODE_METHOD)
            classes_file = os.path.join(os.path.dirname(os.path.abspath(self.filename)), "classes.txt")
            out_class_file = open(classes_file, 'w')

        else:
            out_file = codecs.open(target_file, 'w', encoding=ENCODE_METHOD)
            classes_file = os.path.join(os.path.dirname(os.path.abspath(target_file)), "classes.txt")
            out_class_file = open(classes_file, 'w')


        for box in self.box_list:
            class_index, x_center, y_center, w, h = self.bnd_box_to_yolo_line(box, class_list)
            out_file.write("%d %.6f %.6f %.6f %.6f\n" % (class_index, x_center, y_center, w, h))

        for c in class_list:
            out_class_file.write(c+'\n')

        out_class_file.close()
        out_file.close()



class YoloReader:

    def __init__(self, file_path, image, class_list_path=None):
        # shapes type:
        # [labbel, [(x1,y1), (x2,y2), (x3,y3), (x4,y4)], color, color, difficult]
        self.shapes = []
        self.file_path = file_path
        self.classes = []

        if class_list_path is None:
            dir_path = os.path.dirname(os.path.realpath(self.file_path))
            self.class_list_path = os.path.join(dir_path, "classes.txt")
        else:
            self.class_list_path = class_list_path

        # Try to load classes file, but don't crash if it doesn't exist
        try:
            with open(self.class_list_path, 'r') as classes_file:
                # Read all lines and strip them, ignoring empty lines
                self.classes = [line.strip() for line in classes_file.readlines() if line.strip()]
        except FileNotFoundError:
            print(f"Warning: 'classes.txt' not found at '{self.class_list_path}'. YOLO labels may not load correctly.")


        img_size = [image.height(), image.width(),
                    1 if image.isGrayscale() else 3]

        self.img_size = img_size
        self.verified = False
        self.parse_yolo_format()


    def get_shapes(self):
        return self.shapes

    def add_shape(self, label, x_min, y_min, x_max, y_max, difficult):
        points = [(x_min, y_min), (x_max, y_min), (x_max, y_max), (x_min, y_max)]
        self.shapes.append((label, points, None, None, difficult))

    def yolo_line_to_shape(self, class_index, x_center, y_center, w, h):
        # Add a safety check to prevent IndexError
        try:
            class_index_int = int(class_index)
        except ValueError:
            print(f"Warning: Invalid non-integer class index '{class_index}' found in {self.file_path}. Skipping box.")
            return None

        if not (0 <= class_index_int < len(self.classes)):
            print(f"Warning: Class index '{class_index_int}' in {self.file_path} is out of range for the loaded class list (size: {len(self.classes)}). Skipping box.")
            return None

        label = self.classes[class_index_int]

        x_min = max(float(x_center) - float(w) / 2, 0)
        x_max = min(float(x_center) + float(w) / 2, 1)
        y_min = max(float(y_center) - float(h) / 2, 0)
        y_max = min(float(y_center) + float(h) / 2, 1)

        x_min = round(self.img_size[1] * x_min)
        x_max = round(self.img_size[1] * x_max)
        y_min = round(self.img_size[0] * y_min)
        y_max = round(self.img_size[0] * y_max)

        return label, x_min, y_min, x_max, y_max

    def parse_yolo_format(self):
        # Return if the file doesn't exist or the image size is invalid
        if not os.path.exists(self.file_path) or self.img_size[0] == 0 or self.img_size[1] == 0:
            return

        try:
            with open(self.file_path, 'r') as bnd_box_file:
                for bndBox in bnd_box_file:
                    parts = bndBox.strip().split(' ')
                    if len(parts) != 5:
                        continue  # Skip any malformed lines
                        
                    class_index, x_center, y_center, w, h = parts
                    
                    # Check the result of yolo_line_to_shape before unpacking
                    shape_data = self.yolo_line_to_shape(class_index, x_center, y_center, w, h)

                    if shape_data:
                        label, x_min, y_min, x_max, y_max = shape_data
                        # Caveat: difficult flag is discarded when saved as yolo format.
                        self.add_shape(label, x_min, y_min, x_max, y_max, False)
        except Exception as e:
            print(f"Error parsing YOLO file {self.file_path}: {e}")