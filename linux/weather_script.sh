#!/usr/bin/env bash

echo $(curl -X GET "https://api.openweathermap.org/data/2.5/weather?lat=48.6208&lon=22.2879&appid={95d0319ce6240c4933895c8de563b806}")  > weather.json

# crontab
# 0 7 * * * /home/krolya/python-education/linux/weather_script.sh
