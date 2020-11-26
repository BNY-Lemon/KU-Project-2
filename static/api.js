var url = "/api/v1.0/happiness";

// Fetch the JSON data and console log it
fetch(url)
  .then(response => response.json())
  .then(data => console.log(data));

// // Promise Pending
// var dataPromise = d3.json(url);
// console.log("Data Promise: ", dataPromise);
