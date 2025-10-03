# 🚀 Деплой в приватний репозиторій

## Крок 1: Створіть приватний репозиторій на GitHub

1. Перейдіть на [github.com](https://github.com)
2. Натисніть "New repository"
3. Назвіть репозиторій `AIDR-Bastion` (або будь-яку назву)
4. Виберіть **"Private"**
5. **НЕ** створюйте README, .gitignore або ліцензію
6. Натисніть "Create repository"

## Крок 2: Підключіть локальний репозиторій

```bash
cd /Users/andriibo/Desktop/github/AIDR-Bastion-site

# Замініть YOUR_USERNAME на ваш GitHub username
git remote add origin https://github.com/YOUR_USERNAME/AIDR-Bastion.git

# Замініть YOUR_USERNAME в docusaurus.config.js
# Відкрийте docusaurus.config.js і замініть:
# url: 'https://YOUR_USERNAME.github.io',

git add .
git commit -m "Update config for private repo"
git push -u origin main
```

## Крок 3: Увімкніть GitHub Pages

1. Перейдіть до **Settings** вашого репозиторію
2. Прокрутіть вниз до секції **"Pages"**
3. У розділі **"Source"** виберіть **"Deploy from a branch"**
4. Виберіть гілку **"gh-pages"** (вона створиться автоматично)
5. Натисніть **"Save"**

## Крок 4: Запустіть деплой

1. Перейдіть до вкладки **"Actions"**
2. Знайдіть workflow **"Deploy to GitHub Pages"**
3. Натисніть **"Run workflow"** → **"Run workflow"**

## Крок 5: Перевірте результат

Після успішного виконання ваш сайт буде доступний за адресою:
`https://YOUR_USERNAME.github.io/AIDR-Bastion/`

## Альтернативний спосіб - ручний деплой

Якщо Actions не працюють, можете зробити деплой вручну:

```bash
# Збудувати сайт
npm run build

# Встановити gh-pages
npm install --save-dev gh-pages

# Додати скрипт в package.json
# "deploy": "gh-pages -d build"

# Задеплоїти
npm run deploy
```

## Налаштування для приватного репозиторію

- ✅ Workflow оновлений для приватних репозиторіїв
- ✅ Використовує `peaceiris/actions-gh-pages` (простіший)
- ✅ Автоматично створює гілку `gh-pages`
- ✅ Працює з `GITHUB_TOKEN` (автоматично доступний)
