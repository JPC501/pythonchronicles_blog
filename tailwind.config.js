/** @type {import('tailwindcss').Config} */
module.exports = {
  mode:"jit",
  content: ['./blog/templates/*.html',
  './blog/static/js/.js', "./node_modules/flowbite/*.js"],
  
  theme: {
    extend: {
      borderWidth: {
        '1': '0.5px'
      },
      borderColor:{
        'pyborder':'#91bfc1'
      },
      colors:{
        'pygreen':'#3A8D91',
        'gold':'#D1C079',
        'blue-button-l':'#0177C2',
        'blue-button-r':'#19284A'

      }
    },
  },
  
  plugins: [require("flowbite/plugin")],
}

