from pathlib import Path
import shutil
import sys

def parse_args():
    source_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    destination_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not source_dir or not source_dir.exists():
        print("Error: Specify an existing source directory.")
        sys.exit(1)

    return source_dir, destination_dir

def process_directory(source: Path, destination: Path):
    for item in source.iterdir():
        if item.is_dir():
            process_directory(item, destination)
        else:
            copy_and_sort_file(item, destination)

def copy_and_sort_file(file_path: Path, destination: Path):
    try:
        ext = file_path.suffix[1:].lower() or "unknown"
        target_dir = destination / ext
        target_dir.mkdir(parents=True, exist_ok=True)

        shutil.copy2(file_path, target_dir)
        print(f"Copied: {file_path} -> {target_dir}")
    except Exception as e:
        print(f"Error while copying {file_path}: {e}")

if __name__ == "__main__":
    source_dir, destination_dir = parse_args()
    destination_dir.mkdir(parents=True, exist_ok=True)
    process_directory(source_dir, destination_dir)
    print("Copying success :)")