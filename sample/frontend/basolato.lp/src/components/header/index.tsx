import { FunctionalComponent, h } from "preact";
import { Link } from "preact-router/match";
import * as s from "./style.scss";

const Header: FunctionalComponent = () => {
  return (
    <div>
      {/* <header class={s.header}>
        <h1>Preact App</h1>
        <nav>
          <Link activeClassName={s.active} href="/">
            Home
              </Link>
          <Link activeClassName={s.active} href="/profile">
            Me
              </Link>
          <Link activeClassName={s.active} href="/profile/john">
            John
              </Link>
        </nav>
      </header> */}
      <nav class="uk-navbar-container" uk-navbar style={{backgroundColor: "#000"}}>
        <div class="uk-navbar-left">
          <ul class="uk-navbar-nav">
            <li><Link href="/" activeClassName={s.active}>home</Link></li>
            <li><Link href="/profile" activeClassName={s.active}>Me</Link></li>
            <li class="uk-parent"><Link href="/profile/john" activeClassName={s.active}>john</Link></li>
          </ul>
          <button class={"uk-button uk-button-default "+[s.orgButton]}>Button</button>
          <button class="uk-button uk-button-default" disabled>Disabled</button>
        </div>
      </nav>
    </div>


  );
};

export default Header;
