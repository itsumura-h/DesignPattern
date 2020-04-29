import {h, useState, useEffect} from 'dyo'

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
      <p><a href="/#!/page1">page1</a></p>
      <h1>{state}</h1>
      <input type="text" onInput={event => handleInput(event)}></input>
    </div>
  )
}
export default home
