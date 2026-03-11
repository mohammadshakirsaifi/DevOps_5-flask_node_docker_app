const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
app.set('view engine', 'ejs');

// Parse form data
app.use(bodyParser.urlencoded({ extended: true }));

// Parse JSON (IMPORTANT)
app.use(express.json());

app.get('/', (req, res) => {
  res.render('index', { result: null });
});

app.post('/submit', async (req, res) => {
  try {
    const response = await axios.post(
      'http://backend:5000/submit',
      {
        name: req.body.name,
        email: req.body.email
      },
      {
        headers: { 'Content-Type': 'application/json' }
      }
    );

    res.render('index', { result: response.data });
  } catch (err) {
    console.error(err);
    res.render('index', { result: { error: 'Backend not reachable' } });
  }
});

app.listen(3000, () => {
  console.log('Frontend running on port 3000');
});
