import React, { Component } from 'react'
import { Container } from '@mui/system'
import { TextField } from '@mui/material'
import FileUploadComponent from './fileUpload.component'
import Button from '@mui/material/Button';

export default class Form extends Component {
    // handleSubmit {

    // }

    render() {
        return (
            <div>
                <p>
                    Enter your description
                </p>
                <Container maxWidth="sm">
                    <form method='POST' enctype='' onSubmit={this.handleSubmit}>
                        <TextField
                            id="full-width-text-field"
                            label="Description"
                            type="search"
                            variant="filled"
                            size='large'
                            multiline
                            rows={7}
                            maxRows={10}
                            fullWidth
                        />
                    </form>
                </Container>
                <p>
                    Upload your images
                </p>
                <div className="App container mt-5">
                    <FileUploadComponent id='uploaded-files' />
                </div>
                <p></p>
                <Button variant="contained">Submit</Button>
            </div>
        )
    }
}
