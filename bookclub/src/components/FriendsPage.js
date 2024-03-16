// FriendsPage.js
import React, { Component } from 'react';
import FriendCard from './FriendCard';
import SuggestionCard from './SuggestionCard';
import '../FriendsPage.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Row, Col} from 'reactstrap';


class FriendsPage extends Component {

  // const friendsList = [
  //   { name: "Alice", lastMessage: "2" },
  //   { name: "Bob", lastMessage: "5" },
  // ];

  constructor(props) {
    super(props);
    this.state = {
      friends: []
    };
  }

    /**
   * update data given the api response
   * @param {*} apiResponse 
   */
    updateFriendsActivity = (apiResponse) => {
      this.setState( {friends: apiResponse} );
    }

    /**
   * Get all friends and their information
   */
    fetchDataFriends = () => {
      fetch('http://localhost:5000/friendactivity/1')
      .then(
          (response) => 
          {
              if (response.status === 200)
              {
                return (response.json()) ;
              }
              else
              {
                  console.log("HTTP error:" + response.status + ":" +  response.statusText);
                  return ([ ["status ", response.status]]);
              }
          }
          )//The promise response is returned, then we extract the json data
      .then ((jsonOutput) => //jsonOutput now has result of the data extraction
                {
                    this.updateFriendsActivity(jsonOutput);
                }
            )
      .catch((error) => 
              {console.log(error);
                  this.updateFriendsActivity("");
              } )
    }

  componentDidMount() {
    this.fetchDataFriends();
  }

  render () {

    const suggestedFriends = [
      { name: "Charlie" },
      { name: "Dave" },
    ];

    return (
      <div className="friends-list">
      <Container style={{marginTop:50, marginLeft:50}}>

      <Row style={{border:'solid', borderColor:'lightgray'}}>
          <Col xs={1} md={2} lg={2} style={{backgroundColor: 'black', color:'white'}}>Friend</Col>
          <Col xs={1} md={4} lg={4} style={{backgroundColor: 'black', color:'white'}}>Title</Col>
          <Col xs={1} md={3} lg={3} style={{backgroundColor: 'black', color:'white'}}>Author</Col>
          <Col xs={1} md={3} lg={3} style={{backgroundColor: 'black', color:'white'}}>Genre</Col>
      </Row>

      {/* new row per friend */}
      {
      this.state.friends.map(friend=>
        <Row style={{border:'solid', borderColor:'lightgray'}} key={friend}>
            <Col xs={1} md={2} lg={2}>{friend.username}</Col>
            <Col xs={1} md={4} lg={4}>{friend.title}</Col>
            <Col xs={1} md={3} lg={3}>{friend.author}</Col>
            <Col xs={1} md={3} lg={3}>{friend.genre}</Col>
        </Row>
      )
      }
      </Container>

      <div className="suggested-friends">
          <h2>Suggested for you</h2>
          {suggestedFriends.map((suggestion, index) => (
            <SuggestionCard key={index} name={suggestion.name} onAdd={() => console.log("Add friend")} />
          ))}
      </div>
      </div>
    );
  }
}

export default FriendsPage;
