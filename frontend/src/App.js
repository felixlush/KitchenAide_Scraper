import React, { useState } from 'react';
import { Routes, Route, BrowserRouter, Navigate } from 'react-router-dom';
import Products from './pages/Products';
import Prices from './pages/Prices';
import Login from './pages/Login';
import ProductDetails from './pages/ProductDetails';
import Home from './pages/Home';
import Layout from './components/Layout';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = (credentials) => {
    console.log('Logged In With: ', credentials);
    setIsLoggedIn(true);
  };

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          {isLoggedIn ? (
            <>
              <Route index element={<Home />} />
              <Route path="/products" element={<Products />} />
              <Route path="/prices" element={<Prices />} />
            </>
          ) : (
            <Route path="/login" element={<Login onLogin={handleLogin} />} />
          )}
          {/* Redirect any other route to login if not logged in */}
          <Route path="*" element={<Navigate to={isLoggedIn ? "/" : "/login"} />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
