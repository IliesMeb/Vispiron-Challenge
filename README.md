# Vispiron-Challenge
Brightness Challenge for Vispiron

# Color Brightness Calculator

A Python application that finds the brightest color from a list of hexadecimal color codes.

## Project Structure
Vispiron Challenge/
├── src/
│ ├── __init__.py
│ ├── colour.py
│ └── main.py
├── tests/
│ ├── __init__.py
│ └── colour_test.py
├── requirements.txt
└── README.md


## Installation

1. Clone the repository (with https):
git clone <"https://github.com/IliesMeb/Vispiron-Challenge.git">

2. Create a virtual environment (recommended):
python -m venv myvenv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  

3. Install dependencies:
pip install -r requirements.txt

## Usage 
run python src/main.py  
add colours ad sys variables  
example: python src/main.py "#AABBCC" "#154331" "#A0B1C2" "#000000"  
output: The brightes color is: #AABBCC (r=170, g=187, b=204)  

if a colourname for the brightest colour is found on https://www.csscolorsapi.com/ the output will be:  
example: python src/main.py "#AABBCC" "#154331" "#A0B1C2" "#154331" "#000000" "#F5FFFA"  
output: The brightes color is: #F5FFFA (r=245, g=255, b=250) called MintCream  

## Run Tests when in root directory:
python -m pytest tests/

## Dependencies
Python 3.7+ (used version Python 3.10.12)  
pytest  
requests (for API integration)  

## Improvment Ideas
Implement a microsservice with FastAPI and an easy Frontend to provide the brightest colour   
For colours without a name on https://www.csscolorsapi.com/, calculate nearest colour matching  
Get the hexa code, when providing a Color name  
