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
        "description": "Greg Sullivan's electric pianos",
        "license": "[CC 3.0 Unported](http://creativecommons.org/licenses/by/3.0/)"
    },
    {
        "path": "sfzinstruments-jlearman-jrhodes3d",
        "source": "https://github.com/sfzinstruments/jlearman.jRhodes3d",
        "description": "J. Learman Rhodes: 1977 Rhodes Mark I Stage 73 electric piano",
        "license": "[CC0 1.0](http://creativecommons.org/publicdomain/zero/1.0/)"
    },
    {
        "path": "sfzinstruments-splendid-grand-piano",
        "source": "https://github.com/sfzinstruments/SplendidGrandPiano",
        "description": "AKAI Steinway samples with 4 velocity layers",
        "license": "[Public Domain](https://creativecommons.org/share-your-work/public-domain/)"

    },
    {
        "path": "archiveorg-mellotron",
        "source": "https://archive.org/details/mellotron-archive-cd-rom-nki-wav.-7z",
        "description": "Mellotron Samples",
        "license": "[Unknown](https://archive.org/details/mellotron-archive-cd-rom-nki-wav.-7z)"
    },
    {
        "path": "sgossner-vcsl",
        "source": "https://github.com/sgossner/VCSL",
        "description": "The Versilian Community Sample Library",
        "license": "[CC0 1.0](http://creativecommons.org/publicdomain/zero/1.0/)"
    },
    {
        "path": "sfzinstruments-dsmolken-double-bass",
        "source": "https://github.com/sfzinstruments/dsmolken.double-bass",
        "description": "1958 Otto Rubner double bass played and mapped by D. Smolken.",
        "license": "Royalty-free for all commercial and non-commercial use."
    },
    {
        "path": "sonic-pi-samples",
        "source": "https://github.com/sonic-pi-net/sonic-pi",
        "description": "Samples from Sonic Pi software",
        "license": "[CC0 1.0](http://creativecommons.org/publicdomain/zero/1.0/)"
    },
    {
        "path": "freepats-old-piano-fb",
        "source": "https://freepats.zenvoid.org/Piano/honky-tonk-piano.html",
        "description": "Historic piano with an honky-tonk tone",
        "license": "[CC0 1.0](http://creativecommons.org/publicdomain/zero/1.0/)"
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
