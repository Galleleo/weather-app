from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from weather_app import WeatherApp

app = FastAPI()
templates = Jinja2Templates(directory="fastapi_tailwind_templates")
weather_service = WeatherApp()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/weather", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = Form(...)):
    if not city.strip():
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "error": "Please enter a city name"
        })
    
    weather_data = weather_service.get_weather(city.strip())
    
    if "error" in weather_data:
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "error": weather_data['error']
        })
    
    return templates.TemplateResponse("weather.html", {
        "request": request, 
        "weather": weather_data
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)