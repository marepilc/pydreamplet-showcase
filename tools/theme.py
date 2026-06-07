import json
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path


class Motive(StrEnum):
    LIGHT = "light"
    DARK = "dark"


@dataclass
class Color:
    inherit: str
    current: str
    transparent: str
    black: str
    white: str
    slate: str
    gray: str
    zinc: str
    neutral: str
    stone: str
    red: str
    orange: str
    amber: str
    yellow: str
    lime: str
    green: str
    emerald: str
    teal: str
    cyan: str
    sky: str
    blue: str
    indigo: str
    violet: str
    purple: str
    fuchsia: str
    pink: str
    rose: str
    ink: str
    surface: str


@dataclass(init=False)
class Theme(Color):
    motive: Motive
    font_family: str
    colors: Color

    def __init__(self, motive: Motive | str, font_family: str = "sans-serif"):
        motive = Motive(motive)
        colors_path = Path(__file__).parent / "motives" / f"{motive.value}.json"
        color_values = json.loads(colors_path.read_text())
        colors = Color(**color_values)

        super().__init__(**color_values)
        self.motive = motive
        self.font_family = font_family
        self.colors = colors
