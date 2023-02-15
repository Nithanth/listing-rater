import * as React from 'react'
import Card from '@mui/material/Card'
import CardActions from '@mui/material/CardActions'
import CardContent from '@mui/material/CardContent'
import CardMedia from '@mui/material/CardMedia'
import Button from '@mui/material/Button'
import Typography from '@mui/material/Typography'
import HelpOutlineIcon from '@mui/icons-material/HelpOutline'
import AlertDialog from './readability_dialogue'

export default function ReadabilityCard () {
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardContent style={{ backgroundColor: '#d1ac90' }}>
        <Typography gutterBottom variant='h4' component='div'>
          Readability Score
        </Typography>
        <Typography gutterBottom variant='h5' component='div'>
          72.42
        </Typography>
        <Typography gutterBottom variant='h5' component='div'>
          Fairly easy to read
        </Typography>
      </CardContent>
      <CardActions>
        <Button size='small'>
          <AlertDialog style={{color:'#d1ac90'}}></AlertDialog>
        </Button>
      </CardActions>
    </Card>
  )
}
