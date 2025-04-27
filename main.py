import subprocess
from pathlib import Path

# Configuration
PHOTO_DIR = Path("./photos")
NUM_PHOTOS = 3
CAMERA_DEVICE = "/dev/video0"

def take_photos():
    """Takes multiple photos using the webcam."""
    for i in range(1, NUM_PHOTOS + 1):
        photo_path = PHOTO_DIR / f"photo{i:02}.png"
        try:
            subprocess.run(
                ['fswebcam', '-d', CAMERA_DEVICE, '--no-banner', str(photo_path)],
                check=True
            )
            print(f"Captured {photo_path}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to capture {photo_path}: {e}")

def make_directory():
    """Creates the photo directory if it does not exist."""
    try:
        PHOTO_DIR.mkdir(parents=True, exist_ok=True)
        print(f"Directory '{PHOTO_DIR}' is ready.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{PHOTO_DIR}'.")
    except Exception as e:
        print(f"An error occurred while creating directory: {e}")

def create_vertical_strip():
    """Combines all captured photos into a single vertical strip."""
    output_path = PHOTO_DIR / "vertical_strip.png"
    input_photos = [PHOTO_DIR / f"photo{i:02}.png" for i in range(1, NUM_PHOTOS + 1)]
    try:
        subprocess.run(
            ['convert', *map(str, input_photos), '-append', str(output_path)],
        )
        print(f"Vertical strip created at {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create vertical strip: {e}")

if __name__ == '__main__':
    make_directory()
    take_photos()
    create_vertical_strip()
