import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def get_motive() -> str | None:
    return os.environ.get("PYDREAMPLET_MOTIVE")


def get_motive_path(motive: str) -> str:
    return str(PROJECT_ROOT / "tools" / "motives" / f"{motive}.json")


def get_data_path(script_name: str, filename: str) -> Path:
    return PROJECT_ROOT / "data" / script_name / filename


def get_output_path(filename: str) -> str:
    script_stem = os.environ.get("PYDREAMPLET_SCRIPT_STEM")
    if script_stem is None:
        script_stem = Path(sys.argv[0]).stem

    output_dir = PROJECT_ROOT / "output" / script_stem
    output_dir.mkdir(parents=True, exist_ok=True)
    return str(output_dir / filename)
