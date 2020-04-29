import { h } from 'preact';
import { useState, useEffect } from 'preact/hooks';
import { Link } from 'preact-router/match';

const home=()=>{
  const [state, setState] = useState('')

  useEffect(function(){
  	document.title = `Hello World`
  })

  function handleInput(event:Event):void {
    let target = event.target as HTMLInputElement
    setState(target.value)
  }

	return(
    <div>
      <h1>Home</h1>
      <p><Link href="/page1">page1</Link></p>
      <p><Link href="/page2">page2</Link></p>
      <h1>{state}</h1>
      <input type="text" onInput={event => handleInput(event)}></input>
    </div>
  )
}
export default home
