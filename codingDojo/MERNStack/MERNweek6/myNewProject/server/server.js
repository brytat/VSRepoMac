const { response } = require('express');
const express = require('express');
const cors = require('cors')
const app = express();
app.use(cors())
require('./routes/person.routes')(app);
const port = 8000;


app.use(express.json());
app.use(express.urlencoded({extended: true}))

app.listen(port, () => console.log(`Listening to port: ${port}`) );