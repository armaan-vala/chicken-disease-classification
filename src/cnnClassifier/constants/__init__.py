from pathlib import Path

# Project root (1 level up from src/)
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent


# Config and params file paths (outside src, directly in root)
CONFIG_FILE_PATH = ROOT_DIR / "config" / "config.yaml"
PARAMS_FILE_PATH = ROOT_DIR / "params.yaml"
