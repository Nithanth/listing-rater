import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import MenuItem from '@mui/material/MenuItem';
import { Stack } from '@mui/material';
import CottageOutlinedIcon from '@mui/icons-material/CottageOutlined';

const pages = ['Home', 'About', 'Resources'];

const bar_theme = createTheme({
    status: {
        danger: '#e53e3e',
    },
    palette: {
        primary: {
            main: '#B38B6D',
        },
        secondary: {
            main: '#b87333',
        },
    },
});

export default function ButtonAppBar() {
    return (
        <Box sx={{ flexGrow: 1 }}>
            <ThemeProvider theme={bar_theme}>
                <AppBar
                    position="fixed"
                    color="primary"
                >
                    <Toolbar>
                        <Typography
                            sx={{
                                flexGrow: 1,
                                textAlign: "left"
                            }}
                        >
                            <IconButton
                                size="large"
                                edge="start"
                                color="inherit"
                                aria-label="menu"
                            >
                                <CottageOutlinedIcon />
                            </IconButton>
                        </Typography>
                        <Stack direction='row' spacing={1}>
                            {pages.map((page) => (
                                <MenuItem
                                    key={page}
                                    textAlign="right"
                                >
                                    <Typography textAlign="center" variant="h6">{page}</Typography>
                                </MenuItem>
                            ))}
                        </Stack>
                    </Toolbar>
                </AppBar>
            </ThemeProvider>
        </Box >
    );
}