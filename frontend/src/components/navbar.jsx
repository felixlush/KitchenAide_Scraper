import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="p-8 text-black">
      <div className="flex justify-start">
        <div className="space-x-4">
          <Link to="/" className="font-bold hover:text-gray-300">
            Home
          </Link>
          <Link to="/products" className="font-bold hover:text-gray-300">
            Products
          </Link>
          <Link to="/prices" className="font-bold hover:text-gray-300">
            Prices
          </Link>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;