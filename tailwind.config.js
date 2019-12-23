module.exports = {
  theme: {
    backgroundColor: theme => ({
      ...theme('colors'),
      backdrop: 'rgba(37,36,40,0.8)'
    }),
    extend: {
      width: {
        '3/7': '42.8571429%',
      },
      margin: {
        '3/7': '42.8571429%',
      },
      letterSpacing: {
        '2x-widest': '.4em',
      },
      zIndex: {
      '-10': '-10',
      }
    }
  },
  variants: {
    opacity: ['hover', 'group-hover'],
  },
}
