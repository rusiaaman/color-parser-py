from color_parser_py import ColorParser

def test_color(color_str):
    print(f"\nTesting color: {color_str}")
    try:
        color = ColorParser(color_str)
        print(f"RGBA (0-255): {color.rgba_255}")
        print(f"RGBA (0-1): {color.rgba_float}")
        print(f"Hex: {color.hex}")
        print(f"RGB string: {color.rgb_string}")
    except ValueError as e:
        print(f"Error: {e}")

# Test various color formats
test_colors = [
    "#ff0000",              # Regular hex
    "#f00",                 # Short hex
    "#ff000080",           # Hex with alpha
    "rgb(255, 0, 0)",      # RGB
    "rgba(255, 0, 0, 0.5)", # RGBA
    "hsl(0, 100%, 50%)",   # HSL
    "hsla(0, 100%, 50%, 0.5)", # HSLA
    "red",                 # Named color
    "tomato",             # Another named color
    "transparent",        # Special value
    "invalid-color",      # Invalid color
]

# Test valid/invalid colors
print("Testing color validation:")
for color in ["#ff0000", "rgb(255,0,0)", "invalid-color"]:
    print(f"Is '{color}' valid? {ColorParser.is_valid(color)}")

# Test all color formats
print("\nTesting color parsing:")
for color in test_colors:
    test_color(color)