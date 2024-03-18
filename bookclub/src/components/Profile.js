// Profile.js
import React, { Component } from 'react';
import '../BookPage.css'; // Adjust the path if necessary
import { Button } from 'reactstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Row, Col, Card, CardText, CardHeader, CardBody} from 'reactstrap';
import EditModal from './EditModal';


class Profile extends Component {
  
    constructor(props) {
        super(props);
        this.state = {
            profile: [],
            showEditModal: false,
            booklist: []
        };
    
        //binds
        this.editProfile = this.editProfile.bind(this);
    }

      /**
     * update data given the api response
     * @param {*} apiResponse 
     */
    updateDataProfile = (apiResponse) => {
        this.setState( {profile: apiResponse} );
        console.log("PROFILE: " + apiResponse);
    }

    /**
     * Get all profile and their information
     */
    fetchDataProfile = () => {
        fetch('http://localhost:5000/user/1') // Temporarily using user 1
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
                        this.updateDataProfile(jsonOutput);
                    }
                )
        .catch((error) => 
                {console.log(error);
                    this.updateDataProfile("");
                } )
    }

    /**
     * update data given the api response
     * @param {*} apiResponse 
     */
    updateBookList = (apiResponse) => {
    this.setState( {booklist: apiResponse} );
    }

    /**
     * Get booklist
     */
    fetchDataBookList = () => {
    fetch('http://localhost:5000/booklist/1') // TODO temporarily using user 1
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
                    this.updateBookList(jsonOutput);
                }
            )
    .catch((error) => 
            {console.log(error);
                this.updateBookList("");
            } )
    }


    componentDidMount() {
        this.fetchDataProfile();
        this.fetchDataBookList();
    }


  
    /**
     * Edit profile based on body params
     * @param {*} _username 
     * @param {*} _password 
     * @param {*} _email 
     */
    editProfile = (_username, _password, _email) => {

    // check to see if any are null, if so, then use the previous data
    if (_username === undefined) {
        _username = this.state.profile[0].username;
    }

    if (_password === undefined) {
        _password = this.state.profile[0].password;  
    }

    if (_email === undefined) {
        _email = this.state.profile[0].email;   
    }

    let url = 'http://localhost:5000/user/1';

    console.log('url: ' + url);

    let jData = JSON.stringify({
        username: _username,
        password: _password,
        email: _email
        });
    fetch(url,
        { method: 'PUT',
        body: jData,
        headers: {"Content-type": "application/json; charset=UTF-8", 
                    "Access-Control-Allow-Origin": "*"}        
        })
    .then(
        (response) => 
        {
            if (response.status === 200) {
                return (response.json()) ;
            }
            else
                return ([ ["status ", response.status]]);
        }
        )//The promise response is returned, then we extract the json data
    .then ((jsonOutput) => //jsonOutput now has result of the data extraction, but don't need it in this case
            {
                this.fetchDataProfile();
            }
        )
    .catch((error) => 
        {console.log(error);
        this.fetchDataProfile();
        } )

    }

    closeEditModal = () => {
        this.setState( {showEditModal: false} );
    }

    openEditModal = () => {
        this.setState ( {showEditModal: true} );
    }

    editedProfile = (_username, _password, _email) => {
        this.closeEditModal();
        this.editProfile(_username, _password, _email);
    }

    render () {

        const user = this.state.profile[0];

        return (
            <div>
                <Card style={{marginTop:50, marginLeft:400, width:300}}>    
                    <CardHeader>Profile</CardHeader>
                    <CardBody>
                    {
                        this.state.profile.map(user=>
                            <CardText>username: {user.username}</CardText>
                        )
                    }
                    {
                        this.state.profile.map(user=>
                            <CardText>password: {user.password}</CardText>
                        )
                    }
                    {
                        this.state.profile.map(user=>
                            <CardText>email: {user.email}</CardText>
                        )
                    }

                    <Button onClick={()=>this.openEditModal(user)}>Edit</Button>

                    <EditModal data={this.state.profile[0]} cancel={this.closeEditModal} editing={this.editProfile}
                               showHide={this.state.showEditModal}/>

                    </CardBody>
                </Card>

                <Container style={{marginTop:50, marginLeft:200, width:1000}}>

                <Row style={{border:'solid', borderColor:'lightgray'}}>
                    <Col xs={12} md={12} lg={12} style={{backgroundColor: 'lightblue', color:'black'}}>My Book List</Col>
                </Row>

                <Row style={{border:'solid', borderColor:'lightgray'}}>
                    <Col xs={4} md={4} lg={4} style={{backgroundColor: 'black', color:'white'}}>Title</Col>
                    <Col xs={4} md={4} lg={4} style={{backgroundColor: 'black', color:'white'}}>Genre</Col>
                    <Col xs={4} md={4} lg={4} style={{backgroundColor: 'black', color:'white'}}>Author</Col>
                </Row>

                {
                this.state.booklist.map(book=>
                <Row style={{border:'solid', borderColor:'lightgray'}} key={book}>
                    <Col xs={4} md={4} lg={4}>{book.book_title}</Col>
                    <Col xs={4} md={4} lg={4}>{book.genre}</Col>
                    <Col xs={4} md={4} lg={4}>{book.author}</Col>
                </Row>
                )
                }
                </Container>
            </div>

        );
    }
}

export default Profile;

{/* <EditModal data={this.state.profile[0]} cancel={this.closeEditModal} editing={this.editProfile}
                               defaultUsername={this.state.profile[0][1]} defaultPassword={this.state.profile[0][2]}
                               defaultEmail={this.state.profile[0][3]} showHide={this.state.showEditModal}/> */}