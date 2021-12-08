import os
import platform
from glob import glob
if platform.system() =="Windows":
    labels_dir = "C:/tmp/labels"
else:
    labels_dir = "/tmp/labels"
os.makedirs(labels_dir, exist_ok=True)
labels = {
    "label1": ["1image.JPG", "2.jpeg", "2.json", "1image.json", "3.jpg"],
    "label2": ["1.jpg", "1.json", "2.json", "3.json"],
    "label3": ["15.png", "15.json", "16.json", "16.jpg", "1.PNG", "1.JSON"],
    "label4": ["1.png", "1.txt", "2.txt", ],
}
for label in labels:
    label_path = os.path.join(labels_dir, label)
    os.makedirs(label_path, exist_ok=True)
    for item in labels[label]:
        open(os.path.join(label_path, item), 'a').close()
    print(f"{label_path} {os.listdir(label_path)}")
open(os.path.join(labels_dir, "test.txt"), 'a').close()
