import { FunctionalComponent, h } from "preact";
// import { Route, Router, RouterOnChangeArgs } from "preact-router";

// import Home from "../routes/home";
// import Profile from "../routes/profile";
// import NotFoundPage from '../routes/notfound';
// import Sidebar from "./sidebar";
import Responsive from './responsive'

import 'uikit'
import 'uikit/dist/css/uikit.min.css'


// eslint-disable-next-line @typescript-eslint/no-explicit-any
if ((module as any).hot) {
    // tslint:disable-next-line:no-var-requires
    require("preact/debug");
}

const App: FunctionalComponent = () => {
    return (
      <div id="app">
        <Responsive />
      </div>
    );
};

export default App;
