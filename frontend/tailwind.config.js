/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.js" ,"./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        'hero-pattern': "url('/src/assets/hero-background.jpg')"
      },
      transitionProperty: {
        'width' : 'width'
      }
    },
  },
  plugins: [],
}

