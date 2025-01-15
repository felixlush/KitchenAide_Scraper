import React, { useState, useEffect, useRef } from 'react';
import { Outlet } from 'react-router-dom';
import Navbar from './navbar';

function Layout() {
  const [height, setHeight] = useState('auto');
  const [width, setWidth] = useState('auto') // State to track the card height
  const contentRef = useRef(null); // Ref to measure the content height

  useEffect(() => {
    if (contentRef.current) {
      // Set the initial height based on content
      setHeight(`${contentRef.current.offsetHeight}px`);
    }
  }, []);

  useEffect(() => {
    const resizeObserver = new ResizeObserver(() => {
      if (contentRef.current) {
        setHeight(`${contentRef.current.offsetHeight}px`);
        setWidth(`${contentRef.current.offsetWidth}px`)
      }
    });

    if (contentRef.current) {
      resizeObserver.observe(contentRef.current);
    }

    return () => {
      if (contentRef.current) {
        resizeObserver.unobserve(contentRef.current);
      }
    };
  }, []);

  return (
    <div className="p-20 min-h-screen bg-hero-pattern bg-cover bg-center flex items-center justify-center">
      <div
        // style={{ height, width, minHeight: '500px', minWidth: '300px' }}
        className="bg-white shadow-xl p-8 transition-all duration-500 ease-in-out"
      >
        <Navbar />
        <div ref={contentRef}>
          <Outlet />
        </div>
      </div>
    </div>
  );
}

export default Layout;
