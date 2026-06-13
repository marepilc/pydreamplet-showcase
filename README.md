# pydreamplet-showcase

A collection of SVG examples created with
[pydreamplet](https://github.com/marepilc/pydreamplet).

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

Install the project dependencies:

```shell
uv sync
```

## CLI

Run an example by passing its Python file to `dp`:

```shell
uv run dp polar_noise.py
```

The generated SVG is written to a directory named after the script:

```text
output/polar_noise/polar_noise.svg
```

Use `--motive` (or `-m`) to apply one of the predefined color motives:

```shell
uv run dp polar_noise.py --motive light
uv run dp polar_noise.py -m dark
```

When a motive is selected, the example scripts include it in the output
filename:

```text
output/polar_noise/polar_noise_light.svg
output/polar_noise/polar_noise_dark.svg
```

Available motives are `light` and `dark`. Their definitions are stored in
`tools/motives/`.

To display all CLI options:

```shell
uv run dp --help
```

Examples can also be run directly:

```shell
uv run python polar_noise.py
```

Direct execution uses the default pydreamplet theme and still writes the file
under `output/<script-name>/`.

## Adding an Example

1. Copy `template.py` to a descriptively named, lowercase snake-case file in
   the repository root:

   ```shell
   Copy-Item template.py my_example.py
   ```

2. Add the artwork after the `# your art here` marker. Keep the runtime setup
   and output handling from the template:

   ```python
   from pathlib import Path

   import pydreamplet as dp

   from tools.runtime import get_motive, get_output_path

   motive = get_motive()
   theme = dp.Theme(f"tools/motives/{motive}.json") if motive else dp.Theme()

   svg = dp.SVG(1024, 1024)

   # Build the SVG here.

   filename_suffix = f"_{motive}" if motive else ""
   svg.save(get_output_path(f"{Path(__file__).stem}{filename_suffix}.svg"))
   ```

3. Use colors from `theme` where practical so the example works with both
   predefined motives.

4. Generate and inspect all variants:

   ```shell
   uv run dp my_example.py
   uv run dp my_example.py -m light
   uv run dp my_example.py -m dark
   ```

5. Run the linter:

   ```shell
   uv run ruff check .
   ```

Generated files belong under `output/`, which is excluded from version
control. Example source files should remain self-contained and import shared
CLI/runtime behavior only from `tools/`.
