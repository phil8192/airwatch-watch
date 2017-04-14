import json

print("ts,tid,ip,lat,lon,alt,speed")
with open('push.log') as f:
    for line in f:
        sp = line.find(" ")
        ts = line[:sp]
        js = json.loads(line[sp+1:-1])
        pl = js['payLoad']
        ld = pl['GPSData']
        cd = ",".join([ts,
                       pl.get('TransactionIdentifier', ""),
                       pl.get('IpAddress', ""),
                       str(ld.get('Latitude', "")),
                       str(ld.get('Longitude', "")),
                       str(ld.get('Altitude', "")),
                       str(ld.get('Speed', ""))])
        print(cd)
