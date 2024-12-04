from typing import List, Tuple, ClassVar, overload

class ColorParser:
    """Parse and manipulate CSS color strings."""
    
    def __init__(self, color_str: str) -> None:
        """
        Create a new ColorParser instance.
        
        Args:
            color_str: A string representing a CSS color in any valid format
                (hex, rgb, rgba, hsl, hsla, or named color)
        
        Raises:
            ValueError: If the color string is invalid or cannot be parsed
        """
        ...

    @property
    def rgba_255(self) -> tuple[int, int, int, int]:
        """
        Get RGBA values in 0-255 range.
        
        Returns:
            A tuple of 4 integers (r, g, b, a) where:
                r, g, b are in range 0-255
                a (alpha) is in range 0-255
        """
        ...

    @property
    def rgba_float(self) -> List[float]:
        """
        Get RGBA values in 0-1 range.
        
        Returns:
            A list of 4 floats [r, g, b, a] where all values are in range 0-1
        """
        ...

    @property
    def hex(self) -> str:
        """
        Get color as hex string.
        
        Returns:
            String in format '#RRGGBB' or '#RRGGBBAA' if alpha < 1
        """
        ...

    @property
    def rgb_string(self) -> str:
        """
        Get color as CSS RGB/RGBA string.
        
        Returns:
            String in format 'rgb(R,G,B)' or 'rgba(R,G,B,A)' if alpha < 1
        """
        ...

    @staticmethod
    def is_valid(color_str: str) -> bool:
        """
        Check if a color string is valid.
        
        Args:
            color_str: String to validate
            
        Returns:
            True if string represents a valid CSS color, False otherwise
        """
        ...
