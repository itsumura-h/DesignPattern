import { h } from 'preact';
import { useState, useEffect } from 'preact/hooks';
import { Link } from 'preact-router/match';

const page1=()=>{
  return (
    <div>
      <h1>Page1</h1>
      <p><Link href="/">home</Link></p>
      <p><Link href="/page2">page2</Link></p>
    </div>
  )
}
export default page1
