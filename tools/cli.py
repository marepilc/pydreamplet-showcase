import os
import runpy
from enum import StrEnum
from pathlib import Path

import typer

app = typer.Typer(add_completion=False)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"


class Motive(StrEnum):
    LIGHT = "light"
    DARK = "dark"


def resolve_script(script: Path) -> Path:
    candidates = [script]
    if not script.is_absolute():
        candidates.append(SCRIPTS_DIR / script)

    if script.suffix == "":
        candidates.extend(candidate.with_suffix(".py") for candidate in candidates.copy())

    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved.is_file():
            return resolved

    raise typer.BadParameter(f"Script does not exist: {script}")


@app.command()
def main(
    script: Path = typer.Argument(
        ...,
        help="Showcase script path or a script name from the scripts directory.",
    ),
    motive: Motive | None = typer.Option(None, "--motive", "-m"),
) -> None:
    script = resolve_script(script)

    os.environ["PYDREAMPLET_SCRIPT_STEM"] = script.stem
    if motive is None:
        os.environ.pop("PYDREAMPLET_MOTIVE", None)
    else:
        os.environ["PYDREAMPLET_MOTIVE"] = str(motive)

    runpy.run_path(str(script), run_name="__main__")
