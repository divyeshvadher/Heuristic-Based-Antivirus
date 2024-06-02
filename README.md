# Heuristic-Based-Antivirus

This project is a simple heuristic-based antivirus scanner built with Python. It uses heuristic analysis to identify potential malware or suspicious content in files and directories. The scanner checks for characteristics commonly associated with malware, such as large file size, suspicious strings, executable files, and certain file extensions.

## Features

- **File Size Check**: Flags files that are unusually large.
  
- **Suspicious Strings Check**: Identifies files containing strings commonly associated with malware (e.g., "malicious", "virus", "trojan").
  
- **Executable Check**: Flags files that are executable.
  
- **File Extension Check**: Flags files with suspicious extensions (e.g., `.com`, `.exe`, `.bat`, `.vbs`).
  
- **Media File Check**: Identifies media files (e.g., `.jpg`, `.png`, `.mp4`, `.mp3`).

## Project Structure


- `scanner.py`: Contains the core heuristic analysis functions.
- `main.py`: Placeholder for main logic (currently guides to run `gui.py`).
- `gui.py`: Provides a user interface to scan files and directories.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/divyeshvadher/Heuristic-Based-Antivirus.git
    cd heuristic-antivirus
    ```

2. **Install dependencies** (if any):

    This project primarily relies on the Python standard library. Ensure you have Python installed on your machine.

## Usage

1. **Run the GUI**:

    ```bash
    python3 gui.py
    ```

2. **Use the GUI**:

    - **Scan File**: Click the "Scan File" button to open a file dialog, select a file, and scan it for suspicious characteristics.
    - **Scan Directory**: Click the "Scan Directory" button to open a directory dialog, select a directory, and scan all files within it for suspicious characteristics.
    - **Results**: The results will be displayed in the text area at the bottom of the window, indicating whether each file is suspicious or clean based on the heuristic analysis.
