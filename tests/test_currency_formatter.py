import pytest
from src.currency_formatter import format_currency

def test_default_currency_formatting():
    """Test default currency formatting with $ and 2 decimal places"""
    assert format_currency(1234.56) == '$1,234.56'

def test_different_currency_symbol():
    """Test formatting with different currency symbol"""
    assert format_currency(1234.56, currency='€') == '€1,234.56'

def test_zero_decimal_places():
    """Test formatting with zero decimal places"""
    assert format_currency(1234.56, decimal_places=0) == '$1,235'

def test_multiple_decimal_places():
    """Test formatting with multiple decimal places"""
    assert format_currency(1234.56, decimal_places=4) == '$1,234.5600'

def test_integer_input():
    """Test formatting with integer input"""
    assert format_currency(1234) == '$1,234.00'

def test_negative_number():
    """Test formatting with negative number"""
    assert format_currency(-1234.56) == '$-1,234.56'

def test_large_number():
    """Test formatting with large number"""
    assert format_currency(1234567.89) == '$1,234,567.89'

def test_invalid_number_type():
    """Test raising TypeError for non-numeric input"""
    with pytest.raises(TypeError, match="Number must be an integer or float"):
        format_currency("not a number")

def test_negative_decimal_places():
    """Test raising ValueError for negative decimal places"""
    with pytest.raises(ValueError, match="Decimal places cannot be negative"):
        format_currency(1234.56, decimal_places=-1)