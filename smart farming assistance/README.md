# Smart Farming Assistance

A Python-based smart farming assistant for gardeners and farmers that uses real-time weather forecast data to provide detailed weekly analysis.

## Project Overview

This project:
- uses the `requests` library to fetch weather and geocoding data from the Open-Meteo API
- performs API handling for location lookup and 7-day forecast retrieval
- stores a locally generated weekly weather summary in `data.txt`
- provides a simple local crop database in `cropdata.py`
- recommends crop suitability for the week based on forecast temperature and rainfall

## Features

1. **Real-time weather forecast**
   - Retrieves 7-day weather data for a chosen location
   - Uses latitude and longitude from Open-Meteo geocoding
   - Reads daily forecast values including temperature, precipitation, windspeed, and precipitation probability

2. **Local persistence**
   - Writes a weekly rainfall summary to `data.txt`
   - This file is used by menu features for alerts and scheduling

3. **Dashboard menu**
   - Rainfall alert
   - Irrigation scheduler
   - Best day to spray pesticide
   - Heat / cold wave warning
   - Crop suitability checker
   - Change location

4. **Crop suitability database**
   - Supports crops such as rice, wheat, maize, sugarcane, cotton, jute, tea, coffee, tobacco, mustard, potato, groundnut, brinjal, tomato
   - Each crop has ideal temperature and rainfall ranges
   - The app compares the weekly forecast against crop requirements and reports whether conditions are suitable

## How it works

- `main.py` handles user interaction and menu flow
- `fun_ctions.py` reads the locally stored forecast summary and creates weather-based recommendations
- `cropdata.py` contains crop-specific suitability logic
- `main.py` also handles location lookup, forecast fetching, and saving weather data to `data.txt`

## Usage

1. Run `main.py`
2. Enter a location when prompted
3. Choose menu options to view alerts and recommendations
4. Use the crop checker to verify whether a chosen crop is suitable for the current week

## Notes

- The project uses `requests` for API calls and Python built-in modules like `datetime` for date formatting
- The weather response is stored locally so daily analysis features can work offline after the forecast is saved
- The crop checker acts as a lightweight local database for crop advice
