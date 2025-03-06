# Google Search Console Setup

This script helps you set up and test Google Search Console API credentials for use with the MCP.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/ccnn2509/google-search-console-setup.git
cd google-search-console-setup
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the setup script:
```bash
python setup.py
```

2. Follow the instructions provided by the script to:
   - Create a Google Cloud project
   - Enable the Search Console API
   - Create a service account
   - Download credentials

3. Once you have your credentials.json file, place it in this directory and run the script again to test the configuration.

## Using with MCP

After successful setup, you can use the path to your credentials.json file in the MCP configuration.