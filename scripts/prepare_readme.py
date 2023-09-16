import os


def prepare_readme(path, source, destructive):
    note = f"""
---
<!-- smpldsnds -->

# ⚠ This is just a version of {source} with the following changes:

- Sounds are converted to ogg (opus) and m4a (aac)
- Files are exposed as a github pages
- Some files.json files are added

---
"""

    readme_path = os.path.join(path, "README.md")
    print(f"Preparing README.md... {readme_path}")

    if os.path.exists(readme_path):
        with open(readme_path, "r") as readme_file:
            readme = readme_file.read()

    # is prepared if contains "<!-- smpldsnds -->"
