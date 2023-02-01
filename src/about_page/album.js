import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Button from '@mui/material/Button';
import CameraIcon from '@mui/icons-material/PhotoCamera';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Link from '@mui/material/Link';
import { createTheme, ThemeProvider } from '@mui/material/styles';

function Copyright() {
  return (
    <Typography variant="body2" color="text.secondary" align="center">
      <Link color="inherit" href="https://github.com/shahrishabh7">
        GitHub
      </Link>{' '}
    </Typography>
  );
}

const cards = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const theme = createTheme();
const page_theme = createTheme({
  status: {
    danger: '#e53e3e',
  },
  palette: {
    primary: {
      main: '#B38B6D',
    },
    secondary: {
      main: '#b87333',
      // #fff8e7
    },
  },
});

export default function Album() {
  return (
    <ThemeProvider theme={page_theme}>
      <CssBaseline />
      <main>
        <body bgcolor="#fff8e7">
          <Box
            sx={{
              bgcolor: '#e4cead',
              pt: 8,
              pb: 6,
            }}
          >
            <Container maxWidth="me">
              <p></p>
              <Typography
                component="h1"
                variant="h2"
                align="center"
                color="text.primary"
                gutterBottom
              >
                Optimize your Listing
              </Typography>
            </Container>
            <Container maxWidth="me">
              <Typography variant="h5" align="center" color="text.secondary" paragraph>
                The best hosts have figured out the nuances to the algorithm.
              </Typography>
              {'\n'}
              <Typography variant="h5" align="center" color="text.secondary" paragraph>
                Luckily for you, we bottled them up into one tool.
              </Typography>
              <Stack
                sx={{ pt: 4 }}
                direction="row"
                spacing={2}
                justifyContent="center"
              >
                <Button variant="contained" size="large" autoCapitalize='false'>Optimize</Button>
              </Stack>
            </Container>
          </Box>
          <Box
            sx={{
              bgcolor: '#fff8e7',
              pt: 8,
              pb: 2,
            }}
          >
            <Container maxWidth="me">
              <p></p>
              <Typography
                component="h1"
                variant="h3"
                align="center"
                color="text.primary"
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
              <Grid container spacing={4} style={{ paddingLeft: 300, paddingRight: 300 }}>
                {cards.map((card) => (
                  <Grid item key={card} xs={12} sm={6} md={4}>
                    <Card
                      sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}
                    >
                      <CardMedia
                        component="img"
                        sx={{
                          // 16:9
                          pt: '56.25%',
                        }}
                        image="https://source.unsplash.com/random"
                        alt="random"
                      />
                      <CardContent sx={{ flexGrow: 1 }}>
                        <Typography gutterBottom variant="h5" component="h2">
                          Heading
                        </Typography>
                        <Typography>
                          This is a media card. You can use this section to describe the
                          content.
                        </Typography>
                      </CardContent>
                      <CardActions>
                        <Button size="small">View</Button>
                        <Button size="small">Edit</Button>
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
      <Box sx={{ bgcolor: '#e4cead', p: 6 }} component="footer">
        <Typography variant="h6" align="center" gutterBottom>
          Developed by:
        </Typography>
        <Typography
          variant="subtitle1"
          align="center"
          color="text.secondary"
          component="p"
        >
          Rishabh Shah & Nithanth Ram
        </Typography>
        <Copyright />
      </Box>
      {/* End footer */}
    </ThemeProvider>
  );
}