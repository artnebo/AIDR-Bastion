# 🚀 GitHub Pages Deployment Guide

## Автоматичний деплой через GitHub Actions

Ваш сайт налаштований для автоматичного деплою на GitHub Pages при кожному push до гілки `main`.

### Кроки для деплою:

1. **Запуште код на GitHub:**
   ```bash
   git add .
   git commit -m "Add Docusaurus site with custom styling"
   git push origin main
   ```

2. **Увімкніть GitHub Pages:**
   - Перейдіть до Settings вашого репозиторію
   - Знайдіть секцію "Pages" в лівому меню
   - У розділі "Source" виберіть "GitHub Actions"

3. **Перевірте деплой:**
   - Перейдіть до вкладки "Actions" у вашому репозиторії
   - Чекайте завершення workflow "Deploy to GitHub Pages"
   - Після успішного деплою ваш сайт буде доступний за адресою:
     `https://0xaidr.github.io/AIDR-Bastion/`

### Локальний тест:

```bash
# Запустити локальний сервер
npm start

# Збудувати для продакшену
npm run build

# Тестувати білд локально
npm run serve
```

### Структура файлів:

- `.github/workflows/deploy.yml` - GitHub Actions workflow
- `docusaurus.config.js` - конфігурація Docusaurus
- `src/pages/index.tsx` - головна сторінка
- `src/pages/index.module.css` - стилі головної сторінки

### Особливості сайту:

✅ Темна тема за замовчуванням  
✅ Анімовані зелені точки в Hero секції  
✅ Responsive дизайн  
✅ Автоматичний деплой на GitHub Pages  
