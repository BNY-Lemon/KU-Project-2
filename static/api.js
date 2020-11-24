const url = "/api/v1.0/pisa";

// Fetch the JSON data and console log it
d3.json(url).then(data => {
  console.log(data)})

// Promise Pending
// const dataPromise = d3.json(url);
// console.log("Data Promise: ", dataPromise);
