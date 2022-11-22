import React, { useState, useEffect } from 'react'
import { TextField, Button, Grid } from '@material-ui/core';
import axios from 'axios';
import Stock from './Stock';


const Search = () => {

  const [query, setQuery] = useState("");
  const [results, setResults] = useState("");


  const requestMoreResults = (range) => {
  }

  const handleSearch = (e) => {
    e.preventDefault();
    axios.get(`http://127.0.0.1:8000/api/stockwatch/search/${query}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    }).then ((res) => {
      console.log(res.data)
      setResults(res.data)
    })
  }





  return (
    <div>

    <TextField id="standard-basic" label="Search" 
    onChange={(e) => setQuery(e.target.value)}
    >{query}</TextField>
    <Button onClick={handleSearch} variant="contained" color="primary">
  Search
</Button>

<br/>
<br/>



    {results ? <Grid container spacing={4} direction={'column'} sx={{
        width: '90%',
      }}>
      {results.map((result) => (
        <Grid item xs={12}  key={result.id} sx={{
        width: '90%',
      }}>
        <Stock
          ticker={result.ticker}
          name={result.name}
          price={result.price}
          selectable = {true}
          select = {() => console.log('selected')}
        />
        </Grid>
      ))}


    </Grid> : <div>no results</div>}
    </div>
  )
}

export default Search