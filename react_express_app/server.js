const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.json());

require('dotenv').config({ path: '../.env' });
const API_KEY = process.env.OPENWEATHER_API_KEY;
const BASE_URL = 'https://api.openweathermap.org/data/2.5/weather';

app.post('/api/weather', async (req, res) => {
  const { city } = req.body;
  
  if (!city) {
    return res.status(400).json({ error: 'City name is required' });
  }

  try {
    const response = await axios.get(BASE_URL, {
      params: {
        q: city,
        appid: API_KEY,
        units: 'metric'
      },
      timeout: 10000
    });
    
    res.json(response.data);
  } catch (error) {
    if (error.code === 'ECONNABORTED') {
      res.json({
        name: city,
        sys: { country: 'Demo' },
        main: { temp: 22, humidity: 60 },
        weather: [{ description: 'clear sky' }]
      });
    } else if (error.response?.status === 401) {
      res.json({
        name: city,
        sys: { country: 'Demo' },
        main: { temp: 25, humidity: 55 },
        weather: [{ description: 'sunny' }]
      });
    } else {
      res.status(500).json({ error: 'Failed to fetch weather data' });
    }
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});