# Color Parser Python

Python bindings for CSS color parser using PyO3. Parse and convert colors between different formats.

[![PyPI version](https://badge.fury.io/py/color-parser-py.svg)](https://badge.fury.io/py/color-parser-py)
[![Python Versions](https://img.shields.io/pypi/pyversions/color-parser-py.svg)](https://pypi.org/project/color-parser-py/)

## Installation

### From PyPI (Recommended)
```bash
pip install color_parser_py
```

Pre-built wheels are available for:
- Windows (x86, x64)
- macOS (Intel, Apple Silicon)
- Linux (x86, x86_64, aarch64, armv7, etc.)
- Python 3.7 through 3.13

No Rust toolchain is required for installation from PyPI.

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

# Validate colors without raising exceptions
is_valid = ColorParser.is_valid("#ff0000")  # True
is_valid = ColorParser.is_valid("not-a-color")  # False
```

## Error Handling

The `ColorParser` class validates input and raises `ValueError` for invalid colors:

```python
try:
    color = ColorParser("invalid-color")
except ValueError as e:
    print(f"Error: {e}")  # Error: Failed to parse color: ...
```

You can perform validation without raising exceptions using the static method:

```python
if ColorParser.is_valid(user_input):
    color = ColorParser(user_input)
    # Process the color...
else:
    # Handle invalid color input...
```

## Supported Color Formats

- Hex colors: `#ff0000`, `ff0000`, `#f00`
- RGB/RGBA: `rgb(255, 0, 0)`, `rgba(255, 0, 0, 0.5)`
- HSL/HSLA: `hsl(0, 100%, 50%)`, `hsla(0, 100%, 50%, 0.5)`
- Named colors: `red`, `tomato`, etc.
- Transparent: `transparent`

## Features

- Fast color parsing powered by Rust
- Comprehensive support for CSS color formats
- Type-safe Python interface with proper type hints
- Consistent and predictable behavior across platforms
- Zero Python dependencies - all functionality is implemented in Rust

## Version

Current version: 0.1.5

## Project Structure

This project uses:
- [PyO3](https://github.com/PyO3/pyo3) for Rust-Python bindings
- [Maturin](https://github.com/PyO3/maturin) for building and publishing
- [csscolorparser](https://github.com/mazznoer/csscolorparser-rs) for the underlying color parsing

## Development

### From Source
If you want to install from source or contribute to development:

```bash
# Install Rust toolchain (if not already installed)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Clone the repository
git clone https://github.com/rusiaaman/color-parser-py
cd color-parser-py

# Set up development environment
python -m pip install maturin pytest mypy ruff

# Build and install in development mode
maturin develop

# Run tests
pytest tests/
```

### Running Tests
```bash
pytest tests/
```

### Type Checking
```bash
mypy python/color_parser_py
```

### Linting
```bash
ruff check .
```

### Building Wheels
```bash
maturin build --release
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request