import { h } from 'preact';
import { useState, useEffect } from 'preact/hooks';
import { Link } from 'preact-router/match';

const page2 = () => {
  return (
    <div>
      <h1>Page2</h1>
      <p><Link href="/">home</Link></p>
      <p><Link href="/page1">page1</Link></p>
    </div>
  )
}
export default page2
