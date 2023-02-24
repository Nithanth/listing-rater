import './App.css';
import { Container } from '@mui/system';
import { useState, useCallback } from 'react';
import ResponsiveAppBar from './components/navigation/navigationbar';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Landing from './components/landing_page/landing';
import Generate from './components/generate_page/generate';
import DescriptionPage from './components/description_page/description_page';
import ImagePage from './components/image_page/image_page';
import Results from './components/results_page/results';
import Resources from './components/resources_page/resources_page';

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
            <Route exact path='/resources' element={<Resources/>}/>
          </Routes>
        </div>
      </div>
    </Router>
  )
}

export default App;