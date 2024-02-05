import axios from 'axios';
import React from 'react';
import './App.css';


class App extends React.Component {
  state = { details: [], }

  componentDidMount() {

    let data;
    axios.get('http://localhost:8000')
    .then(res => {
      data = res.data;
      this.setState({
        details: data
      });
    })
    .catch( () => {"ERROR: Couldn't connect to server"});

}

render() {
  return (
    <div>
      <header className="header">Data Generated From Django</header>
      <header className="header">Technologies used for this project were React.js & Django Rest Framework</header>
      <hr></hr>
      {this.state.details.map((output, id) => (
        <div key={id}>
          <div>
            <h2 className="job">Position: {output.job}</h2>
            <h3 className="location">address: {output.location}</h3>
          </div>
        </div>
      ) )}
    </div>

  )
}

}
export default App;
