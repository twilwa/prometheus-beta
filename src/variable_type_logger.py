import logging

def log_variable_type(variable):
    """
    Log the type of a given variable.

    Args:
        variable: Any Python object whose type needs to be logged.

    Returns:
        str: The string representation of the variable's type.

    Example:
        >>> log_variable_type(42)
        'int'
        >>> log_variable_type("Hello")
        'str'
    """
    # Get the type of the variable as a string
    var_type = type(variable).__name__
    
    # Log the type using Python's logging module
    logging.info(f"Variable type: {var_type}")
    
    return var_type