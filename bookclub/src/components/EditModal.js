// EditModal.js
import React, { Component } from 'react';
import '../BookPage.css'; // Adjust the path if necessary
import { Button } from 'reactstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Modal, ModalHeader} from 'reactstrap';
import EditValues from './EditValues';


class EditModal extends Component {
  
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

    render () {


        return (
            <Modal isOpen={this.props.showHide} toggle={this.toggle}>

            <ModalHeader toggle={this.toggle}>
                <div>Edit Profile</div>
            </ModalHeader>

            <EditValues data={this.props.data} editing={this.props.editing} 
                        cancel={this.props.cancel} id={this.props.id}></EditValues>

            </Modal>
        );
    }
}

export default EditModal;

{/* <EditValues data={this.props.data} defaultUsername={this.props.defaultUsername} 
defaultPassword={this.props.defaultPassword} defaultEmail={this.props.defaultEmail}
editing={this.props.editing} cancel={this.props.cancel} id={this.props.id}></EditValues> */}