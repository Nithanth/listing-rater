import './App.css';
import { Container } from '@mui/system';
import { TextField, Button } from '@mui/material';
import FileUploadComponent from './components/imageUpload';
import { useState } from 'react';

function App() {
  // const [images, setImages] = useState(false);
  const [description, setDescription] = useState('');
  const [images,setImages] = useState([])

  const handleSubmit = (e) => {
    e.preventDefault();
    const info = {description};
    
    fetch('/add', {
      method: 'post',
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({
        description:description,
        images:
      })
    }).then(() => {
      console.log("new description added")
    })
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>AirBNB Listing Rater</h1>
        <div>
          <p>
            Enter your description
          </p>
          <Container maxWidth="sm">
            <TextField
              id="full-width-text-field"
              label="Description"
              type="search"
              variant="filled"
              size='large'
              multiline
              rows={7}
              fullWidth
              value={description}
              onChange={(e) => setDescription(e.target.value)}
            />
          </Container>
          <p>
            Upload your images
          </p>
          <p></p>
          <div className="App container mt-5">
            <FileUploadComponent id='uploaded-files' />
          </div>
          <Button variant="contained" onClick={handleSubmit}>Submit</Button>
        </div>
        <p>{description}</p>
      </header>
    </div>
  );
}

export default App;
