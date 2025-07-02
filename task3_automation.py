import os
import shutil

# .jpg files folder
source_folder = "images"

# Path to the folder want to move the .jpg files
destination = "destination"

if not os.path.exists(destination):
    os.makedirs(destination)

# Loop through all files in the source folder
for filename in os.listdir(source_folder):
    # Check if the file ends with .jpg 
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination, filename)
        
        # Move the file
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")

print("All .jpg files have been moved successfully!")