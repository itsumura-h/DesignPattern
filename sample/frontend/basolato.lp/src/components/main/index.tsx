import {h} from 'preact'
import { Route, Router, RouterOnChangeArgs } from "preact-router";
import {Suspense, lazy} from 'preact/compat'

// import Home from '../../routes/home';
// const Top = lazy(()=>import('../../routes/top'))
import Profile from "../../routes/profile";
import NotFoundPage from '../../routes/notfound';

const Main=()=>{
  let currentUrl: string;
  const handleRoute = (e: RouterOnChangeArgs) => {
    currentUrl = e.url;
  };

  return(
    <Suspense fallback={<div>loading...</div>}>
      <Router onChange={handleRoute}>
        <Route path="/" component={lazy(()=>import('../../routes/top'))} />
        <Route path="/profile/" component={Profile} user="me" />
        <Route path="/profile/:user" component={Profile} />
        <NotFoundPage default />
      </Router>
    </Suspense>
  )
}
export default Main