import os, shutil
from sklearn.model_selection import train_test_split

images_dir = r'F:\project\plate\results'
labels_dir = r'F:\project\plate\data\data3'

train_images_dir = r'F:\project\plate\makedataset\data3\train\images'
val_images_dir = r'F:\project\plate\makedataset\data3\val\images'
train_labels_dir = r'F:\project\plate\makedataset\data3\train\labels'
val_labels_dir = r'F:\project\plate\makedataset\data3\val\labels'


image_files = [f for f in os.listdir(images_dir) if f.endswith('.png')]
label_files = [f.replace('.png', '.txt') for f in image_files]


train_images, val_images, train_labels, val_labels = train_test_split(
    image_files, label_files, test_size=0.1, random_state=42
)


for img_file, lbl_file in zip(train_images, train_labels):
    shutil.copy(os.path.join(images_dir, img_file), os.path.join(train_images_dir, img_file))
    shutil.copy(os.path.join(labels_dir, lbl_file), os.path.join(train_labels_dir, lbl_file))

for img_file, lbl_file in zip(val_images, val_labels):
    shutil.copy(os.path.join(images_dir, img_file), os.path.join(val_images_dir, img_file))
    shutil.copy(os.path.join(labels_dir, lbl_file), os.path.join(val_labels_dir, lbl_file))

print("Success")