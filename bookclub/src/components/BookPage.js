// BookPage.js
import React, { Component } from 'react';
import '../BookPage.css'; // Adjust the path if necessary
import { Button } from 'reactstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Row, Col} from 'reactstrap';

class BookPage extends Component {
  
  constructor(props) {
    super(props);
    this.state = {
      books: [],
      booklist: []
    };

    // bind
    this.postAddBookList = this.postAddBookList.bind(this);
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

  postAddBookList = (_bookID) => {

    console.log("BOOK_ID: " + _bookID);

    let url = 'http://localhost:5000/booklist/1'; // TODO temporarily using user 1
    
    let jData = JSON.stringify({
        book_id: _bookID
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
                console.log("setting post booklist state");

                return (response.json()) ;
            }
            else
                return ([ ["status ", response.status]]);
        }
        )//The promise response is returned, then we extract the json data
    .then ((jsonOutput) => //jsonOutput now has result of the data extraction, but don't need it in this case
            {
              // make new book for booklist
              const newBook = {"book_id": _bookID};

              this.fetchDataBookList();
              this.state.booklist.push(newBook);
              this.setState( {booklist: this.state.booklist} );  
            }
        )
    .catch((error) => 
        { console.log("BOOK_ID: " + _bookID)  
          console.log(error);
          this.fetchDataBookList();  
        } )
  }

  componentDidMount() {
    this.fetchDataBooks();
    this.fetchDataBookList();
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
                  <Button onClick={()=>this.postAddBookList(book.id)}>Add to MyList</Button>
                </Col>
            </Row>
          )
          }
          </Container>
      );
    }
}

export default BookPage;