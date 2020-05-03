import { FunctionalComponent, h } from "preact";
import { Route, Router, RouterOnChangeArgs } from "preact-router";

import Home from "../routes/home";
import Profile from "../routes/profile";
import NotFoundPage from '../routes/notfound';
import Header from "./header";
import Sidebar from "./sidebar";

import 'uikit'
import 'uikit/dist/css/uikit.min.css'


// eslint-disable-next-line @typescript-eslint/no-explicit-any
if ((module as any).hot) {
    // tslint:disable-next-line:no-var-requires
    require("preact/debug");
}

const App: FunctionalComponent = () => {
    let currentUrl: string;
    const handleRoute = (e: RouterOnChangeArgs) => {
        currentUrl = e.url;
    };

    return (
        <div id="app">
            <Header />
            <div uk-grid>
              <div class="uk-width-1-5">
                <Sidebar/>
              </div>
              <div class="uk-width-4-5">
                <Router onChange={handleRoute}>
                  <Route path="/" component={Home} />
                  <Route path="/profile/" component={Profile} user="me" />
                  <Route path="/profile/:user" component={Profile} />
                  <NotFoundPage default />
                </Router>
              </div>
            </div>
        </div>
    );
};

export default App;
