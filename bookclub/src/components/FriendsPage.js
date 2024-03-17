// FriendsPage.js
import React, { Component } from 'react';
import FriendCard from './FriendCard';
import SuggestionCard from './SuggestionCard';
import '../FriendsPage.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Row, Col, Button} from 'reactstrap';


class FriendsPage extends Component {

  constructor(props) {
    super(props);
    this.state = {
      friends: [],
      user: 0, // // will figure this out
      potentialFriends: [],
      newFriendID: 0 // will figure this out
    };

    // bind
    this.postNewFriend = this.postNewFriend.bind(this);
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
    fetch('http://localhost:5000/friendactivity/1') // TODO temporarily using user 1
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

  updatePotentialFriends = (apiResponse) => {
    this.setState( {potentialFriends: apiResponse} );
  }

  fetchDataPotenitalFriends = () => {
    fetch('http://localhost:5000/addfriends/1') // TODO temporarily using user 1
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
                  this.updatePotentialFriends(jsonOutput);
              }
          )
    .catch((error) => 
            {console.log(error);
                this.updatePotentialFriends("");
            } )
  }

  postNewFriend = (_friendID) => {

    let url = 'http://localhost:5000/friend/1'; // TODO temporarily using user 1
    
    let jData = JSON.stringify({
        friend_id: _friendID
        });
    fetch(url,
        { method: 'POST',
        body: jData,
        headers: {
                "Content-type": "application/json; charset=UTF-8", 
                "Access-Control-Allow-Origin": "*"}        
        })
    .then(
        (response) => 
        {
            if (response.status === 200) {
                console.log("setting post friend state");

                return (response.json()) ;
            }
            else
                return ([ ["status ", response.status]]);
        }
        )//The promise response is returned, then we extract the json data
    .then ((jsonOutput) => //jsonOutput now has result of the data extraction, but don't need it in this case
            {
              // make new friend, to add to list
              const newFriend = {"friend_id":_friendID};

              this.fetchDataFriends();
              this.state.friends.push(newFriend);
              this.setState( {friends: this.state.friends} );  
              
              // remove from potential friends list
              this.setState( {
                potentialFriends: this.state.potentialFriends.filter(user => user.user_id != _friendID)
              } );
            }
        )
    .catch((error) => 
        {console.log(error);
          this.fetchDataFriends();        
        } )
  }

  componentDidMount() {
    this.fetchDataFriends();
    this.fetchDataPotenitalFriends();
  }

  render () {

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

      <Container style={{marginTop:50, marginLeft:1300, width:300, flex:1, flexDirection: 'column', justifyContent: 'flex-end'}} >

      <Row style={{border:'solid', borderColor:'lightgray'}}>
        <Col xs={12} md={12} lg={12} style={{backgroundColor: 'black', color:'white'}}>Suggested Friends</Col>
      </Row>

        {
        this.state.potentialFriends.map(potFriend=>
          <Row style={{border:'solid', borderColor:'lightgray'}} key={potFriend}>
              <Col xs={1} md={7} lg={7}>{potFriend.username}</Col>
              <Col xs={1} md={3} lg={3} style={{ backgroundColor:'white'}}>
                <Button onClick={()=>this.postNewFriend(potFriend.user_id)}>+</Button>       
              </Col>
          </Row>
        )
        }
      </Container>
      </div>
    );
  }
}

export default FriendsPage;