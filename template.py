from pathlib import Path

import pydreamplet as dp

from tools.runtime import get_motive, get_output_path

motive = get_motive()
theme = dp.Theme(f"tools/motives/{motive}.json") if motive else dp.Theme()

svg = dp.SVG(1024, 1024)

#
# your art here
#

filename_suffix = f"_{motive}" if motive else ""
svg.save(get_output_path(f"{Path(__file__).stem}{filename_suffix}.svg"))
