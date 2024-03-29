import './image_page.css'
import { Container } from '@mui/system'
import { TextField, Button } from '@mui/material'
import { useState, useCallback } from 'react'
import Dropzone from './Dropzone/dropzone'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import Typography from '@mui/material/Typography'
import logo from './monocle_logo.png'
import Box from '@mui/material/Box'
import { Link } from 'react-router-dom'
import { v4 as uuidv4 } from 'uuid'

const button_theme = createTheme({
  status: {
    danger: '#e53e3e'
  },
  palette: {
    primary: {
      main: '#371d10'
    },
    secondary: {
      main: '#b87333'
    },
    background: {
      main: '#e4cead'
    }
  },
  typography: {
    fontSize: 28
  }
})

function ImagePage () {
  const [images, setImages] = useState([])

  const onDrop = useCallback(acceptedFiles => {
    acceptedFiles.map(file => {
      const imageId = uuidv4()
      const reader = new FileReader()
      reader.onload = function (e) {
        setImages(prevState => [
          ...prevState,
          { id: imageId, src: e.target.result }
        ])
      }
      reader.readAsDataURL(file)
      return file
    })
  }, [])

  const handleSubmit = e => {
    e.preventDefault()
    fetch('/evaluate_images', {
      method: 'post',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        images: images
      })
    })
      .then(response => {
        console.log('object posted')
        if (!response.ok) {
          throw new Error('Network response was not ok')
        }
        return response.json()
      })
      .then(data => {
        console.log('data received', data)
        if (!data && !data.result) {
          throw new Error('Response data is not valid')
        }
      })
      .catch(error => {
        // Handle any errors that occur during the request
        console.error(error)
      })
  }

  return (
    <div className='App'>
      <header className='App-header'>
        {/* <div class='spin'>
            <img src={logo} className="App-logo"/>
        </div> */}
        <h1>AirBNB Listing Rater</h1>
        <div className='App'>
          <p>Upload images</p>
          <p></p>
          <div className='App container mt-5' style={{ width: 600 }}>
            <Dropzone onDrop={onDrop}></Dropzone>
          </div>
          <aside>
            <p style={{ fontSize: 23 }}> {images.length} Files Uploaded </p>
          </aside>
          <p></p>
        </div>
        <div>
          <ThemeProvider theme={button_theme}>
            <Link to={'/results'} style={{ textDecoration: 'none' }}>
              <Button
                variant='outlined'
                onClick={handleSubmit}
                size='large'
                sx={{ border: 1.5 }}
                style={{ textTransform: 'none' }}
              >
                Submit
              </Button>
            </Link>
          </ThemeProvider>
        </div>
      </header>
    </div>
  )
}

export default ImagePage
