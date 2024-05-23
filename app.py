from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from enum import Enum

app = FastAPI()


class UnitsEnum(str, Enum):
    """
    An enumeration for temperature units.

    Attributes:
    -----------
    celsius : str
        The Celsius temperature unit.
    fahrenheit : str
        The Fahrenheit temperature unit.
    """

    celsius = "c"
    fahrenheit = "f"


class ConvertRequest(BaseModel):
    """
    A Pydantic model for temperature conversion requests.

    Attributes:
    -----------
    units : UnitsEnum
        The input temperature unit.
    value : float
        The temperature value to be converted.
    """

    units: UnitsEnum
    value: float


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit.

    Parameters:
    -----------
    celsius : float
        Temperature in Celsius.

    Returns:
    --------
    float
        Temperature in Fahrenheit.
    """
    return (9 / 5) * celsius + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert Fahrenheit to Celsius.

    Parameters:
    -----------
    fahrenheit : float
        Temperature in Fahrenheit.

    Returns:
    --------
    float
        Temperature in Celsius.
    """
    return (5 / 9) * (fahrenheit - 32)


@app.post("/convert/")
def convert(request: ConvertRequest = Body(...)):
    """
    Convert temperature between Celsius and Fahrenheit.

    Parameters:
    -----------
    request : ConvertRequest
        The request body containing the input temperature unit and value.

    Returns:
    --------
    dict
        A dictionary with the converted temperature value and the new unit.

    Raises:
    -------
    HTTPException
        If an invalid unit is supplied.
    """
    input_units = request.units
    if input_units == UnitsEnum.celsius:
        fahrenheit = celsius_to_fahrenheit(request.value)
        return {"units": "fahrenheit", "value": fahrenheit}
    elif input_units == UnitsEnum.fahrenheit:
        celsius = fahrenheit_to_celsius(request.value)
        return {"units": "celsius", "value": celsius}
    else:
        raise HTTPException(status_code=400, detail="Invalid units supplied")
