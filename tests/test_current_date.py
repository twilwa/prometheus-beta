import datetime
import pytest
from src.current_date import get_current_date_formatted

def test_get_current_date_formatted():
    """
    Test that the function returns the current date in YYYY-MM-DD format.
    """
    # Get the current date
    today = datetime.date.today()
    
    # Call the function
    formatted_date = get_current_date_formatted()
    
    # Check the format
    assert isinstance(formatted_date, str), "Return value should be a string"
    assert len(formatted_date) == 10, "Formatted date should be 10 characters long"
    
    # Check that the returned date matches today's date
    assert formatted_date == today.strftime('%Y-%m-%d'), "Formatted date should match current date"

def test_date_format():
    """
    Test the specific format of the returned date string.
    """
    formatted_date = get_current_date_formatted()
    
    # Check year part (first 4 characters)
    assert formatted_date[:4].isdigit(), "Year should be 4 digits"
    
    # Check hyphen separators
    assert formatted_date[4] == '-', "First separator should be a hyphen"
    assert formatted_date[7] == '-', "Second separator should be a hyphen"
    
    # Check month and day parts
    assert formatted_date[5:7].isdigit(), "Month should be 2 digits"
    assert formatted_date[8:].isdigit(), "Day should be 2 digits"