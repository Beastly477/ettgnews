const flowbite = require('flowbite/plugin');

module.exports = {
  content: [
    './layouts/**/*.{html,js}',
    './content/**/*.{html,md}',
    './assets/**/*.{js,css}',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [flowbite],
}
