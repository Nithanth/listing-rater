import './App.css';
import { Container } from '@mui/system';
import { useState, useCallback } from 'react';
import ResponsiveAppBar from './components/Navigation/navigationbar';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Landing from './landing/landing';
import Generate from './generate_page/generate';
import DescriptionPage from './description_page/description_page';
import ImagePage from './image_page/image_page';
import Results from './results_page/results';

function App() {

  return (
    <Router>
      <div className="App">
        <ResponsiveAppBar />
        <div className='content'>
          <Routes>
            <Route exact path='/' element={<Landing/>}/>
            <Route exact path='/description' element={<DescriptionPage/>}/>
            <Route exact path='/images' element={<ImagePage/>}/>
            <Route exact path='/generate' element={<Generate/>}/>
          </Routes>
        </div>
      </div>
    </Router>
  )
}

export default App;