module.exports = {
  theme: {
    letterSpacing: {
      '2x-widest': '.4em',
    },
    backgroundColor: theme => ({
      ...theme('colors'),
      backdrop: 'rgba(37,36,40,0.8)'
    })
  },
  variants: {
    opacity: ['hover', 'group-hover'],
  },
}
