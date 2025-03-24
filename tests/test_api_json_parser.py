import pytest
import json
from src.api_json_parser import parse_api_json_response

def test_valid_json_response():
    """Test parsing a valid JSON response."""
    test_response = '{"name": "John", "age": 30}'
    result = parse_api_json_response(test_response)
    assert result == {"name": "John", "age": 30}

def test_nested_json_response():
    """Test parsing a nested JSON response."""
    test_response = '{"user": {"name": "John", "details": {"age": 30, "city": "New York"}}}'
    result = parse_api_json_response(test_response)
    assert result == {"user": {"name": "John", "details": {"age": 30, "city": "New York"}}}

def test_empty_string_raises_error():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="JSON response cannot be empty"):
        parse_api_json_response("")

def test_whitespace_string_raises_error():
    """Test that a whitespace-only string raises a ValueError."""
    with pytest.raises(ValueError, match="JSON response cannot be empty"):
        parse_api_json_response("   \t\n")

def test_invalid_json_raises_error():
    """Test that an invalid JSON string raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid JSON format"):
        parse_api_json_response("{invalid json}")

def test_non_object_json_raises_error():
    """Test that non-object JSON (like an array) raises a ValueError."""
    with pytest.raises(ValueError, match="Parsed JSON must be an object/dictionary"):
        parse_api_json_response('[1, 2, 3]')

def test_json_with_different_types():
    """Test parsing JSON with various data types."""
    test_response = '{"string": "hello", "number": 42, "boolean": true, "null": null}'
    result = parse_api_json_response(test_response)
    assert result == {"string": "hello", "number": 42, "boolean": True, "null": None}