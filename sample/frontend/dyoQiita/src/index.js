import {render} from 'dyo'
import(/* webpackChunkName: "app.js" */ './app').then(module=>{
  const target = document.querySelector('main')
  render(module.default, target)
})
