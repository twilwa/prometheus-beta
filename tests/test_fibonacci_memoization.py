import pytest
from src.fibonacci_memoization import fibonacci_memoized

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert fibonacci_memoized(0) == 0
    assert fibonacci_memoized(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values."""
    # First few values of Fibonacci sequence
    expected_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for n, expected in enumerate(expected_values):
        assert fibonacci_memoized(n) == expected

def test_fibonacci_larger_values():
    """Test larger Fibonacci numbers."""
    assert fibonacci_memoized(10) == 55
    assert fibonacci_memoized(20) == 6765

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Negative number should raise ValueError
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_memoized(-1)
    
    # Non-integer input should raise TypeError
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_memoized(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_memoized("5")

def test_fibonacci_memoization():
    """Verify that the memoization works by checking repeated computations."""
    # We can't directly test memoization's internal cache, 
    # but we can check that repeated calls work correctly
    assert fibonacci_memoized(15) == fibonacci_memoized(15)
    assert fibonacci_memoized(20) == fibonacci_memoized(20)