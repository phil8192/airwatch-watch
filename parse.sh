#!/bin/bash
cat AWLogs.log |grep sendJsonPayload |grep GPSData |cut -d ' ' -f 1,20- >push.log
python3 parse.py >push.csv
rm -f push.log
python3 csv2geojson.py >push_points.geojson
mkdir -p vis/data
echo -n "var points = " >vis/data/points.js
cat push_points.geojson >>vis/data/points.js
echo "done."
