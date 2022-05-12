const express = require('express');
const morgan = require('morgan');
const http = require('http');
const bodyParser = require("body-parser");
const { MongoClient } = require("mongodb");

const hostname = "localhost";
const port = 3000;

const app = express();
app.use(bodyParser.json());

favorite_songs = []

data=[{"song_name":"Smells Like Teen Spirit","flim":"RRR","director":"Bee Gees","singer":"Michael Jackson"},
      {"song_name":"Billie Jean","flim":"JOKER","director":"Led Zeppelin","singer":"Bee Gees"},
      {"song_name":"I Will Survive","flim":"FINE","director":"Guns N’ Roses","singer":"Led Zeppelin"},
      {"song_name":"Whole Lotta Love","flim":"PK","director":"Kendrick Lamar","singer":"Gloria Gaynor"},
    ]
//Assign the appropriate route to the routes.
app.get("/create",async (req,res,next) => {
    const client = new MongoClient("mongodb://localhost:27017")
    await client.connect();
    const database = client.db("music");
    const collection = database.collection("songdetails");

    const result = await collection.insertMany(data);
    res.end(JSON.stringify(result));
})

app.get("/view",async (req,res,next) => {
    const client = new MongoClient("mongodb://localhost:27017")
    await client.connect();
    const database = client.db("music");
    const collection = database.collection("songdetails");

    const result = await collection.find();
    let items = []; 
    await result.forEach(function(doc){
      items.push(doc);
    });
    items.push({"count": items.length});
    res.end(JSON.stringify(items));
})

app.get("/director/:director",async (req,res,next) => {
    const client = new MongoClient("mongodb://localhost:27017")
    await client.connect();
    const database = client.db("music");
    const collection = database.collection("songdetails");
    var condition ={"director":req.params.director};
    console.log(condition);
    const result = await collection.find(condition);
    let items = [];
    await result.forEach(function(doc){
      items.push(doc);
    });
    items.push({"count": items.length});
    res.end(JSON.stringify(items));
})

app.get("/director/:director/singer/:singer",async (req,res,next) => {
    const client = new MongoClient("mongodb://localhost:27017")
    await client.connect();
    const database = client.db("music");
    const collection = database.collection("songdetails");
    const result = await collection.find({$and:[{"director":req.params.director},{"singer":req.params.singer}]});
    let items = [];
    await result.forEach(function(doc){
      items.push(doc);
    });
    items.push({"count": items.length});
    res.end(JSON.stringify(items));
})

app.get("/displayTable",async (req,res,next) => {
    const client = new MongoClient("mongodb://localhost:27017")
    await client.connect();
    const database = client.db("music");
    const collection = database.collection("songdetails");

    const result = await collection.find();
    let items = [];
    await result.forEach(function(doc){
      items.push("<tr><td>"+doc.song_name+"</td>"+"<td>"+doc.flim+"</td>"+"<td>"+doc.director+"</td>"+"<td>"+doc.singer+"</td>"+"</tr>");
    });

    var code ="<html><head> <style>body{background: gray; text-align: center;}table{border: none; border-collapse: collapse; background: peachpuff; text-align: center; margin: 2rem auto 0 auto; width: 900px; font-size: x-large;}table tr:first-child{font-weight: 700;}table tr td{border: 1px solid black; height: 45px;}</style></head><body> <h1>Students Database</h1> <table style='border:1px solid; background-color: aquamarine; text-align: center; margin:auto;'> <tr><td>Song Name</td><td>Film</td><td>Director</td><td>Singer</td><tr>"
    for(var i in items){
        code+=items[i];
    }
    code+="</table>"
    res.write(code);
    res.end();
})



app.use((req, res, next) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
  res.end('<html><body><h1>This is an Express Server</h1></body></html>');
});

//Create HTTP Server.
const server = http.createServer(app);

//Used to start the server on the given port. 
server.listen(port, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});