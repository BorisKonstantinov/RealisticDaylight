# Realistic Daylight

This project aims to obtain the available exposure to direct sunlight for a given location and date with consideration of surrounding orography.

## File Structure Tree

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
├── RealisticDaylight/ <p style="color:blue;">Main Project Folder</p>
│   ├── __pycache__/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── data/
│   │   └── sample_data.csv
│   ├── src/ <p style="color:blue;">Source code goes in here</p>
│   │   ├── __init__.py
│   │   ├── daylight_calculator.py
│   │   ├── main.py
│   │   └── orography_handler.py
│   └── tests/
│       ├── test_daylight_calculator.py
│       └── test_orography_handler.py