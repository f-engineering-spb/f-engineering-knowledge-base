@echo off
title FERO Engineering - Official Website and Brandbook
echo ========================================================
echo   FERO Engineering (ferospb.info) - Local Distribution
echo   Starting local server...
echo ========================================================
python local_server.py
if errorlevel 1 (
    echo.
    echo Python not found in standard PATH, trying 'py'...
    py local_server.py
)
if errorlevel 1 (
    echo.
    echo Python is not installed. You can open 'index.html'
    echo or 'brandbook.html' directly in your browser.
    pause
)
