#!/usr/bin/node

const request = require('request');

// Extract the command-line argument
let number = process.argv[2];

// Check for a film
let url = `https://swapi-api.alx-tools.com/api/films/${number}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log('Error:', response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  console.log (film)
  const characters = film["characters"];

  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      if (response.statusCode !== 200) {
        console.log('Error:', response.statusCode);
        return;
      }

      const character = JSON.parse(body);
      console.log(character["name"]);
    });
  }
});
