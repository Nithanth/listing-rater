import './App.css';
import { Container } from '@mui/system';
import { TextField, Button } from '@mui/material';
import { useState, useCallback } from 'react';
import Dropzone from './components/Dropzone/dropzone';

function App() {
  const [description, setDescription] = useState('');
  const [images, setImages] = useState([]);

  const onDrop = useCallback(acceptedFiles => {
    acceptedFiles.map(file => {
      const reader = new FileReader();
      reader.onload = function (e) {
        setImages(prevState => [
          ...prevState,
          { id: 'a', src: e.target.result }
        ]);
      };
      reader.readAsDataURL(file);
      return file;
    });
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/add', {
      method: 'post',
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        description: description,
        images: images
      })
    }).then(() => {
      console.log("new object posted")
    })
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>AirBNB Listing Rater</h1>
        <div className="App">
          <p>
            Enter description
          </p>
          <Container >
            <TextField
              id="full-width-text-field"
              type="search"
              variant="filled"
              multiline
              rows={6}
              maxWidth='lg'
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              style={{ width: 600 }}
            />
          </Container>
        </div>
        <div className="App">
          <p>
            Upload images
          </p>
          <p>
          </p>
          <div className="App container mt-5" style={{ width: 600 }}>
            <Dropzone onDrop={onDrop}>
            </Dropzone>
          </div>
          <aside>
            <p style={{ fontSize: 23 }}> {images.length} Files Uploaded </p>
          </aside>
          <p>
          </p>
          <Button variant="contained" onClick={handleSubmit}>Rate my listing</Button>
        </div>
      </header>
    </div>
  );
}

export default App;