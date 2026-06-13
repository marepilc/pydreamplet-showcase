from pathlib import Path

import pydreamplet as dp

from tools.runtime import get_motive, get_motive_path, get_output_path

motive = get_motive()
theme = dp.Theme(get_motive_path(motive)) if motive else dp.Theme()

svg = dp.SVG(1024, 1024)

#
# your art here
#

filename_suffix = f"_{motive}" if motive else ""
svg.save(get_output_path(f"{Path(__file__).stem}{filename_suffix}.svg"))
