import React, { useState, useEffect } from 'react'
import { TextField, Grid, Card, Paper, Button, Box } from '@material-ui/core';

const Stock = ({ ticker, amount, price, name, id, selectable, select }) => {
  const handleSelect = () => {
    console.log('selected')
    select()
  }
  return (
    <Box>
    <Paper elevation={1}
      >
      <Grid container spacing={4} elevation='4'
      >

        <Grid item xs={2} variant='contained'>
            {ticker ? <div>{ticker}</div> : <div></div>}
        </Grid>
        <Grid item xs={2} style={{ display: "flex", alignItems: "center", justifyContent:'center'}}>
            {amount ? <div>{amount}</div> : <div></div>}
        </Grid>
        <Grid item xs={2} style={{ display: "flex", alignItems: "center", justifyContent:'center'}}>
            {price ? <div>${price}</div> : <div></div>}
        </Grid>
        <Grid item xs={2} style={{ display: "flex", alignItems: "center", justifyContent:'center'}}>
            {name ? <div>{name}</div> : <div></div>}
        </Grid>
        <Grid item xs={2} style={{ display: "flex", alignItems: "center", justifyContent:'center'}}>
            {id ? <div>{id}</div> : <div></div>}
        </Grid>
        <Grid item xs={2} style={{ display: "flex", alignItems: "center", justifyContent:'center'}}>
            <div>
              {selectable ?
                <Button color='primary' variant='contained' onClick={handleSelect}>select</Button> : <div></div>}
            </div>
        </Grid>
      </Grid>
      </Paper>
    </Box>
  )
}

export default Stock