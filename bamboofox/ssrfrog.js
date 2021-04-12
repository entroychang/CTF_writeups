const express = require("express");
const http = require("http");

const app = express();

app.get("/source", (req, res) => {
    return res.sendFile(__filename);
})
app.get('/', (req, res) => {
    const { url } = req.query;
    if (!url || typeof url !== 'string') console.log('index.html');

    // no duplicate characters in `url`
    if (url.length !== new Set(url).size) {
        console.log(new Set(url).size);
        console.log(url.length);
    }
    console.log(url);
    try {
        http.get(url, resp => {
            resp.setEncoding("utf-8");
            console.log(resp.statusCode);
            resp.statusCode === 200 ? resp.on('data', data => res.send(data)) : res.send(":(");
        }).on('error', () => res.send("WTF!"));
    } catch (error) {
        res.send(error);
        res.send("WTF?");
    }
});

app.listen(3000, '0.0.0.0');