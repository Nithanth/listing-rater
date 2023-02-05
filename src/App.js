import './App.css';
import { Container } from '@mui/system';
import { useState, useCallback } from 'react';
import ResponsiveAppBar from './components/Navigation/navigationbar';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './home_page/home';
import About from './about_page/about';
import Generate from './generate_page/generate';
import Results from './results_page/results';

function App() {

  return (
    <Router>
      <div className="App">
        <ResponsiveAppBar />
        <div className='content'>
          <Routes>
            <Route exact path='/' element={<Home/>}/>
            <Route exact path='/generate' element={<Generate/>}/>
            <Route exact path='/results' element={<Results/>}/>
            <Route exact path='/about' element={<About/>}/>
          </Routes>
        </div>
      </div>
    </Router>
  )
}

export default App;