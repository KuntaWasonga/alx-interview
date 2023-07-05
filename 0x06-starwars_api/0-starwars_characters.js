#!/usr/bin/node

const request = require('request');

// Extract the command-line argument
const number = process.argv[2];

// Check for a film
const url = `https://swapi-api.alx-tools.com/api/films/${number}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log('Error:', response.statusCode);
    return;
  }

  const characters = JSON.parse(body).characters;

  const charactersName = characters.map(
    url => new Promise((resolve, reject) => {
      request(url, (promiseErr, __, charactersReqBody) => {
        if (promiseErr) {
          reject(promiseErr);
        }
        resolve(JSON.parse(charactersReqBody).name);
      });
    }));

  Promise.all(charactersName)
    .then(names => console.log(names.join('\n')))
    .catch(allErr => console.log(allErr));
});
