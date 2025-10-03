// @ts-check

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'AIDR Bastion',
  tagline: 'A comprehensive GenAI protection system designed to safeguard against malicious prompts, injection attacks, and harmful content',
  favicon: 'img/favicon.ico',

  url: 'https://YOUR_USERNAME.github.io',
  baseUrl: '/AIDR-Bastion/',

  organizationName: '0xAIDR',
  projectName: 'AIDR-Bastion',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/0xAIDR/AIDR-Bastion/tree/main/docs/',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/social-card.jpg',
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: true,
        respectPrefersColorScheme: false,
      },
      navbar: {
        title: 'AIDR Bastion',
        logo: {
          alt: 'AIDR Bastion Logo',
          src: 'img/aidr-bastion-logo.png',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Documentation',
          },
          {
            href: 'https://github.com/0xAIDR/AIDR-Bastion',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Introduction',
                to: '/docs/intro',
              },
              {
                label: 'Installation',
                to: '/docs/installation',
              },
              {
                label: 'Configuration',
                to: '/docs/configuration',
              },
              {
                label: 'Usage',
                to: '/docs/usage',
              },
              {
                label: 'API Reference',
                to: '/docs/api-reference',
              },
              {
                label: 'Pipelines',
                to: '/docs/pipelines',
              },
              {
                label: 'Rule Management',
                to: '/docs/rule-management',
              },
              {
                label: 'Adding Custom Pipelines',
                to: '/docs/adding-custom-pipelines',
              },
              {
                label: 'Development',
                to: '/docs/development',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/0xAIDR/AIDR-Bastion',
              },
              {
                label: 'GitHub Issues',
                href: 'https://github.com/0xAIDR/AIDR-Bastion/issues',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'License',
                href: 'https://www.gnu.org/licenses/lgpl-3.0.html',
              },
            ],
          },
        ],
        copyright: `Built with Docusaurus. Licensed under LGPL-3.0.`,
      },
      prism: {
        theme: (() => {
          const {themes} = require('prism-react-renderer');
          return themes.github;
        })(),
        darkTheme: (() => {
          const {themes} = require('prism-react-renderer');
          return themes.dracula;
        })(),
        additionalLanguages: ['python', 'bash', 'json', 'yaml'],
      },
    }),
};

module.exports = config;

