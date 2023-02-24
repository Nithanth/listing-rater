import * as React from 'react'
import Button from '@mui/material/Button'
import Card from '@mui/material/Card'
import CardActions from '@mui/material/CardActions'
import CardContent from '@mui/material/CardContent'
import CardMedia from '@mui/material/CardMedia'
import CssBaseline from '@mui/material/CssBaseline'
import Grid from '@mui/material/Grid'
import Stack from '@mui/material/Stack'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Container from '@mui/material/Container'
import Link from '@mui/material/Link'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import { Link as RouterLink } from 'react-router-dom'
import landingImage from './mountain_image.webp'
import myImage from './image.css'
import FunctionalityBanner from './functionality_banner'

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
                Boost your AirBNB Listing
              </Typography>
            </Container>
            <Typography
              variant='h5'
              align='center'
              color='text.secondary'
              paragraph
            >
              Hosts have spent years procuring the best listing practices to maximize bookings
            </Typography>
            {'\n'}
            <Typography
              variant='h5'
              align='center'
              color='text.secondary'
              paragraph
            >
              Luckily for you, we put it all in one place.
            </Typography>
          </Box>
          <Box
            sx={{
              bgcolor: '#fff8e7',
              pt: 2,
              pb: 8,
              pl: 0,
              pr: 0
            }}
          >
            <FunctionalityBanner></FunctionalityBanner>
          </Box>
          <Box
            sx={{
              bgcolor: '#e4cead',
              pt: 4,
              pb: 8,
              pl: 0,
              pr: 0
            }}
          >
            <Stack
              direction='row'
              spacing={20}
              justifyContent='center'
            >
              <Box>
                <Typography
                  variant='h5'
                  align='center'
                  color='text.secondary'
                  paragraph
                  sx={{ pt: 2 }}
                >
                  Grade and improve your listing:
                </Typography>
                <Stack
                  sx={{ pt: 4 }}
                  direction='row'
                  spacing={2}
                  justifyContent='center'
                >
                  <RouterLink
                    to={'/description'}
                    style={{ textDecoration: 'none' }}
                  >
                    <Button
                      variant='contained'
                      size='large'
                      autoCapitalize='false'
                      style={{ textTransform: 'none', fontSize: '20px' }}
                    >
                      Optimize Description
                    </Button>
                  </RouterLink>
                  <RouterLink to={'/images'} style={{ textDecoration: 'none' }}>
                    <Button
                      variant='contained'
                      size='large'
                      autoCapitalize='false'
                      style={{ textTransform: 'none', fontSize: '20px' }}
                    >
                      Optimize Images
                    </Button>
                  </RouterLink>
                </Stack>
              </Box>
              <Box>
                <Typography
                  variant='h5'
                  align='center'
                  color='text.secondary'
                  paragraph
                  sx={{ pt: 2, pb: 4 }}
                >
                  Generate custom description:
                </Typography>
                <RouterLink to={'/generate'} style={{ textDecoration: 'none' }}>
                  <Button
                    variant='contained'
                    size='large'
                    autoCapitalize='false'
                    style={{ textTransform: 'none', fontSize: '20px' }}
                  >
                    Generate
                  </Button>
                </RouterLink>
              </Box>
            </Stack>
          </Box>

          <Box>
            <div>
              <img src={landingImage} className='myImage' />
            </div>
          </Box>
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
        </body>
      </main>
    </ThemeProvider>
  )
}
