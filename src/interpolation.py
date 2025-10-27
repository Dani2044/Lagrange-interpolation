from typing import List, Tuple

def lagrange_interpolation(data: List[Tuple[int, float, bool]], target_year: int) -> float:
    """
    Perform interpolation using Lagrange polynomial.
    
    Args:
        data: List of (year, population, has_data) tuples
        target_year: Year to interpolate population for
        
    Returns:
        Interpolated population value
    """
    # Extract known data points
    known_years = []
    known_populations = []
    
    for year, population, has_data in data:
        if has_data:
            known_years.append(year)
            known_populations.append(population)
    
    n = len(known_years)
    if n < 2:
        raise ValueError("Not enough data points for interpolation")
    
    result = 0.0
    
    # Apply Lagrange interpolation formula
    for i in range(n):
        term = known_populations[i]
        for j in range(n):
            if i != j:
                term *= (target_year - known_years[j]) / (known_years[i] - known_years[j])
        result += term
    
    return result

def interpolate_missing_data(data: List[Tuple[int, float, bool]]) -> List[Tuple[int, float, bool]]:
    """
    Interpolate all missing data points using Lagrange method.
    
    Args:
        data: List of population data tuples
        
    Returns:
        Complete dataset with interpolated values
    """
    complete_data = data.copy()
    
    for i, (year, _, has_data) in enumerate(complete_data):
        if not has_data:
            try:
                interpolated_pop = lagrange_interpolation(data, year)
                complete_data[i] = (year, round(interpolated_pop), False)
            except ValueError as e:
                print(f"Error interpolating year {year}: {e}")
    
    return complete_data

def get_missing_years(data: List[Tuple[int, float, bool]]) -> List[int]:
    """
    Get list of years with missing data.
    
    Args:
        data: List of population data tuples
        
    Returns:
        List of years with missing population data
    """
    return [year for year, _, has_data in data if not has_data]

def count_known_data(data: List[Tuple[int, float, bool]]) -> int:
    """
    Count number of known data points.
    
    Args:
        data: List of population data tuples
        
    Returns:
        Number of data points with known population values
    """
    return sum(1 for _, _, has_data in data if has_data)