import React, { useEffect } from 'react'
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import { Routes, Route, Link, useNavigate } from "react-router-dom";

const Header = () => {
    return (
        <div>
            <Grid container spacing={2}>
                <Grid item>
                    <Link to='/home'>
                        <Button variant="contained" color="primary">
                            Home
                        </Button>
                    </Link>
                </Grid>
                <Grid item>
                    <Link to='/login'>
                        <Button variant="contained" color="primary">

                            Login
                        </Button>
                    </Link>
                </Grid>
                <Grid item>
                    <Link to='/signup'>

                        <Button variant="contained" color="primary">
                            Signup
                        </Button>
                    </Link>
                </Grid>
                <Grid item>
                    <Link to='/user'>
                        <Button variant="contained" color="primary">
                            User
                        </Button>
                    </Link>
                </Grid>
                <Grid item>
                    <Link to='/about'>
                        <Button variant="contained" color="primary">
                            About
                        </Button>
                    </Link>
                </Grid>
                <Grid item>
                    <Link to='/highscores'>
                        <Button variant="contained" color="primary">
                            High Scores
                        </Button>
                    </Link>
                </Grid>
                <Grid item>
                    <Link to='/logout'>
                        <Button variant="contained" color="primary">
                            Logout
                        </Button>
                    </Link>
                </Grid>
            </Grid>






        </div>
    )
}

export default Header