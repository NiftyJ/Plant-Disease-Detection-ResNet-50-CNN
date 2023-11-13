import os

# Constructing a file path
directory = 'C:/Users/leona/Plant-Disease-Identification-using-CNN/archive_5/PlantVillage_resize_224/PlantVillage_resize_224/s1'
file_name = '1.jpg'
file_path = os.path.join(directory, file_name)

# Check if the file exists
if os.path.exists(file_path):
    print(f"The file {file_name}  exists in the directory {directory}.")
    # Your code here
else:
    print(f"The file {file_name} does not exist in the directory {directory}.")
