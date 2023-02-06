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

const cards = {
  idx: [1, 2, 3, 4, 5, 6, 7, 8, 9],
  image_links: [
    'https://a0.muscache.com/im/pictures/miso/Hosting-31202365/original/702a8b4d-f58d-4b9f-a892-294c80c5daac.jpeg?im_w=1200',
    'https://a0.muscache.com/im/pictures/miso/Hosting-51743588/original/3d964fa7-5680-45e1-9c23-9f55507c5cf1.jpeg?im_w=1200',
    'https://a0.muscache.com/im/pictures/prohost-api/Hosting-639765392409094547/original/650a063f-96e6-44ce-9c9c-97689e5f5ed1.jpeg?im_w=720',
    'https://a0.muscache.com/im/pictures/prohost-api/Hosting-53612611/original/57bedfe1-1d6f-46a7-bfc6-df01553d4233.jpeg?im_w=720',
    'https://a0.muscache.com/im/pictures/82c577ee-3422-4fda-ae09-6716d76e8bef.jpg?im_w=1200',
    'https://a0.muscache.com/im/pictures/miso/Hosting-11818704/original/d7279902-a71b-4fbc-a711-3172286ab458.jpeg?im_w=1200',
    'https://a0.muscache.com/im/pictures/49732403/06cb9f75_original.jpg?im_w=1200',
    'https://a0.muscache.com/im/pictures/3ef2f54a-cb0b-4773-84ec-2089efe6b035.jpg?im_w=720',
    'https://a0.muscache.com/im/pictures/efc1b17b-d3a1-4346-92da-01fd971b6b35.jpg?im_w=720'
  ],
  titles: [
    'Whippoorwill Retreat Treehouse',
    'Log Cabin',
    'Private Beachfront Home',
    'Modern Beach Haven',
    'East Side Beehive',
    'East Sister Rock Island',
    'Mesa Earthship',
    'Luxury Cabin',
    'Stargazing Dome'
  ],
  locations: [
    'Trenton, GA',
    'Sevierville, TN',
    'Panama City Beach, FL',
    'Miramar Beach, FL',
    'Austin, TX',
    'Marathon, FL',
    'Taos, NM',
    'Broken Bow, OK',
    'Lake George, CO'
  ],
  listing_links: [
    'https://www.airbnb.com/rooms/31202365?adults=1&category_tag=Tag%3A8188&children=0&infants=0&search_mode=flex_destinations_search&check_in=2023-02-26&check_out=2023-03-03&previous_page_section_name=1000&federated_search_id=f6a9a5c5-22db-4828-8ea8-fac9ee34708f',
    'https://www.airbnb.com/rooms/51743588?adults=7&children=0&infants=0&pets=0&check_in=2023-02-02&check_out=2023-02-07&source_impression_id=p3_1675351823_4Mzvs1knoIftZYvE',
    'https://www.airbnb.com/rooms/639765392409094547?adults=11&children=5&infants=0&pets=0&check_in=2023-02-06&check_out=2023-02-11&source_impression_id=p3_1675352607_pBUtexN%2FX5FhASao',
    'https://www.airbnb.com/rooms/53612611?adults=11&category_tag=Tag%3A8528&children=5&infants=0&pets=0&search_mode=flex_destinations_search&check_in=2023-03-05&check_out=2023-03-10&source_impression_id=p3_1675354237_tM16k7CagNk8ZWOj',
    'https://www.airbnb.com/rooms/5337141?adults=1&category_tag=Tag%3A8186&children=0&infants=0&search_mode=flex_destinations_search&check_in=2023-02-05&check_out=2023-02-10&federated_search_id=b2387521-5347-42b6-a4a7-979cf69369a8&source_impression_id=p3_1675354341_ryKCrlAIj4vxlAbh',
    'https://www.airbnb.com/rooms/11818704?adults=1&category_tag=Tag%3A675&children=0&infants=0&search_mode=flex_destinations_search&check_in=2023-02-25&check_out=2023-03-04&federated_search_id=d51ccdd2-61bc-4017-b1cb-e98357608ba6&source_impression_id=p3_1675354506_OvZoZR2TXN8SWDuG',
    'https://www.airbnb.com/rooms/1762491?adults=1&category_tag=Tag%3A8174&children=0&infants=0&search_mode=flex_destinations_search&check_in=2023-05-07&check_out=2023-05-12&federated_search_id=ffa26abb-0e1f-4bf5-96af-8d9a516aa08e&source_impression_id=p3_1675354649_F2Ol2A8PCTM95KyN',
    'https://www.airbnb.com/rooms/47905773?adults=1&category_tag=Tag%3A8536&children=0&infants=0&search_mode=flex_destinations_search&check_in=2023-02-12&check_out=2023-02-17&federated_search_id=7431b71c-f9f0-4e38-bced-0bb877068c35&source_impression_id=p3_1675354881_EcKMVdJJJ2Csm15H',
    'https://www.airbnb.com/rooms/52362168?adults=1&category_tag=Tag%3A8173&children=0&infants=0&search_mode=flex_destinations_search&check_in=2023-05-20&check_out=2023-05-26&federated_search_id=4a393f88-992e-4aaf-bc1b-eaab49b96280&source_impression_id=p3_1675355130_PlEdpRtuLAV6xFz%2F'
  ]
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
                Optimize your AirBNB Listing
              </Typography>
            </Container>
            <Container maxWidth='me'>
              <Typography
                variant='h5'
                align='center'
                color='text.secondary'
                paragraph
              >
                Hosts have spent years procuring the best SEO practices
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
              <Stack
                sx={{ pt: 4 }}
                direction='row'
                spacing={2}
                justifyContent='center'
              >
                <RouterLink to={'/'} style={{ textDecoration: 'none' }}>
                  <Button
                    variant='contained'
                    size='large'
                    autoCapitalize='false'
                  >
                    Optimize
                  </Button>
                </RouterLink>
              </Stack>
            </Container>
          </Box>
          <Box
            sx={{
              bgcolor: '#fff8e7',
              pt: 8,
              pb: 2,
              pl: 0,
              pr: 0
            }}
          >
            <Container maxWidth='me'>
              <p></p>
              <Typography
                component='h1'
                variant='h3'
                align='center'
                color='text.primary'
                gutterBottom
              >
                Here are some of our favorite listings:
              </Typography>
            </Container>
          </Box>
          <Box
            sx={{
              bgcolor: '#fff8e7'
            }}
          >
            <Container sx={{ py: 8 }} maxWidth='false'>
              {/* End hero unit */}
              <Grid
                container
                spacing={4}
                style={{ paddingLeft: 300, paddingRight: 300 }}
              >
                {cards.idx.map(card => (
                  <Grid item key={card} xs={12}>
                      <Card
                        sx={{
                          maxWidth: 420,
                          height: '100%',
                          display: 'flex',
                          flexDirection: 'column'
                        }}
                      >
                        <CardMedia
                          height='500'
                          component='img'
                          sx={{
                            // 16:9
                            pt: '0%'
                          }}
                          image={cards.image_links[card - 1]}
                          alt='random'
                        />
                        <CardContent sx={{ flexGrow: 1 }}>
                          <Typography gutterBottom variant='h5' component='h2'>
                            {cards.titles[card - 1]}
                          </Typography>
                          <Typography>{cards.locations[card - 1]}</Typography>
                        </CardContent>
                        <CardActions>
                          <Button
                            size='small'
                            autoCapitalize='none'
                            href={cards.listing_links[card - 1]}
                            target='_blank'
                          >
                            View Listing
                          </Button>
                        </CardActions>
                      </Card>
                  </Grid>
                ))}
              </Grid>
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
