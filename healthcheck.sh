#!/bin/bash

URL="http://127.0.0.1:5000/hello"
LOG="/home/lazare/health.log"

STATUS=$(curl -s -o /dev/null -w "%{http_code}" $URL)

if [ "$STATUS" = "200" ]; then
  echo "$(date): OK" >> $LOG
  exit 0
else
  echo "$(date): FAIL" >> $LOG
  exit 1
fi
