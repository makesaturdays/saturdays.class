
const MyComponent = props => {
	return <p>{props.children}</p>
}



ReactDOM.render(
  <MyComponent>My component</MyComponent>,
  document.getElementById('app')
)



