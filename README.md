# ai_portfolio_project
# AI Data Engineer Portfolio Project

This project demonstrates a simple data pipeline built with Python and SQL.  
It fetches weather data from an API, processes it, and stores it in CSV, SQLite, and PostgreSQL.

## Tech Stack
- Python
- Pandas
- REST API
- SQL
- SQLite
- PostgreSQL

## Features
- API data collection
- JSON → structured data
- CSV export
- SQLite storage
- PostgreSQL storage
- Basic ETL pipeline

## Run project

Activate venv:
.venv\Scripts\activate

Run SQLite pipeline:
python src/weather_api.py

Run PostgreSQL pipeline:
python src/weather_pg.py

## PostgreSQL table
CREATE TABLE weather (
  time TEXT,
  interval INTEGER,
  temperature DOUBLE PRECISION,
  windspeed DOUBLE PRECISION,
  winddirection INTEGER,
  is_day INTEGER,
  weathercode INTEGER
);

## Purpose
This project was created as a portfolio example for a Junior AI/Data Engineer position.
