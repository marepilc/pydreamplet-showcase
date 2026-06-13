import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def get_example_name() -> str:
    example_name = os.environ.get("PYDREAMPLET_EXAMPLE_NAME")
    if example_name is not None:
        return example_name

    script_path = Path(sys.argv[0])
    return script_path.parent.name if script_path.stem == "main" else script_path.stem


def get_motive() -> str | None:
    return os.environ.get("PYDREAMPLET_MOTIVE")


def get_motive_path(motive: str) -> str:
    return str(PROJECT_ROOT / "tools" / "motives" / f"{motive}.json")


def get_data_path(script_name: str, filename: str) -> Path:
    return PROJECT_ROOT / "data" / script_name / filename


def get_output_path(filename: str) -> str:
    output_dir = PROJECT_ROOT / "output" / get_example_name()
    output_dir.mkdir(parents=True, exist_ok=True)
    return str(output_dir / filename)
