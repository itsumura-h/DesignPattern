import { h, Component } from 'preact';
import { Router } from 'preact-router';
import AsyncRoute from 'preact-async-route'

// import Header from './header';

// Code-splitting is automated for routes
// import Home from '../routes/home';
// import Profile from '../routes/profile';

export default class App extends Component {
	
	/** Gets fired when the route changes.
	 *	@param {Object} event		"change" event from [preact-router](http://git.io/preact-router)
	 *	@param {string} event.url	The newly routed URL
	 */
	// handleRoute = e => {
	// 	this.currentUrl = e.url;
	// };

	render() {
		return (
			<div id="app">
        {/* <Router onChange={this.handleRoute}> */}
        <Router>
					<AsyncRoute path="/" getComponent={()=>import('./original/home').then(module=>module.default)}/>
					<AsyncRoute path="/page1" getComponent={()=>import('./original/page1').then(module=>module.default)}/>
					<AsyncRoute path="/page2" getComponent={()=>import('./original/page2').then(module=>module.default)}/>
				</Router>
			</div>
		);
	}
}
