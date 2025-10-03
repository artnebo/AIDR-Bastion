# AIDR Bastion Documentation Website

Official documentation website for AIDR Bastion - A comprehensive GenAI protection system.

## 🚀 Quick Start

### Installation

```bash
npm install
```

### Local Development

```bash
npm start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```bash
npm run build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

```bash
npm run deploy
```

## 📁 Project Structure

```
AIDR-Bastion-site/
├── docs/                      # Markdown documentation
│   ├── intro.md
│   ├── installation.md
│   ├── pipelines/
│   └── rules/
├── src/
│   ├── pages/                 # React pages
│   │   ├── index.tsx         # Homepage
│   │   └── index.module.css
│   └── css/                   # Global styles
│       └── custom.css
├── static/                    # Static assets
│   └── img/
├── docusaurus.config.js      # Site configuration
├── sidebars.js              # Sidebar navigation
└── package.json
```

## 🎨 Design Theme

### Cyberpunk Neon Style

This site features a custom cyberpunk-inspired design with:
- 🏰 **3D Logo**: Custom isometric fortress with neon AIDR branding
- 💚 **Neon Green Effects**: Glowing lines, animations, and accents
- 🌊 **Abstract Animations**: Flowing neon lines across backgrounds
- 🎯 **Modern UI**: Cards, badges, and buttons with glow effects

### Color Scheme

Edit `src/css/custom.css` for color customization:

```css
:root {
  --ifm-color-primary: #00ff88;           /* Neon Green */
  --ifm-background-color: #292C3D;        /* Dark Blue-Gray */
  --ifm-background-surface-color: #2f3349;
  --ifm-code-background: #242838;
}
```

### Key Files

- **Homepage**: `src/pages/index.tsx` - Hero section with animations
- **Homepage Styles**: `src/pages/index.module.css` - Neon effects and animations
- **Global Styles**: `src/css/custom.css` - Color scheme and variables
- **Documentation**: `docs/*.md` - Markdown content
- **Navigation**: `sidebars.js` - Sidebar configuration
- **Logo**: `static/img/aidr-bastion-logo.png` - 3D cyberpunk fortress

## 📚 Documentation

For more information about Docusaurus, visit:
- [Docusaurus Documentation](https://docusaurus.io/)
- [AIDR Bastion Repository](https://github.com/0xAIDR/AIDR-Bastion)

## 📝 License

Documentation is licensed under [LGPL-3.0](https://www.gnu.org/licenses/lgpl-3.0.html).

AIDR Bastion project is licensed under [LGPL-3.0](https://github.com/0xAIDR/AIDR-Bastion/blob/main/LICENSE).



