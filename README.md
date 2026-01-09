# Brio invoice PDF extractor

The **Brio Invoice PDF Extractor** is a template-based tool designed to extract invoice information from PDF documents efficiently and accurately.

## Features
- Extracts invoice details such as **date**, **amount**, **contractant**, **carrier**...
- Supports both single and batch PDF processing.
- Generates structured output in **CSV** formats.
- Handles specifically defined PDF layouts and formats.

## Basic requirements
Python 3.6+ tested (3.8+ recommended / still maintained )

## Setup

1. Clone the repo:
```bash
git clone https://github.com/nico0001/BrioPDFExtractor.git
cd BrioPDFExtractor
```
2. Create and activate a virtual environment:
```cmd
python -m venv .venv
```
### Linux/macOS
```cmd
source .venv/bin/activate
```
### Windows
```cmd
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

```cmd
.venv\Scripts\activate
```
3. Install dependencies:
```cmd
pip install -r requirements.txt
```

4. Load input folder:

Move any desired PDF file(s) in input

5. Run the project:
```cmd
python test.py
```