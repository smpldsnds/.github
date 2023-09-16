import os
import shutil


def setup_shared_files(path, destructive):
    # Create the .github/workflows folder inside the given path if it doesn't exist
    github_workflow_path = os.path.join(path, '.github', 'workflows')
    if destructive:
        os.makedirs(github_workflow_path, exist_ok=True)

    if destructive:
        shutil.copy('./files/deploy.yml', github_workflow_path)
        shutil.copy('./files/.gitignore', path)

    print(f"Files successfully copied")
