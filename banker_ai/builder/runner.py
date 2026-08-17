from pathlib import Path
import subprocess


def project_path(name):
    return Path("projects") / name


def build(name):
    root = project_path(name)

    if not root.exists():
        raise FileNotFoundError(f"Project not found: {name}")

    print(f"Building {name}...")

    subprocess.run(
        ["python", "src/main.py"],
        cwd=root,
        check=True
    )

    print("Build completed.")


def test(name):
    root = project_path(name)

    if not root.exists():
        raise FileNotFoundError(f"Project not found: {name}")

    subprocess.run(
        ["python", "-m", "unittest", "discover", "-s", "tests"],
        cwd=root,
        check=True
    )


def run(name):
    root = project_path(name)

    if not root.exists():
        raise FileNotFoundError(f"Project not found: {name}")

    subprocess.run(
        ["python", "src/main.py"],
        cwd=root,
        check=True
    )
