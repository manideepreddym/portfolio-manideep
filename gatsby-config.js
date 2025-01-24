const config = require('./src/config');

module.exports = {
  siteMetadata: {
    title: 'Manideep Reddy',
    description: 'Manideep Reddy is an AI Engineer specializing in production-grade machine learning systems and LLMs.',
    siteUrl: 'https://manideepreddym.github.io/portfolio-manideep',
    image: '/og.png',
    twitterUsername: '@manideepreddy',
  },
  plugins: [
    `gatsby-plugin-react-helmet`,
    `gatsby-plugin-styled-components`,
    `gatsby-plugin-image`,
    `gatsby-plugin-sharp`,
    `gatsby-transformer-sharp`,
    `gatsby-plugin-sitemap`,
    `gatsby-plugin-robots-txt`,
    {
      resolve: `gatsby-plugin-manifest`,
      options: {
        name: 'Manideep Reddy',
        short_name: 'Manideep',
        start_url: '/',
        background_color: config.colors.darkNavy,
        theme_color: config.colors.navy,
        display: 'minimal-ui',
        icon: 'src/images/logo.png',
      },
    },
    `gatsby-plugin-offline`,
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `images`,
        path: `${__dirname}/src/images`,
      },
    },
    {
      resolve: `gatsby-transformer-remark`,
      options: {
        plugins: [
          'gatsby-remark-external-links',
          {
            resolve: 'gatsby-remark-images',
            options: {
              maxWidth: 700,
              quality: 90
            },
          },
          'gatsby-remark-code-titles',
          {
            resolve: `gatsby-remark-prismjs`,
            options: {
              classPrefix: 'language-',
              showLineNumbers: false,
              noInlineHighlight: false
            },
          },
        ],
      },
    },
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `content`,
        path: `${__dirname}/content`,
      },
    }
  ],
};