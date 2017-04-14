# airwatch-watch

!["airwatch points"](https://raw.githubusercontent.com/phil8192/airwatch-watch/master/points.png "airwatch points") 

[AirWatch](https://air-watch.com/) is a set of tools for "[Enterprise mobility management](https://en.wikipedia.org/wiki/AirWatch)".
lots of companies install it on company issued laptops, phones etc for remote management.

disturbingly, amongst other things, the airwatch client continuously logs location, altitude and even current velocity data.

this script extracts a `timestamp, id, current ip, latitude, longitude, altitude, speed' csv from data stored
in an airwatch log file. on a mac, this can be found in:

```
/Library/Application\ Support/AirWatch/Data/Logs/AWLogs.log
```  

# running

## 1) extract coordinates

copy the AWSLogs.log file somewhere, then in the same working dir:

```bash
./parse.sh
```

you will end up with `push.csv` and `push_points.geojson`.

## 3) visualise

a [leaflet.js](https://github.com/Leaflet/Leaflet) + [turf,js](https://github.com/Turfjs/turf) visualisation is in vis/. 
