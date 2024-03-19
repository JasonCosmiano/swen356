// ReviewModal.js
import React, { Component } from 'react';
import '../BookPage.css'; // Adjust the path if necessary
import { Button } from 'reactstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Modal, ModalHeader} from 'reactstrap';
import ReviewValues from './ReviewValues';


class ReviewModal extends Component {
  
    constructor(props) {
        super(props);
        if (this.props.data===undefined) {
            this.state = {
                user_id: 1,
                title: '',
                body: '',
                rating: 1
            };
        }

        else {
            this.state = {
                user_id: 1,
                title: this.props.data[2],
                body: this.props.data[4],
                rating: this.props.data[5]
            }
        }

        // binds
        this.setUserId = this.setUserId.bind(this);
        this.setBookId = this.setBookId(this);
        this.setTitle = this.setTitle.bind(this);
        this.setBody = this.setBody.bind(this);
        this.setRating = this.setRating.bind(this);
    }

    setUserId = () => {
        this.setState({user_id: 1});
    }

    setBookId = () => {
        this.setState({user_id: this.props.book_id});
    }

    setTitle = () => {
        this.setState({title: this.props.book_title});
    }

    setBody = (e) => {
        this.setState({body: e.target.value});
    }

    setRating = (e) => {
        this.setState({rating: e.target.value});
    }

    toggle = () => {
        this.props.cancel();
    }

    render () {


        return (
            <Modal isOpen={this.props.showHide} toggle={this.toggle}>

            <ModalHeader toggle={this.toggle}>
                <div>{this.props.book_title}</div>
            </ModalHeader>

            <ReviewValues data={this.props.data} posting={this.props.posting} 
                        cancel={this.props.cancel} book_id={this.props.book_id} book_title={this.props.book_title}></ReviewValues>

            </Modal>
        );
    }
}

export default ReviewModal;
