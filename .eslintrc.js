module.exports = {
  root: true,
  extends: [
    'eslint:recommended',
    'plugin:react/recommended'
  ],
  settings: {
    react: {
      version: 'detect'
    }
  },
  rules: {
    'react/prop-types': 0
  }
}