import json
import os


def create_json_files(directory, destructive):
    instruments = []
    create_index_json_files(directory, instruments, destructive)

    instruments = [x.replace(directory + "/", "") for x in instruments]
    output_path = os.path.join(directory, 'instruments.json')
    if destructive:
        with open(output_path, 'w') as json_file:
            json.dump(instruments, json_file)

    print(f"index.json created: {output_path}")


def create_index_json_files(directory, instruments, destructive):
    print(f"Creating index.json files in {directory}...")
    ogg_files = [os.path.splitext(file)[0] for file in os.listdir(
        directory) if file.endswith('.ogg')]

    if ogg_files:
        output_path = os.path.join(directory, 'files.json')
        instruments.append(directory)
        if destructive:
            # Save the list of filenames to an index.json file inside the directory
            with open(output_path, 'w') as json_file:
                json.dump(ogg_files, json_file)
        print(f"files.json created: {output_path}")

    # Check and process nested subdirectories
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path) and not item.startswith('.'):
            create_index_json_files(item_path, instruments, destructive)
