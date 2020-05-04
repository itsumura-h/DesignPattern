import { h, FunctionalComponent } from 'preact'
import { Link } from "preact-router/match";

const Sidebar = () => {
  return (
    <ul class="uk-nav-primary uk-nav-parent-icon" uk-nav>
      <li>
        <Link href="/" activeClassName="uk-active" class="uk-button uk-button-default">home</Link>
        <Link href="/profile" activeClassName="uk-active" class="uk-button uk-button-default">Me</Link>
        <Link href="/profile/john" activeClassName="uk-active" class="uk-button uk-button-default">john</Link>
        <Link href="/profile" activeClassName="uk-active" class="uk-button uk-button-default">Me</Link>
        <Link href="/profile/john" activeClassName="uk-active" class="uk-button uk-button-default">john</Link>
        <Link href="/profile" activeClassName="uk-active" class="uk-button uk-button-default">Me</Link>
        <Link href="/profile/john" activeClassName="uk-active" class="uk-button uk-button-default">john</Link>
        <Link href="/profile" activeClassName="uk-active" class="uk-button uk-button-default">Me</Link>
        <Link href="/profile/john" activeClassName="uk-active" class="uk-button uk-button-default">john</Link>
        <Link href="/profile" activeClassName="uk-active" class="uk-button uk-button-default">Me</Link>
        <Link href="/profile/john" activeClassName="uk-active" class="uk-button uk-button-default">john</Link>
        <Link href="/profile" activeClassName="uk-active" class="uk-button uk-button-default">Me</Link>
        <Link href="/profile/john" activeClassName="uk-active" class="uk-button uk-button-default">john</Link>
        <Link href="/profile" activeClassName="uk-active" class="uk-button uk-button-default">Me</Link>
        <Link href="/profile/john" activeClassName="uk-active" class="uk-button uk-button-default">john</Link>
        <Link href="/profile" activeClassName="uk-active" class="uk-button uk-button-default">Me</Link>
        <Link href="/profile/john" activeClassName="uk-active" class="uk-button uk-button-default">john</Link>
      </li>
    </ul>
  )
}
export default Sidebar
