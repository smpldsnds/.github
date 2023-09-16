import os

README_HEADER = """

## A collection of open source or public domain samples deployed using github pages

"""

README_FOOTER = """

Each repository is resulting from an automated process to:

- Convert audio files to .ogg (opus) and .m4a (aac) formats.
- Create a files.json with the list of files for each folder
- Create a instruments.json with the list of folders with samples

No other changes are made to the original samples or packages.

Kudos for all _samplerists_ and sample creators out there! 🙌

If you know a sample bundle with an open source license and want to include here, please open an [issue](https://github.com/smpldsnds/.github/issues) or a [pull request](https://github.com/smpldsnds/.github/pulls)
"""


def prepare_profile_readme(repositories, destructive):
    readme = README_HEADER

    repositories = sorted(repositories, key=lambda x: x["description"])

    for repo in repositories:
        name = repo["path"]
        repo_url = f"https://github.com/smpldsnds/{name}"
        description = repo["description"]
        source = repo["source"]
        license = repo["license"]
        readme += f"- [`{name}`]({repo_url}): {description}. License: {license}. ([source]({source}))\n"

    output_path = "./profile/README.md"
    readme += README_FOOTER

    # check if output_path exists
    if os.path.exists(output_path):
        if destructive:
            with open(output_path, "w") as readme_file:
                readme_file.write(readme)
        print(f"Profile README.md written: {output_path}")
