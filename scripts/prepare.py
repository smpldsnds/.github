import glob
import json
import os
import shutil
import sys
from datetime import datetime

from convert_audio_files import convert_audio_files
from generate_html import generate_html_index
from generate_json import create_index_json_files

REPOSITORIES = [
    {"path": "sfzinstruments-greg-sullivan-e-pianos",
        "source": "https://github.com/sfzinstruments/GregSullivan.E-Pianos"},
    {"path": "sfzinstruments-jlearman-jrhodes3d", "source": ""},
    {"path": "sfzinstruments-splendid-grand-piano", "source": ""},
    {
        "path": "archiveorg-mellotron",
        "source": "https://archive.org/details/mellotron-archive-cd-rom-nki-wav.-7z"
    },
    {
        "path": "sgossner-vcsl",
        "source": "https://github.com/sgossner/VCSL"
    }
]


def setup_shared_files(path, destructive):
    # Create the .github/workflows folder inside the given path if it doesn't exist
    github_workflow_path = os.path.join(path, '.github', 'workflows')
    if destructive:
        os.makedirs(github_workflow_path, exist_ok=True)

    if destructive:
        shutil.copy('./files/deploy.yml', github_workflow_path)
        shutil.copy('./files/.gitignore', path)

    print(f"Files successfully copied")


def process_all_repositories(destructive=False):
    for repo in REPOSITORIES:
        path = f"../{repo['path']}"
        print(f"Processing {repo['path']}...")
        setup_shared_files(path, destructive)
        convert_audio_files(path, destructive)
        create_index_json_files(path, destructive)
        generate_html_index(path, destructive)


def main():
    # Get the current timestamp in seconds since the Unix epoch
    current_timestamp = int(datetime.utcnow().timestamp())

    # Parse the provided timestamp if exists
    provided_timestamp = int(sys.argv[2]) if len(sys.argv) == 3 else 0

    # Check if the provided timestamp is within 10 seconds from the current time
    time_difference = abs(current_timestamp - provided_timestamp)

    destructive = time_difference <= 10

    print(f"Destructive: {destructive}")
    process_all_repositories(destructive)
    if not destructive:
        print(f"Run this script again with the --destructive flag to perform actions:")
        print(f"python scripts/prepare.py --destructive {current_timestamp}")
        sys.stdout.write("\033[1;31mNo file was written\033")


if __name__ == "__main__":
    main()
