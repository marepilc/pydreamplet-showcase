import os
import runpy
from enum import StrEnum
from pathlib import Path

import typer

app = typer.Typer(add_completion=False)


class Motive(StrEnum):
    LIGHT = "light"
    DARK = "dark"


@app.command()
def main(
    script: Path = typer.Argument(..., help="Python showcase script to run."),
    motive: Motive | None = typer.Option(None, "--motive", "-m"),
) -> None:
    script = script.resolve()
    if not script.is_file():
        raise typer.BadParameter(f"Script does not exist: {script}")

    os.environ["PYDREAMPLET_SCRIPT_STEM"] = script.stem
    if motive is None:
        os.environ.pop("PYDREAMPLET_MOTIVE", None)
    else:
        os.environ["PYDREAMPLET_MOTIVE"] = str(motive)

    runpy.run_path(str(script), run_name="__main__")
