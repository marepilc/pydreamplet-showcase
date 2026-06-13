# pydreamplet-showcase

A collection of SVG examples created with
[pydreamplet](https://github.com/marepilc/pydreamplet).

## Project Layout

```text
scripts/                  Showcase scripts
data/<script-name>/       Data used by a specific showcase
tools/motives/            Light and dark color motives
tools/                    Shared CLI and runtime helpers
output/<script-name>/     Generated SVG files
```

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

Install the project dependencies:

```shell
uv sync
```

## CLI

Run an example by passing its name to `dp`:

```shell
uv run dp polar_noise
```

The CLI resolves short names from `scripts/`. An explicit path works too:

```shell
uv run dp scripts/polar_noise.py
```

The generated SVG is written to a directory named after the script:

```text
output/polar_noise/polar_noise.svg
```

Use `--motive` (or `-m`) to apply one of the predefined color motives:

```shell
uv run dp polar_noise --motive light
uv run dp polar_noise -m dark
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
uv run python scripts/polar_noise.py
```

Direct execution uses the default pydreamplet theme and still writes the file
under `output/<script-name>/`.

## Adding an Example

1. Copy `scripts/template.py` to a descriptively named, lowercase snake-case
   file in the `scripts` directory:

   ```shell
   Copy-Item scripts/template.py scripts/my_example.py
   ```

2. Add the artwork after the `# your art here` marker. Keep the runtime setup
   and output handling from the template:

   ```python
   from pathlib import Path

   import pydreamplet as dp

   from tools.runtime import get_motive, get_motive_path, get_output_path

   motive = get_motive()
   theme = dp.Theme(get_motive_path(motive)) if motive else dp.Theme()

   svg = dp.SVG(1024, 1024)

   # Build the SVG here.

   filename_suffix = f"_{motive}" if motive else ""
   svg.save(get_output_path(f"{Path(__file__).stem}{filename_suffix}.svg"))
   ```

3. If the example needs input data, store it under a directory matching the
   script stem:

   ```text
   data/my_example/
   ```

   Resolve data files with the shared runtime helper:

   ```python
   from tools.runtime import get_data_path

   data_path = get_data_path(Path(__file__).stem, "input.json")
   ```

4. Use colors from `theme` where practical so the example works with both
   predefined motives.

5. Generate and inspect all variants:

   ```shell
   uv run dp my_example
   uv run dp my_example -m light
   uv run dp my_example -m dark
   ```

6. Run the linter:

   ```shell
   uv run ruff check .
   ```

Generated files belong under `output/`, which is excluded from version
control. Keep example-specific data under `data/<script-name>/` and shared
CLI/runtime behavior under `tools/`.
