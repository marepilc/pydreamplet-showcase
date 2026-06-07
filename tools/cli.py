import os
import runpy
from pathlib import Path

import typer

from tools.theme import Motive

app = typer.Typer(add_completion=False)


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
        os.environ["PYDREAMPLET_MOTIVE"] = motive.value

    runpy.run_path(str(script), run_name="__main__")
