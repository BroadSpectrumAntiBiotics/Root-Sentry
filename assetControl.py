import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

def get_asset_path(subfolder: str, filename: str) -> str:
    return os.path.join(ASSETS_DIR, subfolder, filename)

def load_ascii_art(subfolder: str, filename: str) -> str:

    path = get_asset_path(f"graphics/{subfolder}", filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "[ASCII art missing]"
