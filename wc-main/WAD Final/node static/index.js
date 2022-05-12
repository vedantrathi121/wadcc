const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json()); // body to json
app.use(bodyParser.urlencoded({ extended: false }));

// app.route("/").get((req,res) => { // 
//     res.send("<html><head><title>Nodejs Assignment</title></head><body><h1>Nodejs Assignment</h1><p>This is a static website</p></body></html>")
// })
app.route("/").get((req,res) => { // 
    res.sendFile('om.html', {root: __dirname })  // starting folder la root dir consider kar
})
app.listen(3000,()=>{
    console.log("Server started at post 3000")
}); // port listen

module.exports = app;


// enter url : get request
