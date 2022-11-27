import './App.css';
import { Container } from '@mui/system';
import { TextField } from '@mui/material';
import FileUploadComponent from './components/fileUpload.component';
import { useState, useEffect } from 'react';

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <h1>AirBNB Listing Rater</h1>
        <p>
          Enter your description
        </p>
        <Container maxWidth="sm">
          <form method='POST'>
            <TextField
              id="full-width-text-field"
              label="Description"
              type="search"
              variant="filled"
              size='large'
              multiline
              rows={7}
              maxRows={10}
              fullWidth
            />
          </form>
        </Container>
        <p>
          Upload your images
        </p>
        <div className="App container mt-5">
          <FileUploadComponent />
        </div>
      </header>
    </div>
  );
}

export default App;
