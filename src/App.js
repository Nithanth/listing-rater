import './App.css';
import { Container } from '@mui/system';
import { useState, useCallback } from 'react';
import ResponsiveAppBar from './components/Navigation/navigationbar';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import About from './about_page/about';
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
            <Route exact path='/' element={<About/>}/>
            <Route exact path='/description' element={<DescriptionPage/>}/>
            <Route exact path='/images' element={<ImagePage/>}/>z
            <Route exact path='/about' element={<About/>}/>
          </Routes>
        </div>
      </div>
    </Router>
  )
}

export default App;