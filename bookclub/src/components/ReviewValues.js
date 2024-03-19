// ReviewValues.js
import React, { Component } from 'react';
import '../BookPage.css'; // Adjust the path if necessary
import { Button } from 'reactstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {ModalBody, Label, Input, InputGroup, ModalFooter} from 'reactstrap';

class ReviewValues extends Component {
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

    saveChanges = () => {
        this.toggle();
        this.props.posting(this.state.user_id, this.props.book_title, this.props.book_id, this.state.body, this.state.rating);
    }

    render () {


        return (
            <div>
            <ModalBody>
                <Label>Title</Label>
                <InputGroup>
                <Input type="text" placeholder="Title" onChange={this.setTitle}/>
                </InputGroup>

                <Label>Type review here...</Label>
                <InputGroup>
                <Input type="text" placeholder="Review" onChange={this.setBody}/>
                </InputGroup>

                <Label>Rating</Label>
                <InputGroup>
                <Input type="text" placeholder="Rating" onChange={this.setRating}/>
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

export default ReviewValues;
