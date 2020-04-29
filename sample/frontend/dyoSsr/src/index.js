import http from 'http'
import {h, render} from 'dyo'

function Example (props) {
	return Promise.resolve(
    <h1>Hello</h1>
  )
}

// import router from './app.js'
http.createServer((req, res) => {
  // return render(h('html', {}, h(Example)), res)
  return render(h('html', {}, h(Example)), res)
  // return render(Promise.resolve(router), res)
}).listen(3000)