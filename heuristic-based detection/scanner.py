import os

# Define suspicious file extensions
SUSPICIOUS_EXTENSIONS = [".com", ".exe", ".bat", ".vbs"]
MEDIA_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".mp4", ".avi", ".mp3", ".wav"]

def check_file_size(file_path, max_size=10*1024*1024):
    """Check if the file size is suspiciously large."""
    try:
        file_size = os.path.getsize(file_path)
        return file_size > max_size
    except Exception as e:
        print(f"Error checking file size {file_path}: {e}")
        return False

def check_suspicious_strings(file_path, suspicious_strings=None):
    """Check for suspicious strings in the file."""
    if suspicious_strings is None:
        suspicious_strings = ["malicious", "virus", "trojan", "malware"]
    try:
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read()
            return any(s in content for s in suspicious_strings)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return False

def is_executable(file_path):
    """Check if the file is executable."""
    return os.access(file_path, os.X_OK)

def check_file_extension(file_path):
    """Check if the file has a suspicious extension."""
    _, extension = os.path.splitext(file_path)
    return extension.lower() in SUSPICIOUS_EXTENSIONS

def check_media_file(file_path):
    """Check if the file is a media file."""
    _, extension = os.path.splitext(file_path)
    return extension.lower() in MEDIA_EXTENSIONS

def scan_file(file_path):
    """Scan a single file using heuristic methods."""
    suspicious = (
        check_file_size(file_path) or 
        check_suspicious_strings(file_path) or 
        is_executable(file_path) or 
        check_file_extension(file_path) or 
        check_media_file(file_path)
    )
    return suspicious

def scan_directory(directory_path):
    """Scan all files in a directory using heuristic methods."""
    results = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            suspicious = scan_file(file_path)
            results.append((file_path, suspicious))
    return results
