import { h } from "preact";
import { Link } from "preact-router/match";
import * as s from "./style.scss";

const Header=()=>{
  return (
    <div>
      <nav class="uk-navbar-container" uk-navbar>
        <div class={"uk-navbar-left "+s.overflow}>
          <div class="uk-navbar-item">
            <Link href="/" class={"uk-button uk-button-default "+s.link}>top</Link>
            <Link href="/profile" class={"uk-button uk-button-default "+s.link}>Me</Link>
            <Link href="/profile/john" class={"uk-button uk-button-default "+s.link}>john</Link>
            <Link href="/profile" class={"uk-button uk-button-default "+s.link}>Me</Link>
            <Link href="/profile/john" class={"uk-button uk-button-default "+s.link}>john</Link>
            <Link href="/profile" class={"uk-button uk-button-default "+s.link}>Me</Link>
            <Link href="/profile/john" class={"uk-button uk-button-default "+s.link}>john</Link>
            <Link href="/profile" class={"uk-button uk-button-default "+s.link}>Me</Link>
            <Link href="/profile/john" class={"uk-button uk-button-default "+s.link}>john</Link>
            <Link href="/profile" class={"uk-button uk-button-default "+s.link}>Me</Link>
            <Link href="/profile/john" class={"uk-button uk-button-default "+s.link}>john</Link>
            <Link href="/profile" class={"uk-button uk-button-default "+s.link}>Me</Link>
            <Link href="/profile/john" class={"uk-button uk-button-default "+s.link}>john</Link>
            <Link href="/profile" class={"uk-button uk-button-default "+s.link}>Me</Link>
            <Link href="/profile/john" class={"uk-button uk-button-default "+s.link}>john</Link>
          </div>
        </div>
      </nav>
    </div>
  );
};

export default Header;
