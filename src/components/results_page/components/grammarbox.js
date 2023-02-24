import { Grammarly, GrammarlyEditorPlugin } from '@grammarly/editor-sdk-react'
import { TextField } from '@mui/material'
import { useState, useCallback } from 'react'

let clientID = 'client_EEVPg27sThodxpJcK8tjRv'

export default function GrammarBox ({ description }) {
  const [text, setText] = useState(description)

  return (
    <Grammarly
      clientId={clientID}
      config={{
        activation: 'immediate'
      }}
    >
      <GrammarlyEditorPlugin clientId={clientID}>
        <TextField
          fullWidth='true'
          multiline
          id='full-width-text-field'
          rows={6}
          value={text}
          onChange={e => setText(e.target.value)}
        >
          {text}
        </TextField>
      </GrammarlyEditorPlugin>
    </Grammarly>
  )
}
