import os
from src.file_io import read_population_data, write_plot_data, write_interpolation_results
from src.interpolation import interpolate_missing_data, get_missing_years, count_known_data
from src.visualization import create_population_plot

def display_interpolation_results(complete_data):
    """
    Display interpolation results in console.
    
    Args:
        complete_data: Complete dataset with interpolated values
    """
    print("\nINTERPOLATION RESULTS (rounded to nearest integer):")
    print("Year    Population")
    print("----    ----------")
    
    for year, population, has_data in complete_data:
        if not has_data:
            formatted_pop = f"{int(population):,}"
            print(f"{year}    {formatted_pop:>10}")

def display_data_summary(complete_data):
    """
    Display data summary in console.
    
    Args:
        complete_data: Complete dataset with interpolated values
    """
    known_count = count_known_data(complete_data)
    missing_count = len(get_missing_years(complete_data))
    
    print("\n=== DATA SUMMARY ===")
    print(f"Total years: {len(complete_data)} (1990-2023)")
    print(f"Original data points: {known_count}")
    print(f"Interpolated points: {missing_count}")
    print(f"Interpolation method: Lagrange polynomial")

def main():
    """Main function to run population data analysis."""
    # File paths
    input_file = "data/population.txt"
    output_dir = "output"
    plot_data_file = os.path.join(output_dir, "plot_data.txt")
    results_file = os.path.join(output_dir, "interpolation_results.txt")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Read data
    print("=== POPULATION DATA ANALYSIS ===")
    data = read_population_data(input_file)
    
    if not data:
        print("Could not read data.")
        return 1
    
    print(f"Read {len(data)} records.")
    
    # Analyze data
    known_count = count_known_data(data)
    missing_years = get_missing_years(data)
    
    print(f"\n=== INTERPOLATION ANALYSIS ===")
    print(f"Number of known data points: {known_count}")
    
    if missing_years:
        print(f"\nMISSING YEARS TO INTERPOLATE: {missing_years}")
        
        # Interpolate missing data
        complete_data = interpolate_missing_data(data)
        
        # Display interpolation results
        display_interpolation_results(complete_data)
        
        # Write formatted files
        write_plot_data(plot_data_file, complete_data)
        write_interpolation_results(results_file, complete_data)
        
        # Generate plots
        print("\n=== GENERATING POPULATION PLOT ===")
        create_population_plot(complete_data, output_dir)
        
    else:
        print("\nNo years with missing data.")
        complete_data = data
    
    # Display summary
    display_data_summary(complete_data)
    print(f"\nOutput files generated in: {output_dir}/")

if __name__ == "__main__":
    main()