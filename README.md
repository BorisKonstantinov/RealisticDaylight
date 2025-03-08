# RealisticDaylight
Estimates the sunlight available at a location, taking into account the surrounding orography.

│
├── .github/
│   │
│   └── workflows/
│       └── python-app.yml
│
│
├── RealisticDaylight/
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── src/
│   │   │
│   │   ├── __pycache__/
│   │   │   └── daylight_calculator.cpython-312.pyc
│   │   │
│   │   ├── __init__.py
│   │   ├── daylight_calculator.py
│   │   ├── main.py
│   │   └── orography_handler.py
│   │
│   └── __init__.py
│
├── data/
│   └── sample_data.csv
│
├── tests/
│   ├── mytests.ipynb
│   ├── test_daylight_calculator.py
│   └── test_orography_handler.py
│
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── README.md
└── requirements.txt