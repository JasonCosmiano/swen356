// Review.js
import React, { Component } from 'react';
import '../BookPage.css'; // Adjust the path if necessary
import { Button } from 'reactstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Row, Col, Container} from 'reactstrap';
import ReviewModal from './ReviewModal';

class Review extends Component {
  
    constructor(props) {
        super(props);
        this.state = {
          books: [],
          reviews: [],
          showEditModal: false,
          selectedRow: {}
        };


        // bind
        this.postNewReview = this.postNewReview.bind(this);
      }
    
    /**
     * update data given the api response
     * @param {*} apiResponse 
     */
    updateBooks = (apiResponse) => {
        this.setState( {books: apiResponse} );
    }

    /**
     * Get all books and their information
     */
    fetchDataBooks = () => {
    fetch('http://localhost:5000/books') 
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
                    this.updateBooks(jsonOutput);
                }
            )
    .catch((error) => 
            {console.log(error);
                this.updateBooks("");
            } )
    }

    /**
     * update data given the api response
     * @param {*} apiResponse 
     */
    updateReviews = (apiResponse) => {
        this.setState( {reviews: apiResponse} );
    }

    /**
     * Get all reviews
     */
    fetchDataReviews = () => {
        fetch('http://localhost:5000/review') 
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
                        this.updateReviews(jsonOutput);
                    }
                )
        .catch((error) => 
                {console.log(error);
                    this.updateReviews("");
                } )
    }
    

    componentDidMount() {
        this.fetchDataBooks();
        this.fetchDataReviews();
    }

    postNewReview = (_user_id, _title, _book_id, _body, _rating) => {

        let url = 'http://localhost:5000/review'; 

        let jData = JSON.stringify({
            user_id: _user_id,
            title: _title,
            book_id: _book_id,
            body: _body,
            rating: _rating
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
                    console.log("setting post review state");

                    return (response.json()) ;
                }
                else
                    return ([ ["status ", response.status]]);
            }
            )//The promise response is returned, then we extract the json data
        .then ((jsonOutput) => //jsonOutput now has result of the data extraction, but don't need it in this case
                {
                    // make new review, to add to list
                    const newReview = {"user_id":_user_id, "title":_title, "book_id":_book_id, "body":_body, "rating":_rating};

                    this.fetchDataReviews();
                    this.state.reviews.push(newReview);
                    this.setState( {reviews: this.state.reviews} );  
                }
            )
        .catch((error) => 
            {console.log(error);
                this.fetchDataReviews();
            } )
    }

    closeEditModal = () => {
        this.setState( {showEditModal: false} );
    }

    openEditModal = (book) => {
        this.setState( { selectedRow: book } );
        this.setState ( {showEditModal: true} );
    }

    postedReview = (_user_id, _title, _book_id, _body, _rating) => {
        this.closeEditModal();
        this.postNewReview(_user_id, _title, _book_id, _body, _rating);
    }
    

    
    render () {

        return (
        
            <Container style={{marginTop:50, marginLeft:200}}>

            <Row style={{border:'solid', borderColor:'lightgray'}}>
                <Col xs={1} md={1} lg={1} style={{backgroundColor: 'black', color:'white'}}>Title</Col>
                <Col xs={1} md={1} lg={1} style={{backgroundColor: 'black', color:'white'}}>Genre</Col>
                <Col xs={1} md={1} lg={1} style={{backgroundColor: 'black', color:'white'}}>Author</Col>
                <Col xs={1} md={1} lg={1} style={{backgroundColor: 'black', color:'white'}}>Page Count</Col>
                <Col xs={1} md={1} lg={1} style={{backgroundColor: 'black', color:'white'}}>Publisher</Col>
                <Col xs={1} md={1} lg={1} style={{backgroundColor: 'black', color:'white'}}>Value</Col>
                <Col xs={1} md={5} lg={5} style={{backgroundColor: 'black', color:'white'}}>Description</Col>
                <Col xs={1} md={1} lg={1} style={{backgroundColor: 'black', color:'white'}}></Col>
            </Row>

            {
            
            this.state.books.map(book=>
            <Row style={{border:'solid', borderColor:'lightgray', height:200}} key={book}>
                <Col xs={1} md={1} lg={1}>{book.title}</Col>
                <Col xs={1} md={1} lg={1}>{book.genre}</Col>
                <Col xs={1} md={1} lg={1}>{book.author}</Col>
                <Col xs={1} md={1} lg={1}>{book.page_count}</Col>
                <Col xs={1} md={1} lg={1}>{book.publisher}</Col>
                <Col xs={1} md={1} lg={1}>{book.value}</Col>
                <Col xs={1} md={5} lg={5}>{book.description}</Col>
                <Col md={1} lg={1}>
                    <ReviewModal data={this.state.selectedRow} cancel={this.closeEditModal} posting={this.postedReview}
                                book_id={this.state.selectedRow.id} book_title={this.state.selectedRow.title}
                               showHide={this.state.showEditModal}/>
                    <Button onClick={()=>this.openEditModal(book)}>Review</Button>
                </Col>
            </Row>
            
            )

            
            }
            </Container>
        );
    }
}

export default Review;