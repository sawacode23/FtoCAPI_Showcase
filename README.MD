# Temperature Conversion API

## Overview

This API allows the conversion of temperature values between Celsius and Fahrenheit. It's built using FastAPI and exposes a single endpoint that takes a temperature value and its unit, and returns the converted value in the other unit.

## Features

- Convert temperature from Celsius to Fahrenheit.
- Convert temperature from Fahrenheit to Celsius.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-repo/temperature-conversion-api.git
   cd temperature-conversion-api
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the application

1. **Start the FastAPI server**:

   ```bash
   uvicorn main:app --reload
   ```

2. **Accessing the API documentation**:
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the automatically generated API documentation by Swagger.

## API Endpoint

### `POST /convert/`

**Request Body**:

- `units` (enum): The unit of the input temperature value. Can be either 'c' for 'celsius' or 'f' for 'fahrenheit'.
- `value` (float): The temperature value to be converted.

Example:

```json
{
  "units": "c",
  "value": 25.0
}
```

**Response**:

- `units` (str): The converted temperature unit.
- `value` (float): The converted temperature value.

Example:

```json
{
  "units": "f",
  "value": 77.0
}
```

**Errors**:

- `400 Bad Request`: Invalid units supplied.

## Conversion Logic

- **Celsius to Fahrenheit**:

  ```
  (9 / 5) * celsius + 32
  ```

- **Fahrenheit to Celsius**:
  ```
  (5 / 9) * (fahrenheit - 32)
  ```
