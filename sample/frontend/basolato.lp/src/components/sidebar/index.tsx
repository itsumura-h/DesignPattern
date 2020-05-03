import { h, FunctionalComponent } from 'preact'
import { Link } from "preact-router/match";

const Sidebar = () => {
  return (
    <ul class="uk-nav-primary uk-nav-parent-icon" uk-nav>
      <li class="uk-parent">
        <a href="#">Parent</a>
        <ul class="uk-nav-primary uk-nav-sub">
          <li><Link href="/" activeClassName="uk-active">home</Link></li>
          <li><Link href="/profile" activeClassName="uk-active">Me</Link></li>
          <li class="uk-parent"><Link href="/profile/john" activeClassName="uk-active">john</Link></li>
        </ul>
      </li>
      <li><a href="#">Item</a></li>
    </ul>
  )
}
export default Sidebar
