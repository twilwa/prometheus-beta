import logging

# Configure a handler to capture logs
log_capture_handler = logging.StreamHandler()
log_capture_handler.setLevel(logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(log_capture_handler)

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
    
    # Log the type using the preconfigured logger
    logger.info(f"Variable type: {var_type}")
    
    return var_type