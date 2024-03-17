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
      books: []
    }
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

    componentDidMount() {
      this.fetchDataBooks();
    }

    render () {

      return (
          <Container style={{marginTop:50, marginLeft:50}}>
          {
          this.state.books.map(book=>
            <Row style={{border:'solid', borderColor:'lightgray'}} key={book}>
                <Col xs={1} md={1} lg={1}>{book.title}</Col>
                <Col xs={1} md={1} lg={1}>{book.genre}</Col>
                <Col xs={1} md={1} lg={1}>{book.author}</Col>
                <Col xs={1} md={1} lg={1}>{book.page_count}</Col>
                <Col xs={1} md={1} lg={1}>{book.publisher}</Col>
                <Col xs={1} md={1} lg={1}>{book.value}</Col>
                <Col xs={1} md={5} lg={5}>{book.description}</Col>
                <Col md={1} lg={1}>
                  <Button>Add to MyList</Button>
                </Col>
            </Row>
          )
          }
          </Container>
      );
    }
}

export default BookPage;