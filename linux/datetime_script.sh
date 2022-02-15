#!/usr/bin/env bash

echo $(date +"%D - %T") >> datetime.txt

# crontab
# 0 * * * * /home/krolya/python-education/linux/datetime_script.sh
