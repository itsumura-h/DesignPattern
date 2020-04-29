import { lazy } from "dyo";
// import {createRouter}  from "dyo-router";
import createRouter  from "dyo-router";

const router = createRouter([
  {
    path: "/",
    component: lazy(() => import('./components/home').then(module => module.default)),
  },
  {
    path: "/page1",
    component: lazy(() => import('./components/page1').then(module => module.default)),
  },
]);
export default router;
