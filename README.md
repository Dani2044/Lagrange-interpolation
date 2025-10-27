# Population Data Analysis Project

A numerical analysis project that performs Lagrange interpolation on population data to estimate missing values and visualize population trends.

## 📁 Project Structure

```
population-analysis/
├── data/
│   └── population.txt             # Input population data file
├── output/
│   ├── interpolation_results.txt  # Results of interpolation
│   ├── plot_data.txt              # Formatted data for plotting
│   └── population_plot.png        # Generated population plot
├── src/
│   ├── __init__.py
│   ├── file_io.py                # File input/output operations
│   ├── interpolation.py          # Lagrange interpolation functions
│   └── visualization.py          # Plot generation using matplotlib
├── main.py                       # Main program entry point
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Features

- **Data Reading**: Reads population data from text files with support for missing values
- **Lagrange Interpolation**: Uses polynomial interpolation to estimate missing population values
- **Data Visualization**: Generates professional population trend plots
- **Formatted Output**: Creates well-aligned text files with results
- **Error Handling**: Robust error handling for file operations and data processing

## 📊 Data Format

The input file `population.txt` should contain:
- Header line with description
- Data lines with format: `YEAR POPULATION`
- Missing values marked as `-1`

Example:
```
Country 16 Population Data (1990-2023)
1990 24563215
1991 -1
1992 25678901
...
```

## 🛠️ Installation & Usage

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd population-analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare your data**
   - Place your population data in `data/population.txt`

4. **Run the analysis**
   ```bash
   python main.py
   ```

## 📈 Output

The program generates:

- **Console Output**: Summary statistics and interpolation results
- **plot_data.txt**: Well-formatted data for external plotting
- **interpolation_results.txt**: Only the interpolated values
- **population_plot.png**: Visual representation of population trends

## 🔧 Dependencies

- Python 3.7+
- matplotlib
- numpy (if needed for future enhancements)

## 🧮 Interpolation Method

Uses **Lagrange Polynomial Interpolation**:
- Constructs a polynomial that passes through all known data points
- Evaluates the polynomial at missing years
- Provides smooth estimates for missing population values

## 📋 Functions Overview

### File I/O (`src/file_io.py`)
- `read_population_data()`: Reads and parses input data
- `write_plot_data()`: Creates formatted plotting data
- `write_interpolation_results()`: Saves interpolation results

### Interpolation (`src/interpolation.py`)
- `lagrange_interpolation()`: Core interpolation algorithm
- `interpolate_missing_data()`: Applies interpolation to all missing points
- `get_missing_years()`: Identifies years needing interpolation

### Visualization (`src/visualization.py`)
- `create_population_plot()`: Generates matplotlib population plot

## 🎯 Usage Example

```python
# Read data
data = read_population_data("data/population.txt")

# Interpolate missing values
complete_data = interpolate_missing_data(data)

# Generate visualization
create_population_plot(complete_data)
```

## 📊 Plot Features

- Original data points marked in blue
- Interpolated values marked in red
- Smooth population trend line
- Professional formatting and styling
- High-resolution output (300 DPI)

## 🔍 Error Handling

- File not found errors
- Invalid data format detection
- Insufficient data points for interpolation
- Robust exception handling throughout

## 📝 License

This project is for educational purposes in numerical analysis.