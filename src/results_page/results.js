import './results.css'
import { Container } from '@mui/system'
import { TextField, Button } from '@mui/material'
import { useState, useCallback } from 'react'
import Dropzone from '../components/Dropzone/dropzone'
import { createTheme, ThemeProvider } from '@mui/material/styles'
import Typography from '@mui/material/Typography'
import Box from '@mui/material/Box'
import Grid from '@mui/material/Grid'
import Card from './components/card'
import GrammarBox from './components/grammarbox'

const description =
  "Stylish, modern, and chic, two-bedroom, two bath home located on the border of the SOMA, Mission, and Hayes Valley district! The unit has a contemporary and inviting floor plan characterized with gorgeous wood floors, gourmet kitchen with stainless steel appliances, a comfortable living/dining area, and two significant bedrooms with plenty of natural light and are separated for privacy. Both bedrooms are spacious and complete with ample closet space, access to private decks that overlook the garden-like outdoor space, and there is a laundry closet for convenience. There is also an updated gym, common courtyard, grilling area, deeded storage, and available garage parking. Don't miss this wonderful home that is close to shopping, world renowned dining, cafes, public transportation, tech shuttles, HWY 101/280 and more!"

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

const cards = {
  idx: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  links: [
    'http://www.lisascreativedesigns.com/wp-content/uploads/2014/05/Staged-Living-Room-Before-3-600x397.jpg',
    'http://www.lisascreativedesigns.com/wp-content/uploads/2014/05/Staged-Living-Room-Before-3-600x397.jpg',
    'http://www.lisascreativedesigns.com/wp-content/uploads/2014/05/Staged-Living-Room-Before-3-600x397.jpg'
  ]
}

function Results () {
  return (
    <div className='Results'>
      <header>
        {/* <div class='spin'>
            <img src={logo} className="App-logo"/>
        </div> */}
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
              Beautiful property!
            </Typography>
          </Container>
          <Container maxWidth='me'>
            {'\n'}
            <Typography
              variant='h5'
              align='center'
              color='text.secondary'
              paragraph
            >
              Here's our two cents.
            </Typography>
          </Container>
          <Container
            maxWidth='me'
            sx={{
              bgcolor: '#f1e5d3',
              pt: 6,
              pb: 6,
              pl: 0,
              pr: 0
            }}
          >
            {'\n'}
            <Typography
              variant='h4'
              align='center'
              color='text.secondary'
              paragraph
              sx={{
                bgcolor: '#f1e5d3',
                pt: 0,
                pb: 6,
                pl: 0,
                pr: 0
              }}
            >
              Images
            </Typography>
            <Typography
              variant='h6'
              align='left'
              color='text.secondary'
              paragraph
              sx={{
                bgcolor: '#f1e5d3',
                pt: 0,
                pb: 6,
                pl: 0,
                pr: 0
              }}
            >
              The following images were flagged with issues:
            </Typography>
            <Box>
              {cards.idx?.map(card => (
                <Grid spacing={2} item key={card} sx={{ pt: 2 }}>
                  <Card image={cards.links[card]}></Card>
                </Grid>
              ))}
            </Box>
          </Container>
          <Container
            maxWidth='me'
            sx={{
              bgcolor: '#f1e5d3',
              pt: 6,
              pb: 6,
              pl: 0,
              pr: 0
            }}
          >
            {'\n'}
            <Typography
              variant='h4'
              align='center'
              color='text.secondary'
              paragraph
              sx={{
                bgcolor: '#f1e5d3',
                pt: 0,
                pb: 6,
                pl: 0,
                pr: 0
              }}
            >
              Description
            </Typography>
            <Typography
              variant='h6'
              align='left'
              color='text.secondary'
              paragraph
              sx={{
                bgcolor: '#f1e5d3',
                pt: 0,
                pb: 6,
                pl: 0,
                pr: 0
              }}
            >
              Grammar issues are flagged below, hover over underlined text to
              review issues and suggestions.
            </Typography>
            <Box sx={{ pt: 1, pb: 6, pl: 0, pr: 0 }}>
              <GrammarBox description={description}></GrammarBox>
            </Box>
          </Container>
        </Box>
      </header>
    </div>
  )
}

export default Results
