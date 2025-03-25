from math import sqrt
from typing import List

import requests

class Colour:
    def __init__(self, hexa_value: str):
        self.hexa_value = hexa_value.upper()

        if not self._is_valid_hexa_code(hexa_value):
            raise ValueError(f"Invalid hex colour code: {hexa_value}")
        
        self.red = int(self.hexa_value[1:3], 16)
        self.green = int(self.hexa_value[3:5], 16)
        self.blue = int(self.hexa_value[5:7], 16)
        self.colour_name = self._get_color_name(self.hexa_value)
        self.brightness = self.calculate_brightness()
    
    @classmethod
    def find_brightest_color(cls, hexa_colors_list: List[str]) -> str:
        """Find the brightest color from a list of hexa color codes."""
        if not hexa_colors_list:
            raise ValueError("Color list cannot be empty")

        brightness_list: List[dict] = []

        for hexa_code in hexa_colors_list:
            color = Colour(hexa_code)
            brightness_list.append(color.__dict__)

        for brightness_dict in brightness_list:
            if brightness_dict["brightness"] == max(brightness_list, key=lambda x: x["brightness"])["brightness"]:
                brightest_color = brightness_dict
        
        if not brightest_color["colour_name"]:
            return f"The brightes color is: {brightest_color['hexa_value']} (r={brightest_color['red']}, g={brightest_color['green']}, b={brightest_color['blue']})"

        return f"The brightes color is: {brightest_color['hexa_value']} (r={brightest_color['red']}, g={brightest_color['green']}, b={brightest_color['blue']}) called {brightest_color['colour_name']}"

    def _is_valid_hexa_code(self, hexa_value: str) -> bool:
        if not hexa_value[0] == '#' or len(hexa_value) != 7:
            return False
        for i in range(1, 7):
                if not hexa_value[i] in '0123456789ABCDEF':
                    return False
        return True
    
    def calculate_brightness(self) -> float:
        """Calculate the brightness of a color using the formula: sqrt(0.241 R^2 + 0.691 G^2 + 0.068 B^2)."""
        return sqrt(
            0.241 * (self.red ** 2) +
            0.691 * (self.green ** 2) +
            0.068 * (self.blue ** 2)
        )
    
    def _get_color_name(self, hexa_code) -> str:
        """
        Get color name from API https://www.csscolorsapi.com/
        """
        try:
            url = "https://csscolorsapi.com/api/colors"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            for colour in data.get('colors'):
                if colour.get('hex').upper() == hexa_code.lstrip('#').upper():
                    return colour.get('name')
        except Exception as e:
            return "color name not found because of following error {e}"
        