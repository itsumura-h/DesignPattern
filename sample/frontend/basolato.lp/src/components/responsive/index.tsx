import {h} from 'preact'

import Sidebar from "../sidebar";
import Header from "../header";
import Main from '../main'

import * as s from './style.scss'

const Responsive=()=>{
  return(
    <div class={s.top}>
      <div class={s.pc} uk-grid>
        <div class="uk-width-1-5">
          <Sidebar/>
        </div>
        <div class="uk-width-4-5">
         <Main />
        </div>
      </div>
      <div class={s.phone}>
        <Header />
        <Main />
      </div>
    </div>
  )
}
export default Responsive