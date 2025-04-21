import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response
from dicttoxml import dicttoxml
from data import weather_data, cities 

app = FastAPI()

@app.get("/getweather/{city}")
def get_weather(city: str, format: str | None = "JSON"):
    city_data = weather_data.get(city.capitalize(), {"details for city": "Not Found"})

    if format.upper() == "XML":
        xml_data = dicttoxml(city_data, custom_root='weather', attr_type=False)
        return Response(content=xml_data, media_type="application/xml")
    else:
        return JSONResponse(content=city_data)


@app.get("/cities")
def get_cities():
    return JSONResponse(content=cities.get("cities", []))
    

    
