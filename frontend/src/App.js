import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from 'react'
import { Routes, Route } from 'react-router-dom'
import Products from "./pages/Products"
import Prices from "./pages/Prices"
import ProductDetails from "./pages/ProductDetails"
import Home from "./pages/Home"


function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/products" element={<Products />} />
      <Route path="/products/:id" element={<ProductDetails />} />
      <Route path="/prices" element={<Prices />} />
    </Routes>
  );
}
export default App;
