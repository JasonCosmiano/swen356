// EditValues.js
import React, { Component } from 'react';
import '../BookPage.css'; // Adjust the path if necessary
import { Button } from 'reactstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {ModalBody, Label, Input, InputGroup, ModalFooter} from 'reactstrap';

class EditValues extends Component {
  
    constructor(props) {
        super(props);
        if (this.props.data===undefined) {
            this.state = {
                username: '',
                password: '',
                email: ''
            };
        }

        else {
            this.state = {
                username: this.props.data[1],
                password: this.props.data[2],
                email: this.props.data[3]
            }
        }

        // binds
        this.updateUsername = this.updateUsername.bind(this);
        this.updatePassword = this.updatePassword.bind(this);
        this.updateEmail = this.updateEmail.bind(this);
    }

    updateUsername = (e) => {
        this.setState({username: e.target.value});
    }

    updatePassword = (e) => {
        this.setState({password: e.target.value});
    }

    updateEmail = (e) => {
        this.setState({email: e.target.value});
    }

    toggle = () => {
        this.props.cancel();
    }

    saveChanges = () => {
        this.toggle();
        this.props.editing(this.state.username, this.state.password, this.state.email);
    }

    render () {

        return (
            <div>
            <ModalBody>
                <Label>Username</Label>
                <InputGroup>
                <Input type="text" placeholder="Username" onChange={this.updateUsername}/>
                </InputGroup>

                <Label>Password</Label>
                <InputGroup>
                <Input type="text" placeholder="Password" onChange={this.updatePassword}/>
                </InputGroup>

                <Label>Email</Label>
                <InputGroup>
                <Input type="text" placeholder="Email" onChange={this.updateEmail}/>
                </InputGroup>
            </ModalBody>

            <ModalFooter>
                <Button color="secondary" onClick={this.toggle}>Cancel</Button>
                <Button type="submit" color='primary' onClick={this.saveChanges}>Save</Button>
            </ModalFooter>
            </div>
        );
    }
}

export default EditValues;