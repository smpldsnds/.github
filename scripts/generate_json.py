import json
import os


def create_json_files(directory, repo, destructive):
    instruments = []
    if "file_extension" in repo:
        file_extension = repo["file_extension"]
    else:
        file_extension = ".ogg"
    create_index_json_files(directory, instruments, file_extension, destructive)

    instruments = [x.replace(directory + "/", "") for x in instruments]
    instruments_path = os.path.join(directory, "instruments.json")
    if destructive:
        with open(instruments_path, "w") as json_file:
            json.dump(instruments, json_file)
    print(f"index.json created: {instruments_path}")

    sfz_files = find_all_sfz_files(directory)
    sfz_files = [x.replace(directory + "/", "").replace(".sfz", "") for x in sfz_files]
    sfz_files_path = os.path.join(directory, "sfz_files.json")
    if destructive:
        with open(sfz_files_path, "w") as json_file:
            json.dump(sfz_files, json_file)


def find_all_sfz_files(directory):
    sfz_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".sfz"):
                sfz_files.append(os.path.join(root, file))
    return sfz_files


def create_index_json_files(directory, instruments, file_extension, destructive):
    print(f"Creating index.json files in {directory}...")
    ogg_files = [
        os.path.splitext(file)[0]
        for file in os.listdir(directory)
        if file.endswith(file_extension)
    ]

    if ogg_files:
        instruments_path = os.path.join(directory, "files.json")
        instruments.append(directory)
        if destructive:
            # Save the list of filenames to an index.json file inside the directory
            with open(instruments_path, "w") as json_file:
                json.dump(ogg_files, json_file)
        print(f"files.json created: {instruments_path}")

    # Check and process nested subdirectories
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path) and not item.startswith("."):
            create_index_json_files(item_path, instruments, file_extension, destructive)
