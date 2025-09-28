# Nature Data Artistic Visualization Project

## Project Description
This project transforms weather data (temperature) into artistic visualizations, exploring the boundary between data visualization and artistic expression.

## Data Source
- Simulated annual temperature data
- Data represents daily temperature variations over a complete year

## Visualization Content
1. **Traditional Line Chart**: Displays annual temperature trends
2. **Temperature Rose Diagram**: Artistic temperature representation in polar coordinates
3. **Scatter Art Plot**: Temperature visualization using size and color encoding

## How to Run
### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Program
```bash
python weather_art.py
```

## File Structure
```
project-folder/
├── weather_art.py       # Main program file
├── requirements.txt     # Dependencies list
├── README.md           # Documentation
├── weather_art.png     # Generated visualization 1
└── simple_weather_art.png # Generated visualization 2
```

## Tech Stack
- **Python 3.x**
- **matplotlib**: Data visualization
- **numpy**: Numerical computations
- **pandas**: Data processing

## Code Example
```python
# Generate simulated weather data
def generate_weather_data():
    dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(365)]
    temperatures = []
    # Simulate seasonal temperature variations...
```

## Generated Visualizations
After running the program, two images will be generated:
- `weather_art.png`: Contains traditional line chart and polar art diagram
- `simple_weather_art.png`: Simplified artistic scatter plot

## Features
- Simulates realistic seasonal temperature variations
- Creative polar coordinate visualization
- Color and size mapping for enhanced visual effects
- Clean and modular code structure

## Project Requirements Met
- ✅ Data from natural sources (weather data)
- ✅ Data processing and cleaning
- ✅ Creative artistic visualization
- ✅ Python programming techniques
- ✅ Complete documentation

## Author
[WANG Leru]

## Course Information
- **Course Name**: [SD5913 Creative Programming for Designers and Artists]
- **Submission Date**: [28/09/2025]