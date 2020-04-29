import { lazy } from "dyo";
import { createRouter } from "dyo-router";
// templates
import Home from "./components/view";

const router = createRouter([
  {
    path: "/",
    component: Home,
  },
  {
    path: "/page1",
    component: lazy(() => import('./components/page1').then(module => module.default)),
  },
  {
    path: "/page2",
    component: lazy(() => import('./components/page2').then(module => module.default)),
  },
  {
    path: "/page3",
    component: lazy(() => import('./components/page3').then(module => module.default)),
  },
]);
export default router;
