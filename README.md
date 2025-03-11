# Realistic Daylight

This project aims to obtain the available exposure to direct sunlight for a given location and date with consideration of surrounding orography.

## File Structure Tree

<pre>
RealisticDaylight/
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── README.md
├── requirements.txt
├── .github/
│   └── workflows/
│       └── python-app.yml
├── .pytest_cache/
│   ├── .gitignore
│   ├── CACHEDIR.TAG
│   └── v/
│       └── cache/
│           ├── lastfailed
│           ├── nodeids
│           └── stepwise
├── <span style="color:blue;">RealisticDaylight/ (Main Project Folder)</span>
│   ├── __pycache__/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── data/
│   │   └── sample_data.csv
│   ├── <span style="color:blue;">src/ (Source code goes in here)</span>
│   │   ├── __init__.py
│   │   ├── daylight_calculator.py
│   │   ├── main.py
│   │   └── orography_handler.py
│   └── tests/
│       ├── test_daylight_calculator.py
│       └── test_orography_handler.py
</pre>