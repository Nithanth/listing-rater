import { useState } from 'react'
import * as React from 'react'
import Button from '@mui/material/Button'
import CssBaseline from '@mui/material/CssBaseline'
import Grid from '@mui/material/Grid'
import Stack from '@mui/material/Stack'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Container from '@mui/material/Container'
import Link from '@mui/material/Link'
import TextField from '@mui/material/TextField'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import { Link as RouterLink } from 'react-router-dom'
import InputLabel from '@mui/material/InputLabel'
import MenuItem from '@mui/material/MenuItem'
import FormControl from '@mui/material/FormControl'
import Select, { SelectChangeEvent } from '@mui/material/Select'

function Copyright () {
  return (
    <Typography variant='body2' color='text.secondary' align='center'>
      <Link
        color='inherit'
        href='https://github.com/shahrishabh7'
        target='_blank'
      >
        GitHub
      </Link>{' '}
    </Typography>
  )
}

const theme = createTheme()

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
const page_theme = createTheme({
  status: {
    danger: '#e53e3e'
  },
  palette: {
    primary: {
      main: '#B38B6D'
    },
    secondary: {
      main: '#b87333'
      // #fff8e7
    }
  }
})

export default function Album () {
  const [address, setAddress] = useState('')
  const [amenities, setAmenities] = useState('')
  const [bathrooms, setBathrooms] = useState('')
  const [bedrooms, setBedrooms] = useState('')

  const handleChangeBath = (event: SelectChangeEvent) => {
    setBathrooms(event.target.value)
  }

  const handleChangeBed = (event: SelectChangeEvent) => {
    setBedrooms(event.target.value)
  }

  const handleSubmit = e => {
    e.preventDefault()
    fetch('/generate', {
      method: 'post',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        address: address
      })
    }).then(() => {
      console.log('new address posted')
    })
  }

  return (
    <ThemeProvider theme={page_theme}>
      <CssBaseline />
      <main>
        <body bgcolor='#fff8e7'>
          <Box
            sx={{
              bgcolor: '#e4cead',
              pt: 14,
              pb: 6,
              pl: 0,
              pr: 0
            }}
          >
            <Container maxWidth='me'>
              <p></p>
              <Typography
                component='h1'
                variant='h2'
                align='center'
                color='text.primary'
                gutterBottom
              >
                Let us generate you a description!
              </Typography>
            </Container>
            <Container maxWidth='me'>
              <Stack
                sx={{ pt: 4 }}
                direction='row'
                spacing={2}
                justifyContent='center'
              ></Stack>
            </Container>
          </Box>
          <Box
            sx={{
              bgcolor: '#fff8e7',
              pt: 2,
              pb: 12,
              pl: 0,
              pr: 0
            }}
          >
            <Container maxWidth='me'>
              <Container>
                <Typography
                  component='h1'
                  variant='h4'
                  align='center'
                  color='text.secondary'
                  gutterBottom
                >
                  Address
                </Typography>
                <TextField
                  id='full-width-text-field'
                  type='search'
                  variant='filled'
                  multiline
                  rows={2}
                  maxWidth='lg'
                  value={address}
                  onChange={e => setAddress(e.target.value)}
                  style={{ width: 600 }}
                />
              </Container>
              <Container sx={{ pt: 5 }}>
                <Stack
                  direction='row'
                  spacing={2}
                  justifyContent='center'
                >
                  <FormControl>
                    <InputLabel id='demo-simple-select-label'>
                      Bedroom Count
                    </InputLabel>
                    <Select
                      labelId='demo-simple-select-label'
                      id='demo-simple-select'
                      value={bedrooms}
                      label='bedrooms'
                      onChange={handleChangeBed}
                      style={{ width: 200 }}
                    >
                      <MenuItem value={1}>1</MenuItem>
                      <MenuItem value={2}>2</MenuItem>
                      <MenuItem value={3}>3</MenuItem>
                      <MenuItem value={4}>4</MenuItem>
                      <MenuItem value={5}>5</MenuItem>
                      <MenuItem value={6}>6</MenuItem>
                      <MenuItem value={7}>7</MenuItem>
                      <MenuItem value={8}>8</MenuItem>
                      <MenuItem value={9}>9</MenuItem>
                      <MenuItem value={10}>10</MenuItem>
                    </Select>
                  </FormControl>
                  <FormControl>
                    <InputLabel id='demo-simple-select-label'>
                      Bathroom Count
                    </InputLabel>
                    <Select
                      labelId='demo-simple-select-label'
                      id='demo-simple-select'
                      value={bathrooms}
                      label='bathrooms'
                      onChange={handleChangeBath}
                      style={{ width: 200 }}
                    >
                      <MenuItem value={1}>1</MenuItem>
                      <MenuItem value={2}>2</MenuItem>
                      <MenuItem value={3}>3</MenuItem>
                      <MenuItem value={4}>4</MenuItem>
                      <MenuItem value={5}>5</MenuItem>
                      <MenuItem value={6}>6</MenuItem>
                    </Select>
                  </FormControl>
                </Stack>
              </Container>
              <Container sx={{pt:5}}>
                <Typography
                  component='h1'
                  variant='h4'
                  align='center'
                  color='text.secondary'
                  gutterBottom
                >
                  Amenities
                </Typography>
                <TextField
                  id='full-width-text-field'
                  type='search'
                  variant='filled'
                  multiline
                  rows={5}
                  maxWidth='lg'
                  value={amenities}
                  onChange={e => setAmenities(e.target.value)}
                  style={{ width: 600 }}
                />
              </Container>
              <Container
                sx={{
                  bgcolor: '#fff8e7',
                  pt: 6,
                  pb: 0,
                  pl: 0,
                  pr: 0
                }}
              >
                <div>
                  <ThemeProvider theme={button_theme}>
                    <Button
                      variant='outlined'
                      onClick={handleSubmit}
                      size='large'
                      sx={{ border: 1.5 }}
                      style={{ textTransform: 'none' }}
                    >
                      Generate Description
                    </Button>
                  </ThemeProvider>
                </div>
              </Container>
            </Container>
          </Box>
        </body>
      </main>
      {/* Footer */}
      <Box sx={{ bgcolor: '#e4cead', p: 6 }} component='footer'>
        <Typography variant='h6' align='center' gutterBottom>
          Developed by:
        </Typography>
        <Typography
          variant='subtitle1'
          align='center'
          color='text.secondary'
          component='p'
        >
          Nithanth Ram & Rishabh Shah
        </Typography>
        <Copyright />
      </Box>
      {/* End footer */}
    </ThemeProvider>
  )
}
