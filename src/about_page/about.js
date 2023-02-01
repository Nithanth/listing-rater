import {Link} from 'react-router-dom';
import Album from "./album";
import { useState, useCallback } from 'react';
import ResponsiveAppBar from '../components/Navigation/navigationbar';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import { Container } from '@mui/material';

function About() {
  
    return (
      <Container maxWidth='false'>
      <Album></Album>
      </Container>
    );
  }
  
  export default About;