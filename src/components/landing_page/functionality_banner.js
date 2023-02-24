import CameraEnhanceOutlinedIcon from '@mui/icons-material/CameraEnhanceOutlined'
import CreateOutlinedIcon from '@mui/icons-material/CreateOutlined'
import AutoFixHighOutlinedIcon from '@mui/icons-material/AutoFixHighOutlined'
import AttractionsOutlinedIcon from '@mui/icons-material/AttractionsOutlined'
import OutdoorGrillOutlinedIcon from '@mui/icons-material/OutdoorGrillOutlined'
import ModeIcon from '@mui/icons-material/Mode'
import { Container } from '@mui/material'
import Typography from '@mui/material/Typography'
import Stack from '@mui/material/Stack'

function functionality_banner () {
  return (
    <Container maxWidth='false'>
      <Typography
        fontSize='30px'
        variant='h3'
        align='center'
        color='text.primary'
        paragraph
        sx={{ pt: 2 }}
      >
        Our AI-driven engine optimizes descriptions based on
      </Typography>

      <Stack
        sx={{ pt: 4 }}
        direction='row'
        spacing={10}
        justifyContent='center'
      >
        <Stack
          sx={{ pt: 4 }}
          direction='column'
          spacing={2}
          justifyContent='center'
          alignItems='center'
        >
          <Typography>Persuasive Appeal</Typography>
          <AutoFixHighOutlinedIcon fontSize='large'></AutoFixHighOutlinedIcon>
        </Stack>
        <Stack
          sx={{ pt: 4 }}
          direction='column'
          spacing={2}
          justifyContent='center'
          alignItems='center'
        >
          <Typography>Image Quality</Typography>
          <CameraEnhanceOutlinedIcon fontSize='large'></CameraEnhanceOutlinedIcon>
        </Stack>
        <Stack
          sx={{ pt: 4 }}
          direction='column'
          spacing={2}
          justifyContent='center'
          alignItems='center'
        >
          <Typography>Clarity</Typography>
          <CreateOutlinedIcon fontSize='large'></CreateOutlinedIcon>
        </Stack>

        <Stack
          sx={{ pt: 4 }}
          direction='column'
          spacing={2}
          justifyContent='center'
          alignItems='center'
        >
          <Typography>Local Attractions</Typography>
          <AttractionsOutlinedIcon fontSize='large'></AttractionsOutlinedIcon>
        </Stack>
        <Stack
          sx={{ pt: 4 }}
          direction='column'
          spacing={2}
          justifyContent='center'
          alignItems='center'
        >
          <Typography>Amenities</Typography>
          <OutdoorGrillOutlinedIcon fontSize='large'></OutdoorGrillOutlinedIcon>
        </Stack>
      </Stack>
    </Container>
  )
}

export default functionality_banner
