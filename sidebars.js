/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    {
      type: 'doc',
      id: 'intro',
      label: 'Introduction',
    },
    {
      type: 'doc',
      id: 'installation',
      label: 'Installation',
    },
    {
      type: 'doc',
      id: 'configuration',
      label: 'Configuration',
    },
    {
      type: 'doc',
      id: 'usage',
      label: 'Usage',
    },
    {
      type: 'doc',
      id: 'api-reference',
      label: 'API Reference',
    },
    {
      type: 'doc',
      id: 'pipelines',
      label: 'Pipelines',
    },
    {
      type: 'doc',
      id: 'rule-management',
      label: 'Rule Management and Customization',
    },
    {
      type: 'doc',
      id: 'adding-custom-pipelines',
      label: 'Adding Custom Pipelines',
    },
    {
      type: 'doc',
      id: 'development',
      label: 'Development',
    },
    {
      type: 'doc',
      id: 'license',
      label: 'License',
    },
    {
      type: 'doc',
      id: 'built-with',
      label: 'Built With',
    },
    {
      type: 'doc',
      id: 'to-do-list',
      label: 'TO-DO List',
    },
  ],
};

module.exports = sidebars;

