import * as React from 'react'
import Box from '@mui/material/Box'
import Popper from '@mui/material/Popper'
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined'
import Button from '@mui/material/Button';

export default function SimplePopper () {
  const [anchorEl, setAnchorEl] = React.useState(null)

  const handleClick = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(anchorEl ? null : event.currentTarget)
  }

  const open = Boolean(anchorEl)
  const id = open ? 'simple-popper' : undefined

  return (
    <div>
      <Button aria-describedby={id} onClick={handleClick} size='small' outlined='false'>
        <InfoOutlinedIcon></InfoOutlinedIcon>
      </Button>
      <Popper id={id} open={open} anchorEl={anchorEl}>
        <Box sx={{ border: 1, p: 1 }}>blurry</Box>
      </Popper>
    </div>
  )
}
