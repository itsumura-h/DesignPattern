import express from 'express';
import { h } from 'preact';
import render from 'preact-render-to-string';
/** @jsx h */
import Index from './index'

// basic HTTP server via express:
const app = express();
app.listen(3000);

// on each request, render and return a component:
app.get('/:fox', (req, res) => {
	let html = render(Index);
	// send it back wrapped up as an HTML5 document:
	res.send(`<!DOCTYPE html><html><body>${html}</body></html>`);
});