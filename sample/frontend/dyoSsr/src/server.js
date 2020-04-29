// const express = require("express");
// const { render, h } = require("dyo");
// const path = require("path");
// const { App } = require("./app");
import express from 'express'
import {render, h} from 'dyo'
import path from 'path'
import router from './app.js'

const app = express();

const HTMLShell = (html) => `
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title> SSR Dyo App </title>
        </head>
        <body>
            <div id="app">${html}</div>
        </body>
    </html>`

app.use(express.static(path.join(__dirname, "dist")));
app.get('**', (req, res) => {
  let html = render(h('html', {}, router))
  res.send(HTMLShell(html))
})
app.listen(3000);

// const path = require('path')
// const express = require('express')
// const app = express(),
//             DIST_DIR = __dirname,
//             HTML_FILE = path.join(DIST_DIR, 'index.html')
// app.use(express.static(DIST_DIR))
// app.get('*', (req, res) => {
//     res.sendFile(HTML_FILE)
// })
// const PORT = process.env.PORT || 3000
// app.listen(PORT, () => {
//     console.log(`App listening to ${PORT}....`)
//     console.log('Press Ctrl+C to quit.')
// })