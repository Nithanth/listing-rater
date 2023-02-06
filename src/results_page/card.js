import * as React from 'react'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import CardMedia from '@mui/material/CardMedia'
import Typography from '@mui/material/Typography'
import { CardActionArea } from '@mui/material'
import Popper from './popper'

export default function ActionAreaCard ({ image, labels }) {
  return (
    <Card sx={{ height: 250, width: 200 }}>
      <CardMedia component='img' height='140' image={image} />
      <CardContent sx={{ pb: 10, pt: 8 }}>
        <Popper></Popper>
      </CardContent>
    </Card>
  )
}
