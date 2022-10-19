import React, { useState, useEffect } from 'react'
import { TextField, Grid, Card, Paper, box, Box, Button } from '@material-ui/core';
import { BrowserRouter, Route, Routes, Link } from "react-router-dom";


const Usernav = () => {


    return (
        <div>
            <Grid container spacing={3}>
                <Grid item xs={12}>
                <Link to='profile'>
                    <Button variant="contained" color="primary">
                    profile
                    </Button>
                    </Link>
                </Grid>
                <Grid item xs={12}>
                <Link to='search'>
                    <Button variant="contained" color="primary">
                    search
                    </Button>
                    </Link>
                </Grid>
                <Grid item xs={12}>
                <Link to='holdings'>
                    <Button variant="contained" color="primary">
                    holdings
                    </Button>
                    </Link>
                </Grid>
                <Grid item xs={12}>
                <Link to='watchlist'>
                    <Button variant="contained" color="primary">
                    watchlist
                    </Button>
                    </Link>
                </Grid>
                <Grid item xs={12}>
                <Link to='transactions'>
                    <Button variant="contained" color="primary">
                    transactions
                    </Button>
                    </Link>
                </Grid>
            </Grid>
        </div>
    )
}

export default Usernav