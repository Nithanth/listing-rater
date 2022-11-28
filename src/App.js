import './App.css';
import { Container } from '@mui/system';
import { TextField } from '@mui/material';
import FileUploadComponent from './components/fileUpload.component';
import { useState, useEffect } from 'react';
import Form from './components/form';

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <h1>AirBNB Listing Rater</h1>
        <Form className="App">
        </Form>
      </header>
    </div>
  );
}

export default App;
