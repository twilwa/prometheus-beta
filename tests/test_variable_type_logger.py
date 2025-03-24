import pytest

from src.variable_type_logger import log_variable_type

def test_log_variable_type_primitive_types(caplog):
    """Test logging of primitive types."""
    # Test various primitive types
    test_cases = [
        (42, 'int'),
        ("Hello", 'str'),
        (3.14, 'float'),
        (True, 'bool'),
        (None, 'NoneType')
    ]

    for variable, expected_type in test_cases:
        # Call the function
        result = log_variable_type(variable)

        # Check returned type
        assert result == expected_type, f"Failed for {variable}"

        # Check logged message
        assert f"Variable type: {expected_type}" in caplog.text, f"Log message incorrect for {variable}"

def test_log_variable_type_complex_types(caplog):
    """Test logging of complex types."""
    # Test various complex types
    test_cases = [
        ([], 'list'),
        ({}, 'dict'),
        (set(), 'set'),
        (tuple(), 'tuple'),
        ((x for x in range(5)), 'generator')
    ]

    for variable, expected_type in test_cases:
        # Call the function
        result = log_variable_type(variable)

        # Check returned type
        assert result == expected_type, f"Failed for {variable}"

        # Check logged message
        assert f"Variable type: {expected_type}" in caplog.text, f"Log message incorrect for {variable}"

def test_log_variable_type_custom_class(caplog):
    """Test logging of custom class type."""
    class TestClass:
        pass

    test_instance = TestClass()

    # Call the function
    result = log_variable_type(test_instance)

    # Check returned type
    assert result == 'TestClass'

    # Check logged message
    assert "Variable type: TestClass" in caplog.text