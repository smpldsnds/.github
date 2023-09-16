import sys
from datetime import datetime

from convert_audio_files import convert_audio_files
from create_profile_readme import prepare_profile_readme
from generate_html import generate_html_index
from generate_json import create_json_files
from setup_shared_files import setup_shared_files

REPOSITORIES = [
    {
        "path": "sfzinstruments-greg-sullivan-e-pianos",
        "source": "https://github.com/sfzinstruments/GregSullivan.E-Pianos",
        "description": "Greg Sullivan's electric pianos"
    },
    {
        "path": "sfzinstruments-jlearman-jrhodes3d",
        "source": "https://github.com/sfzinstruments/jlearman.jRhodes3d",
        "description": "J. Learman Rhodes: 1977 Rhodes Mark I Stage 73 electric piano"
    },
    {
        "path": "sfzinstruments-splendid-grand-piano",
        "source": "https://github.com/sfzinstruments/SplendidGrandPiano",
        "description": "AKAI Steinway samples with 4 velocity layers"

    },
    {
        "path": "archiveorg-mellotron",
        "source": "https://archive.org/details/mellotron-archive-cd-rom-nki-wav.-7z",
        "description": "Mellotron Samples"
    },
    {
        "path": "sgossner-vcsl",
        "source": "https://github.com/sgossner/VCSL",
        "description": "The Versilian Community Sample Library"
    },
    {
        "path": "freepats-old-piano-fb",
        "source": "https://freepats.zenvoid.org/Piano/honky-tonk-piano.html",
        "description": "Historic piano with an honky-tonk tone"
    }
]


# All steps should be idempotent
def run_steps(path, destructive=False):
    print(f"Processing {path}...")
    setup_shared_files(path, destructive)
    convert_audio_files(path, destructive)
    create_json_files(path, destructive)
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
    for repo in REPOSITORIES:
        path = f"../{repo['path']}"
        run_steps(path, destructive)
        prepare_profile_readme(REPOSITORIES, destructive)

    if not destructive:
        print(f"Run this script again with the --destructive flag to perform actions:")
        print(f"python scripts/prepare.py --destructive {current_timestamp}")
        sys.stdout.write("\033[1;31mNo file was written\033")


if __name__ == "__main__":
    main()
