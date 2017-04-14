(function() {

  // bounding box from points
  var bbox = turf.bbox(points); 
 
  // init map and pan/zoom to bounding box.
  var map = L.map("map").fitBounds([[bbox[1], bbox[0]],
                                    [bbox[3], bbox[2]]]);
  
  // use dark mapbox map
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw", {
    maxZoom: 18,
    attribution: "osm contributors :)",
    id: "mapbox.dark"
  }).addTo(map);
  
  // turn point collection into linestring (assume they are in order)
  coords = turf.coordAll(points);
  line = turf.lineString(coords);

  // overlay linestring
  L.geoJSON(line, {
    style: function(f) {
      return { 
        color: "#ff0000",
        weight: 1,
        opacity: 0.25,
        lineCap: "round"
      } 
    } 
  }).addTo(map);

  // overlay points
  L.geoJSON(points, {
    pointToLayer: function(f, lat_lng) {
      return L.circleMarker(lat_lng, {
        radius: 1,
        color: "#ff0000",
        weight: 1,
        opactity: 1,
        fillOpactity: 1 
      });
    }
  }).addTo(map);

})()
