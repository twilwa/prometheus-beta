import os
import requests

def download_file(url, destination=None):
    """
    Download a file from a given URL.

    Args:
        url (str): The URL of the file to download.
        destination (str, optional): The path where the file should be saved. 
                                     If not provided, uses the filename from the URL.

    Returns:
        str: The path where the file was saved.

    Raises:
        ValueError: If the URL is invalid or empty.
        requests.RequestException: If there's an error during the download.
        IOError: If there's an issue writing the file.
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    try:
        # Send a GET request to download the file
        response = requests.get(url, stream=True)
        
        # Raise an exception for bad HTTP responses
        response.raise_for_status()

        # Determine destination path
        if destination is None:
            # Extract filename from URL if no destination provided
            filename = url.split('/')[-1]
            destination = os.path.join(os.getcwd(), filename)

        # Ensure directory exists
        os.makedirs(os.path.dirname(destination) or os.getcwd(), exist_ok=True)

        # Write the file
        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        return destination

    except requests.RequestException as e:
        raise requests.RequestException(f"Error downloading file from {url}: {str(e)}")
    except IOError as e:
        raise IOError(f"Error saving file to {destination}: {str(e)}")