import pytest
import logging
import io
import sys

from src.variable_type_logger import log_variable_type

def test_log_variable_type_primitive_types():
    """Test logging of primitive types."""
    # Redirect logging to capture log output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Test various primitive types
    test_cases = [
        (42, 'int'),
        ("Hello", 'str'),
        (3.14, 'float'),
        (True, 'bool'),
        (None, 'NoneType')
    ]

    for variable, expected_type in test_cases:
        # Reset log capture
        log_capture.truncate(0)
        log_capture.seek(0)

        # Call the function
        result = log_variable_type(variable)

        # Check returned type
        assert result == expected_type, f"Failed for {variable}"

        # Check logged message
        log_output = log_capture.getvalue().strip()
        assert f"Variable type: {expected_type}" in log_output, f"Log message incorrect for {variable}"

def test_log_variable_type_complex_types():
    """Test logging of complex types."""
    # Redirect logging to capture log output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Test various complex types
    test_cases = [
        ([], 'list'),
        ({}, 'dict'),
        (set(), 'set'),
        (tuple(), 'tuple'),
        ((x for x in range(5)), 'generator')
    ]

    for variable, expected_type in test_cases:
        # Reset log capture
        log_capture.truncate(0)
        log_capture.seek(0)

        # Call the function
        result = log_variable_type(variable)

        # Check returned type
        assert result == expected_type, f"Failed for {variable}"

        # Check logged message
        log_output = log_capture.getvalue().strip()
        assert f"Variable type: {expected_type}" in log_output, f"Log message incorrect for {variable}"

def test_log_variable_type_custom_class():
    """Test logging of custom class type."""
    class TestClass:
        pass

    test_instance = TestClass()

    # Redirect logging to capture log output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Call the function
    result = log_variable_type(test_instance)

    # Check returned type
    assert result == 'TestClass'

    # Check logged message
    log_output = log_capture.getvalue().strip()
    assert "Variable type: TestClass" in log_output