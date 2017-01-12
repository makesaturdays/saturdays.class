if (module.hot)
	module.hot.accept()


import '../styles/all.scss'

import React from 'react';
import ReactDOM from 'react-dom';

import { MyComponent } from './component.js'


// const MyComponent = props => {
// 	return <p>{props.children}</p>
// }

ReactDOM.render(
	<MyComponent>My component</MyComponent>,
	document.getElementById('app')
)



