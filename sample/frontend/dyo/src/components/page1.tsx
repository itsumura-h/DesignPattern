import {h, useState, useEffect} from 'dyo'

const Inside=():JSX.Element=>{
  const [input, setInput] = useState<string>("")
  const [list, setList] = useState<string[]>([])

  function onInput(e:Event):void{
    let target = e.target as HTMLInputElement
    setInput(target.value)
  }

  function add():void{
    if(input.length > 0){
      list.push(input)
      setList(list)
      setInput("")
    }
  }

  function remove():void{
    let newList = [...list]
    newList.shift()
    setList(newList)
  }

  return (
    <div>
      <input type="text" onInput={e=>onInput(e)} value={input}/>
      <p><button type="button" onClick={add}>add</button></p>
      <p><button type="button" onClick={remove}>remove</button></p>
      <ul>
        {list.map(row=>{
          return <li>{row}</li>
        })}
      </ul>
    </div>
  )
}

const Page1=():JSX.Element=>{
  return(
    <div>
      <h1>Page1</h1>
      <p><a href="/#!/">home</a></p>
      <p><a href="/#!/page2">page2</a></p>
      <Inside />
    </div>
  )
}
export default Page1