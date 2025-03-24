import json
from typing import Any, Dict, Optional

def parse_api_json_response(response: str) -> Dict[str, Any]:
    """
    Parse a JSON response from an API.

    Args:
        response (str): A JSON-formatted string from an API response.

    Returns:
        Dict[str, Any]: A dictionary containing the parsed JSON data.

    Raises:
        ValueError: If the input is an empty string.
        json.JSONDecodeError: If the input is not a valid JSON string.
    """
    # Check for empty input
    if not response or not response.strip():
        raise ValueError("JSON response cannot be empty")

    try:
        # Attempt to parse the JSON string
        parsed_response = json.loads(response)
        
        # Ensure the parsed response is a dictionary
        if not isinstance(parsed_response, dict):
            raise ValueError("Parsed JSON must be an object/dictionary")
        
        return parsed_response
    except json.JSONDecodeError as e:
        # Re-raise with a more informative error message
        raise ValueError(f"Invalid JSON format: {str(e)}")