import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/AIDR-Bastion/docs',
    component: ComponentCreator('/AIDR-Bastion/docs', '6ce'),
    routes: [
      {
        path: '/AIDR-Bastion/docs',
        component: ComponentCreator('/AIDR-Bastion/docs', '555'),
        routes: [
          {
            path: '/AIDR-Bastion/docs',
            component: ComponentCreator('/AIDR-Bastion/docs', '80f'),
            routes: [
              {
                path: '/AIDR-Bastion/docs/',
                component: ComponentCreator('/AIDR-Bastion/docs/', '4d2'),
                exact: true
              },
              {
                path: '/AIDR-Bastion/docs/adding-custom-pipelines',
                component: ComponentCreator('/AIDR-Bastion/docs/adding-custom-pipelines', 'ba8'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/AIDR-Bastion/docs/api-reference',
                component: ComponentCreator('/AIDR-Bastion/docs/api-reference', '387'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/AIDR-Bastion/docs/built-with',
                component: ComponentCreator('/AIDR-Bastion/docs/built-with', 'a3d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/AIDR-Bastion/docs/configuration',
                component: ComponentCreator('/AIDR-Bastion/docs/configuration', '8ba'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/AIDR-Bastion/docs/development',
                component: ComponentCreator('/AIDR-Bastion/docs/development', 'cf0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/AIDR-Bastion/docs/installation',
                component: ComponentCreator('/AIDR-Bastion/docs/installation', 'aed'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/AIDR-Bastion/docs/intro',
                component: ComponentCreator('/AIDR-Bastion/docs/intro', '7f4'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/AIDR-Bastion/docs/license',
                component: ComponentCreator('/AIDR-Bastion/docs/license', 'a96'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/AIDR-Bastion/docs/pipelines',
                component: ComponentCreator('/AIDR-Bastion/docs/pipelines', 'b03'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/AIDR-Bastion/docs/rule-management',
                component: ComponentCreator('/AIDR-Bastion/docs/rule-management', 'b61'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/AIDR-Bastion/docs/to-do-list',
                component: ComponentCreator('/AIDR-Bastion/docs/to-do-list', '6af'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/AIDR-Bastion/docs/usage',
                component: ComponentCreator('/AIDR-Bastion/docs/usage', '5e0'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/AIDR-Bastion/',
    component: ComponentCreator('/AIDR-Bastion/', '171'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
