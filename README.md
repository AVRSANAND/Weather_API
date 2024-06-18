# Weather Data API 

## Overview
This project is a Flask-based web API for accessing historical weather data. The API serves data from text files stored in the `data_small` folder. It allows users to query temperature data for specific stations and dates. The project is intended for educational purposes, demonstrating how to build a simple RESTful API using Python and Flask.

## Features
- **Home Page**: Displays a table of available weather stations.
- **API Endpoints**:
  - Get temperature data for a specific station on a specific date.
  - Get all temperature data for a specific station.
  - Get all temperature data for a specific station for a specific year.

## Project Structure
```
weather-api/
│
├── data_small/             # Folder containing weather data files
│   ├── stations.txt        # List of stations
│   ├── TG_STAID000001.txt  # Weather data for station 1
│   ├── TG_STAID000002.txt  # Weather data for station 2
│   └── ...                 # Additional weather data files
│
├── templates/
│   └── index.html          # HTML template for the home page
│
├── main.py                 # Main application script
├── README.md               # Project README file
└── requirements.txt        # Project dependencies
```

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/weather-api.git
    cd weather-api
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python main.py
    ```

## Usage
Once the application is running, you can access the following endpoints by opening the development server in your browser `http://127.0.0.1:5000`:

### Home Page
- **URL**: `/`
- **Description**: Displays a table of available weather stations.

### Get temperature data for a specific station on a specific date
- **URL**: `/api/v1/<station>/<date>`
- **Method**: GET
- **Parameters**:
  - `station`: The station ID (e.g., `10`).
  - `date`: The date in `YYYY-MM-DD` format (e.g., `2001-09-11`).
- **Example**:
  ```bash
  curl http://127.0.0.1:5000/api/v1/10/2001-09-11
  ```
- **Response**:
  ```json
  {
      "station": "10",
      "date": "2001-09-11",
      "temperature": 15.2
  }
  ```

### Get all temperature data for a specific station
- **URL**: `/api/v1/<station>`
- **Method**: GET
- **Parameters**:
  - `station`: The station ID (e.g., `10`).
- **Example**:
  ```bash
  curl http://127.0.0.1:5000/api/v1/10
  ```
- **Response**:
  ```json
  [
      {
          "    DATE": "2001-09-11",
          "   TG": 152
      },
      ...
  ]
  ```

### Get all temperature data for a specific station for a specific year
- **URL**: `/api/v1/yearly/<station>/<year>`
- **Method**: GET
- **Parameters**:
  - `station`: The station ID (e.g., `10`).
  - `year`: The year (e.g., `2001`).
- **Example**:
  ```bash
  curl http://127.0.0.1:5000/api/v1/yearly/10/2001
  ```
- **Response**:
  ```json
  [
      {
          "    DATE": "2001-01-01",
          "   TG": 45
      },
      ...
  ]
  ```

## Notes
- **Temperature Data**: The temperature values (`TG`) in the data files are stored as integers to save space. The actual temperature is the stored value divided by 10. For example, a value of `152` corresponds to `15.2°C`.

## Dependencies
- Flask
- pandas
