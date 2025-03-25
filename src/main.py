import sys
from typing import Dict, List

from colour import Colour

def main():
    if len(sys.argv) > 1:
        colors = sys.argv[1:]
    else:
        raise ValueError("No colors provided")
    try:
        result = Colour.find_brightest_color(colors)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
