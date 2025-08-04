# Weather App - Multiple Tech Stack Implementations

A weather app implemented in four different tech stacks, all using the OpenWeatherMap API.

## Setup

1. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. For React version, install Node.js dependencies:
   ```bash
   cd react_express_app && npm install
   ```

## Implementations

### 1. Command Line (Python)
**File:** `weather_app.py`
```bash
python3 weather_app.py
```

### 2. Flask + Bootstrap Web UI
**File:** `flask_bootstrap_app.py`
**Templates:** `flask_bootstrap_templates/`
```bash
python3 flask_bootstrap_app.py
```
**URL:** http://localhost:5000

### 3. FastAPI + Tailwind Web UI
**File:** `fastapi_tailwind_app.py`
**Templates:** `fastapi_tailwind_templates/`
```bash
python3 fastapi_tailwind_app.py
```
**URL:** http://localhost:8000

### 4. React + Express Full Stack
**Directory:** `react_express_app/`

**Option A - Run both together:**
```bash
cd react_express_app && npm run dev
```

**Option B - Run separately:**
```bash
# Terminal 1 - Backend
cd react_express_app && npm run server

# Terminal 2 - Frontend
cd react_express_app/client && npm start
```
**URL:** http://localhost:3000

## API Key

The app uses a default OpenWeatherMap API key. For production, set your own:
```bash
export OPENWEATHER_API_KEY="your_api_key"
```
Get a free key at [OpenWeatherMap](https://openweathermap.org/api)

## Git Setup

This project uses the Python .gitignore template with additional Node.js entries for the React Express app to ignore `node_modules/`, build files, and other generated content.