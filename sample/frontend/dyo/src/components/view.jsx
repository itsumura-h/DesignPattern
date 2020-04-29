import {h, useState, useEffect} from 'dyo'

const Count=()=>{
  const [count, setCount] = useState(0)
  function click(){
    setCount(count+1)
  }
  return (
    <div>
      <button onClick={click}>add</button>
      <p>{count}</p>
    </div>
  )
}

const Message=()=>{
  const [msg, setMsg] = useState('')
  function input(e){
    setMsg(e.target.value)
  }
  return(
    <div>
      <input type="text" onInput={e=>input(e)}/>
      <p>{msg}</p>
    </div>
  )
}

const Home=()=>{
  const title = 'dyo'
  const list = [1,2,3]

  const call=()=>{
    alert('Hello')
  }

  return (
    <div>
      <h1>{title}</h1>
      <p><a href="/#!/page1">page1</a></p>
      <p><a href="/#!/page2">page2</a></p>
      <ul>
        {list.map(row=>{
          return <li style="color: #ff6600">{row}</li>
        })}
      </ul>
      <button onclick={call}>Hello</button>
      <div>
        <input type="text" onInput={e=>console.log(e.target.value)} />
      </div>
      <hr/>
      <div>
        <h2>useState</h2>
        <Count />
        <Message />
      </div>
      <hr/>
    </div>
  )
}
export default Home
