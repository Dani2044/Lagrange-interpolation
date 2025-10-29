import matplotlib.pyplot as plt
import os
from typing import List, Tuple

def create_population_plot(complete_data: List[Tuple[int, float, bool]], output_dir: str = "output"):
    """
    Create population plot using matplotlib.
    
    Args:
        complete_data: Complete dataset with interpolated values
        output_dir: Output directory for saving the plot
    """
    # Extract data
    years = [item[0] for item in complete_data]
    populations = [item[1] for item in complete_data]
    data_types = [item[2] for item in complete_data]
    
    # Separate original and interpolated data
    original_years = [years[i] for i in range(len(years)) if data_types[i]]
    original_pops = [populations[i] for i in range(len(populations)) if data_types[i]]
    interpolated_years = [years[i] for i in range(len(years)) if not data_types[i]]
    interpolated_pops = [populations[i] for i in range(len(populations)) if not data_types[i]]
    
    # Create plot
    plt.figure(figsize=(12, 8))
    
    # Plot trend line
    plt.plot(years, populations, 'b-', linewidth=2, alpha=0.7, label='Population Trend')
    
    # Plot original data points
    plt.plot(original_years, original_pops, 'bo', markersize=6, label='Original Data')
    
    # Plot interpolated data points
    if interpolated_years:
        plt.plot(interpolated_years, interpolated_pops, 'ro', markersize=6, label='Interpolated Data')
    
    # Customize plot
    plt.title('Population Evolution (1990-2023) - Country 16', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Population', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Format y-axis
    plt.ticklabel_format(style='plain', axis='y')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    os.makedirs(output_dir, exist_ok=True)
    plot_path = os.path.join(output_dir, "population_plot.png")
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    plt.show()