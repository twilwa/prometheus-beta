def find_kth_smallest(arr, k):
    """
    Find the kth smallest element in an array.
    
    Args:
        arr (list): Input list of numbers
        k (int): The k-th smallest element to find (1-based index)
    
    Returns:
        The kth smallest element in the array
    
    Raises:
        ValueError: If k is invalid (less than 1 or greater than array length)
        TypeError: If inputs are of incorrect type
    """
    # Validate inputs
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    # Check for invalid k values
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}, got {k}")
    
    # Edge case for empty list
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Use Python's built-in sorting for simplicity and efficiency
    sorted_arr = sorted(arr)
    
    # Return the kth smallest element (1-based indexing)
    return sorted_arr[k-1]