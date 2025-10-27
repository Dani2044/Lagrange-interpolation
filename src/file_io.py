from typing import List, Tuple

def read_population_data(filename: str) -> List[Tuple[int, float, bool]]:
    """
    Read population data from file.
    
    Args:
        filename: Path to input data file
        
    Returns:
        List of (year, population, has_data) tuples
    """
    data = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Read header
            header = file.readline().strip()
            print(f"Reading: {header}")
            
            # Read data
            for line in file:
                line = line.strip()
                if not line:
                    continue
                    
                parts = line.split()
                if len(parts) >= 2:
                    year = int(parts[0])
                    pop_value = parts[1]
                    
                    if pop_value == "-1":
                        data.append((year, -1.0, False))
                    else:
                        data.append((year, float(pop_value), True))
                        
    except FileNotFoundError:
        print(f"Error: Could not open file {filename}")
    except Exception as e:
        print(f"Error reading file: {e}")
        
    return data

def write_plot_data(filename: str, complete_data: List[Tuple[int, float, bool]]):
    """
    Write well-formatted data for plotting.
    
    Args:
        filename: Output file path
        complete_data: Complete dataset with interpolated values
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Calculate column widths for proper alignment
            max_year_width = max(len(str(year)) for year, _, _ in complete_data)
            max_pop_width = max(len(f"{int(pop):,}") for _, pop, _ in complete_data)
            
            # Set minimum widths for headers
            year_width = max(max_year_width, 4)
            pop_width = max(max_pop_width, 10)
            
            # Write header with proper spacing
            file.write(f"{'Year':<{year_width}}  {'Population':<{pop_width}}  Type\n")
            file.write(f"{'-'*year_width}  {'-'*pop_width}  ----\n")
            
            # Write data with perfect alignment
            for year, population, has_data in complete_data:
                data_type = "original" if has_data else "interpolated"
                formatted_pop = f"{int(population):,}"
                file.write(f"{year:<{year_width}}  {formatted_pop:>{pop_width}}  {data_type}\n")
                
        print(f"Plot data written to: {filename}")
    except Exception as e:
        print(f"Error writing plot data: {e}")

def write_interpolation_results(filename: str, complete_data: List[Tuple[int, float, bool]]):
    """
    Write only interpolation results to file.
    
    Args:
        filename: Output file path
        complete_data: Complete dataset with interpolated values
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("INTERPOLATION RESULTS\n")
            file.write("=====================\n\n")
            
            # Calculate column widths
            missing_data = [(year, pop) for year, pop, has_data in complete_data if not has_data]
            if missing_data:
                max_year_width = max(len(str(year)) for year, _ in missing_data)
                max_pop_width = max(len(f"{int(pop):,}") for _, pop in missing_data)
                
                year_width = max(max_year_width, 4)
                pop_width = max(max_pop_width, 10)
                
                file.write(f"{'Year':<{year_width}}  {'Population':<{pop_width}}\n")
                file.write(f"{'-'*year_width}  {'-'*pop_width}\n")
                
                for year, population in missing_data:
                    formatted_pop = f"{int(population):,}"
                    file.write(f"{year:<{year_width}}  {formatted_pop:>{pop_width}}\n")
            else:
                file.write("No interpolation needed - all data available\n")
                
        print(f"Interpolation results written to: {filename}")
    except Exception as e:
        print(f"Error writing interpolation results: {e}")