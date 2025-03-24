import os
import pytest
import requests
from src.file_downloader import download_file

def test_download_file_with_default_destination(tmp_path):
    """Test downloading a file with default destination."""
    # Use a small, reliable file for testing
    test_url = "https://raw.githubusercontent.com/python/cpython/main/LICENSE"
    
    # Change current working directory to temp path
    os.chdir(tmp_path)
    
    # Download the file
    saved_path = download_file(test_url)
    
    # Check if file exists and is not empty
    assert os.path.exists(saved_path)
    assert os.path.getsize(saved_path) > 0
    assert os.path.basename(saved_path) == "LICENSE"

def test_download_file_with_custom_destination(tmp_path):
    """Test downloading a file with a custom destination."""
    test_url = "https://raw.githubusercontent.com/python/cpython/main/LICENSE"
    custom_path = os.path.join(tmp_path, "python_license.txt")
    
    # Change current working directory to temp path
    os.chdir(tmp_path)
    
    # Download the file
    saved_path = download_file(test_url, custom_path)
    
    # Check file details
    assert saved_path == custom_path
    assert os.path.exists(saved_path)
    assert os.path.getsize(saved_path) > 0

def test_invalid_url_raises_error():
    """Test that invalid URLs raise appropriate exceptions."""
    with pytest.raises(ValueError):
        download_file("")
    
    with pytest.raises(ValueError):
        download_file(None)

def test_non_existent_url_raises_error():
    """Test downloading from a non-existent URL raises an exception."""
    with pytest.raises(requests.RequestException):
        download_file("https://example.com/nonexistent_file.txt")

def test_download_to_nested_directory(tmp_path):
    """Test downloading a file to a nested directory."""
    test_url = "https://raw.githubusercontent.com/python/cpython/main/LICENSE"
    nested_path = os.path.join(tmp_path, "downloads", "python", "license.txt")
    
    # Change current working directory to temp path
    os.chdir(tmp_path)
    
    # Download the file
    saved_path = download_file(test_url, nested_path)
    
    # Check file details
    assert saved_path == nested_path
    assert os.path.exists(saved_path)
    assert os.path.getsize(saved_path) > 0