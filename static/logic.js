var url = "/api/v1.0/happiness";

// Fetch the JSON data and console log it
fetch(url)
  .then(response => response.json())
  .then(data => {
    console.log(data)
  });
  
// function transformData(data, key) {
//     objArray=[];
   
//    + Object.entries(data[0][key]).forEach(e=> {
//       obj = {};
//      obj[e[0]] = e[1]
//      objArray.push(obj)
     
//     })
//   return objArray
// }

// Create a map object
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});

// Add a tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

d3.json(url, function(data) {
  // Creating a GeoJSON layer with the retrieved data
  L.geoJson(data).addTo(myMap);
  // Loop through the cities array and create one marker for each city, bind a popup containing its name and population add it to the map
  for (var i = 0; i < data.length; i++) {
    try {
      // nonExistentFunction();
        var country = data[i];
        L.marker([country.Latitude, country.Longitude]) //
          .bindPopup("<h1>" + country.Country + "</h1> <hr> <h3>Happiness Ladder Score " + country["Ladder score"] + "</h3>") // finish adding rest of data
          .addTo(myMap);
        console.log("random");
    } catch {
      console.log("error");
      // expected output: ReferenceError: nonExistentFunction is not defined
      // Note - error messages will vary depending on browser
    }
  }
})
