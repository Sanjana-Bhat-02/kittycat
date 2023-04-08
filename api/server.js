const express = require('express');
const fs = require('fs')
const app = express();


function sendRandomItem(array) {
    const randomIndex = Math.floor(Math.random() * array.length);
    const randomItem = array[randomIndex];
    return randomItem
}

//route handler for GET requests to /fact
app.get('/fact', (req, res) => {
  fetch('https://raw.githubusercontent.com/vadimdemedes/cat-facts/master/cat-facts.json')
    .then(response => response.json())
    .then(data => {
        res.send(sendRandomItem(data));
    })
    .catch(error => {
      console.error(error);
      res.status(500).send('Internal server error');
    });
});

//route handler for GET requests to /picture
app.get('/picture', (req, res) => {
    fs.readFile('./pics.txt', 'utf-8', (err, data) => {
        if (err) {
            console.error(err);
            res.status(500).send('Internal server error');
            return;
        }
        const pictures = data.split("\n");
        res.send(sendRandomItem(pictures));
        
    })
})

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
