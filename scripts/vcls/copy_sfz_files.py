
import os
import shutil

# VSCL .sfz files were in the sfz branch. This script copies them to the smpldsnds repo


def copy_missing_files(input_dir, output_dir, destructive):
    print(f"Copying missing .sfz files from {input_dir} to {output_dir}...")
    # Walk through the directory structure of the input directory
    total = 0
    for dirpath, dirnames, filenames in os.walk(input_dir):

        for file in filenames:
            if file.endswith(".sfz"):
                print(f"Found {file} in {dirpath}")
                # Create the relative path
                relative_path = os.path.relpath(dirpath, input_dir)
                dest_path = os.path.join(output_dir, relative_path)
                # Destination file path
                dest_file_path = os.path.join(dest_path, file)

                print(f"Copying {file} to {dest_file_path}")

                # Check if the destination folder exists
                if not os.path.exists(dest_path):
                    raise Exception(f"Folder '{dest_path}' doesn't exist!")

                total += 1

                # Check if the file doesn't already exist in the output directory
                if destructive:
                    shutil.copy2(os.path.join(dirpath, file), dest_file_path)

    print(f"Total files copied: {total}")


if __name__ == "__main__":
    input_folder = "../VCSL"
    output_folder = "../sgossner-vcsl"

    try:
        copy_missing_files(input_folder, output_folder, destructive=True)
        print("All missing .sfz files copied successfully!")
    except Exception as e:
        print(f"Error: {e}")
