import pytest
from color_parser_py import ColorParser
from typing import List


def test_hex_color() -> None:
    color = ColorParser("#ff0000")
    assert color.rgba_255 == (255, 0, 0, 255)
    assert color.hex == "#ff0000"
    assert color.rgb_string == "rgb(255,0,0)"
    assert color.rgba_float == [1.0, 0.0, 0.0, 1.0]


def test_short_hex_color() -> None:
    color = ColorParser("#f00")
    assert color.rgba_255 == (255, 0, 0, 255)
    assert color.hex == "#ff0000"


def test_hex_with_alpha() -> None:
    color = ColorParser("#ff000080")
    assert color.rgba_255 == (255, 0, 0, 128)
    assert color.hex == "#ff000080"
    assert "0.5" in color.rgb_string  # Check alpha is around 0.5


def test_rgb_function() -> None:
    cases = [
        "rgb(255, 0, 0)",
        "rgb(255,0,0)",
        "rgb(255 0 0)",
        "rgb(100%, 0%, 0%)",
    ]
    for case in cases:
        color = ColorParser(case)
        assert color.rgba_255 == (255, 0, 0, 255), f"Failed for {case}"


def test_rgba_function() -> None:
    cases = [
        ("rgba(255, 0, 0, 0.5)", (255, 0, 0, 128)),
        ("rgba(255 0 0 / 50%)", (255, 0, 0, 128)),
    ]
    for case, expected in cases:
        color = ColorParser(case)
        assert color.rgba_255 == expected, f"Failed for {case}"


def test_hsl_function() -> None:
    cases = [
        "hsl(0, 100%, 50%)",
        "hsl(0 100% 50%)",
        "hsl(0deg 100% 50%)",
    ]
    for case in cases:
        color = ColorParser(case)
        assert color.rgba_255 == (255, 0, 0, 255), f"Failed for {case}"


def test_hsla_function() -> None:
    color = ColorParser("hsla(0, 100%, 50%, 0.5)")
    assert color.rgba_255 == (255, 0, 0, 128)


def test_named_colors() -> None:
    cases = [
        ("red", (255, 0, 0, 255)),
        ("blue", (0, 0, 255, 255)),
        ("transparent", (0, 0, 0, 0)),
    ]
    for name, expected in cases:
        color = ColorParser(name)
        assert color.rgba_255 == expected, f"Failed for {name}"


def test_invalid_colors() -> None:
    invalid_cases = [
        "not-a-color",
        "rgb(300, 0, 0)",  # Out of range
        "rgba(255, 0, 0, 2)",  # Invalid alpha
        "#fz0000",  # Invalid hex
    ]
    for case in invalid_cases:
        with pytest.raises(ValueError):
            ColorParser(case)


def test_validation_method() -> None:
    assert ColorParser.is_valid("#ff0000") is True
    assert ColorParser.is_valid("rgb(255, 0, 0)") is True
    assert ColorParser.is_valid("not-a-color") is False


def test_color_properties() -> None:
    color = ColorParser("rgb(128, 64, 32)")
    rgba_255 = color.rgba_255
    rgba_float = color.rgba_float
    
    # Test tuple unpacking for rgba_255
    r, g, b, a = rgba_255
    assert isinstance(r, int)
    assert 0 <= r <= 255
    
    # Test float values are normalized
    assert all(0 <= x <= 1 for x in rgba_float)
    
    # Convert back to ints and compare
    converted_ints = tuple(int(x * 255) for x in rgba_float[:3])
    assert converted_ints == (128, 64, 32)