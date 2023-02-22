import './description_page.css'
import { Container } from '@mui/system'
import { TextField, Button } from '@mui/material'
import { useState, useCallback } from 'react'
import Dropzone from '../components/Dropzone/dropzone'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import Typography from '@mui/material/Typography'
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

function DescriptionPage () {
  const [description, setDescription] = useState('')

  const handleSubmit = e => {
    e.preventDefault()
    fetch('/evaluate_description', {
      method: 'post',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        description: description,
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
        <div className='content'>
          <p>Enter description</p>
          <Container>
            <TextField
              id='full-width-text-field'
              type='search'
              variant='filled'
              multiline
              rows={6}
              maxWidth='lg'
              value={description}
              onChange={e => setDescription(e.target.value)}
              style={{ width: 600 }}
            />
          </Container>
        </div>
        <div>
          <ThemeProvider theme={button_theme}>
            <Link to={'/results'} style={{ textDecoration: 'none' }}>
              <Button
                variant='outlined'
                onClick={handleSubmit}
                size='large'
                sx={{ border: 1.5 }}
              >
                Rate my listing
              </Button>
            </Link>
          </ThemeProvider>
        </div>
      </header>
    </div>
  )
}

export default DescriptionPage
