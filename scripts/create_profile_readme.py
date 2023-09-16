import os

README_HEADER = """

## A collection of open source or public domain samples deployed using github pages

Repositories:

"""

README_FOOTER = """
"""


def prepare_profile_readme(repositories, destructive):
    readme = README_HEADER

    repositories = sorted(repositories, key=lambda x: x["description"])

    for repo in repositories:
        name = repo["path"]
        repo_url = f"https://github.com/smpldsnds/{name}"
        description = repo["description"]
        source = repo["source"]
        readme += f"- `[{name}]({repo_url})`: {description}. ([source]({source}))\n"

        output_path = "./profile/README.md"

        # check if output_path exists
        if os.path.exists(output_path):
            if destructive:
                with open(output_path, "w") as readme_file:
                    readme_file.write(readme)
            print(f"Profile README.md written: {output_path}")
