from pathlib import Path

import pydreamplet as dp
from pydreamplet.noise import SimplexNoise2D

from tools.runtime import get_motive, get_output_path

motive = get_motive()
theme = dp.Theme(f"tools/motives/{motive}.json") if motive else dp.Theme()

noise = SimplexNoise2D()
svg = dp.SVG(1024, 1024)
margin = 48
g = dp.G(pos=(svg.w / 2, svg.h / 2))
svg.append(g)

shapes_count = 8
line = dp.LineGenerator(curve="linear")
offset = dp.Vector(1, 1)
palette = dp.generate_colors("#db45f9", n=shapes_count)
min_radius = 20
max_radius = svg.w / 2 - margin
radius_step = (max_radius - min_radius) / (shapes_count - 1)

for shape_index, color in enumerate(palette):
    base_radius = max_radius - shape_index * radius_step
    points: list[tuple[float, float]] = []
    angle = 0
    while angle < 360:
        direction = dp.Vector.from_polar(angle)
        radius = base_radius + noise.noise(
            direction.x, direction.y, frequency=1.5, amplitude=50
        )
        points.append((direction * radius + offset).xy)
        angle += 0.1
    g.append(dp.Path(line(points), opacity=0.5, stroke=theme.ink, fill=color))

filename_suffix = f"_{motive}" if motive else ""
svg.save(get_output_path(f"{Path(__file__).stem}{filename_suffix}.svg"))
