'use strict';

var _component = require('./component.js');

// const MyComponent = props => {
// 	return <p>{props.children}</p>
// }

ReactDOM.render(React.createElement(
	_component.MyComponent,
	null,
	'My component'
), document.getElementById('app'));