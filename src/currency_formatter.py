def format_currency(number, currency='$', decimal_places=2):
    """
    Format a number with a currency symbol and specified decimal places.
    
    Args:
        number (int, float): The number to be formatted.
        currency (str, optional): Currency symbol to use. Defaults to '$'.
        decimal_places (int, optional): Number of decimal places. Defaults to 2.
    
    Returns:
        str: Formatted currency string.
    
    Raises:
        TypeError: If number is not a numeric type.
        ValueError: If decimal_places is negative.
    """
    # Validate input types
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be an integer or float")
    
    # Validate decimal places
    if decimal_places < 0:
        raise ValueError("Decimal places cannot be negative")
    
    # Format the number with specified decimal places and currency symbol
    try:
        formatted = f"{currency}{number:,.{decimal_places}f}"
        return formatted
    except Exception as e:
        raise ValueError(f"Error formatting currency: {str(e)}")