// src/components/ReactionButtons.js
import React, { useState } from 'react'
import '../ReactionButtons.css';

const ReactionButtons = () => {
    const initialData = () => {
    fetch('http://localhost:5000/reactions')
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
      })
      .then ((results) => {
        setHeartCount(results['heart']);
        setThumbsUpCount(results['thumbsUp']);
        setThumbsDownCount(results['thumbsDown']);
        setCryingCount(results['crying']);
      }
      )
  }
  const [heartCount, setHeartCount] = useState((initialData))
  const [thumbsUpCount, setThumbsUpCount] = useState('')
  const [thumbsDownCount, setThumbsDownCount] = useState('')
  const [cryingCount, setCryingCount] = useState('')



  const onButtonClickHeart = () => {
    let jData = JSON.stringify({
      reaction : "heart"
      });
    fetch("http://localhost:5000/reactions", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
          },
        body: jData
    })
    .then(
      (response) => 
        {
            if (response.status === 200) {
                console.log("getting data");
                return (response.json()) ;
            }
            else
                return ([ ["status ", response.status]]);
        })
    .then(result => {
          setHeartCount(result)
      })
  }

  const onButtonClickThumbsUp = () => {
    let jData = JSON.stringify({
      reaction : "thumbsUp"
      });
    fetch("http://localhost:5000/reactions", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
          },
        body: jData
    })
    .then(
      (response) => 
        {
            if (response.status === 200) {
                console.log("getting data");
                return (response.json()) ;
            }
            else
                return ([ ["status ", response.status]]);
        })
    .then(result => {
          setThumbsUpCount(result)
      })
  }

  const onButtonClickThumbsDown = () => {
    let jData = JSON.stringify({
      reaction : "thumbsDown"
      });
    fetch("http://localhost:5000/reactions", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
          },
        body: jData
    })
    .then(
      (response) => 
        {
            if (response.status === 200) {
                console.log("getting data");
                return (response.json()) ;
            }
            else
                return ([ ["status ", response.status]]);
        })
    .then(result => {
          setThumbsDownCount(result)
      })
  }

  const onButtonClickCrying = () => {
    let jData = JSON.stringify({
      reaction : "crying"
      });
    fetch("http://localhost:5000/reactions", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
          },
        body: jData
    })
    .then(
      (response) => 
        {
            if (response.status === 200) {
                console.log("getting data");
                return (response.json()) ;
            }
            else
                return ([ ["status ", response.status]]);
        })
    .then(result => {
          setCryingCount(result)
      })
  }

return(
  <div className="reaction-buttons">
    <button onClick={onButtonClickHeart}>❤️<br></br>{heartCount}</button>
    <button onClick={onButtonClickThumbsUp}>👍<br></br>{thumbsUpCount}</button>
    <button onClick={onButtonClickThumbsDown}>👎<br></br>{thumbsDownCount}</button>
    <button onClick={onButtonClickCrying}>😭<br></br>{cryingCount}</button>
  </div>
)
}

export default ReactionButtons;
