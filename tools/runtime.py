import os
import sys
from pathlib import Path


def get_motive() -> str | None:
    return os.environ.get("PYDREAMPLET_MOTIVE")


def get_output_path(filename: str) -> str:
    script_stem = os.environ.get("PYDREAMPLET_SCRIPT_STEM")
    if script_stem is None:
        script_stem = Path(sys.argv[0]).stem

    output_dir = Path("output") / script_stem
    output_dir.mkdir(parents=True, exist_ok=True)
    return str(output_dir / filename)
