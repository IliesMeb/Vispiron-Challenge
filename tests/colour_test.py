import pytest
from src.colour import Colour

def test_correct_colour_object_creation():
    """create right Colour Object with hexa code"""
    color = Colour("#F5FFFA")
    assert color.hexa_value == "#F5FFFA"
    assert color.red == 245
    assert color.green == 255
    assert color.blue == 250
    assert color.brightness.__round__(0) == 252
    assert color.colour_name == "MintCream"

def test_invalid_hexa_code():
    """identify incorrect hexa code: missing #"""

    with pytest.raises(ValueError, match=f"Invalid hex colour code: AABBCC"):
        Colour("AABBCC")

def test_brightness_calculation():
    """calculate right brightness"""
    white = Colour("#FFFFFF").calculate_brightness()
    black = Colour("#000000").calculate_brightness()
    assert white > black

def test_right_message():
    """return right message when a list of hexa codes is provided"""
    colors = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
    result = Colour.find_brightest_color(colors)
    assert result == "The brightes color is: #FFFFFF (r=255, g=255, b=255) called White"

def test_error_message_when_wrong_hexa_code():
    """return right message when a list of hexa codes is provided: #FFFFFZ"""
    colors = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFZ"]
    with pytest.raises(ValueError, match=f"Invalid hex colour code: #FFFFFZ"):
        Colour.find_brightest_color(colors)
