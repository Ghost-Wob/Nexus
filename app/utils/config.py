from pathlib import Path
import yaml


ROOT = Path(__file__).resolve().parents[2]

CONFIG_PATH = ROOT / "config" / "config.yaml"
PROFILE_PATH = ROOT / "config" / "profile.yaml"


def load_yaml(path: Path):
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


config = load_yaml(CONFIG_PATH)
profile = load_yaml(PROFILE_PATH)
