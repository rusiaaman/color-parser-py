# Color Parser Python

Python bindings for CSS color parser using PyO3. Parse and convert colors between different formats.

## Prerequisites

- Python 3.7+
- Rust toolchain (install from https://rustup.rs/)

## Installation

```bash
# Install Rust toolchain (if not already installed)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install from GitHub
pip install git+https://github.com/rusiaaman/color-parser-py

# Or install in development mode
git clone https://github.com/rusiaaman/color-parser-py
cd color-parser-py
pip install maturin
maturin develop
```

## Usage

```python
from color_parser_py import ColorParser

# Parse a color
color = ColorParser("#ff0000")

# Get different representations
print(color.rgba_255)     # [255, 0, 0, 255]
print(color.rgba_float)   # [1.0, 0.0, 0.0, 1.0]
print(color.hex)          # "#ff0000"
print(color.rgb_string)   # "rgb(255,0,0)"

# Parse with alpha
color_with_alpha = ColorParser("rgba(255, 0, 0, 0.5)")
print(color_with_alpha.rgba_255)  # [255, 0, 0, 128]
```

## Supported Color Formats

- Hex colors: `#ff0000`, `ff0000`, `#f00`
- RGB/RGBA: `rgb(255, 0, 0)`, `rgba(255, 0, 0, 0.5)`
- HSL/HSLA: `hsl(0, 100%, 50%)`, `hsla(0, 100%, 50%, 0.5)`
- Named colors: `red`, `tomato`, etc.
- Transparent: `transparent`
