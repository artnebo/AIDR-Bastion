# 🚀 Готові команди для деплою

## Крок 1: Створіть репозиторій на GitHub
1. Перейдіть на https://github.com/new
2. Repository name: `AIDR-Bastion`
3. Description: `AIDR Bastion Documentation Site`
4. Виберіть **Private**
5. **НЕ** створюйте README, .gitignore, ліцензію
6. Натисніть **"Create repository"**

## Крок 2: Виконайте ці команди в терміналі

```bash
cd /Users/andriibo/Desktop/github/AIDR-Bastion-site

# Підключити репозиторій
git remote add origin https://github.com/artnebo/AIDR-Bastion.git

# Додати всі зміни
git add .

# Зробити коміт
git commit -m "AIDR Bastion documentation site with animations and custom styling"

# Запуштити на GitHub
git push -u origin main
```

## Крок 3: Увімкніть GitHub Pages
1. Перейдіть до https://github.com/artnebo/AIDR-Bastion/settings/pages
2. У розділі **"Source"** виберіть **"Deploy from a branch"**
3. Виберіть гілку **"gh-pages"** (вона створиться автоматично)
4. Натисніть **"Save"**

## Крок 4: Запустіть деплой

### Варіант 1: Автоматичний деплой через Actions
1. Перейдіть до https://github.com/artnebo/AIDR-Bastion/actions
2. Знайдіть workflow **"Deploy to GitHub Pages"**
3. Натисніть **"Run workflow"** → **"Run workflow"**

### Варіант 2: Ручний деплой
```bash
# Збудувати сайт
npm run build

# Задеплоїти на GitHub Pages
npm run deploy-gh-pages
```

## Крок 5: Перевірте результат
Після успішного деплою ваш сайт буде доступний за адресою:
**https://artnebo.github.io/AIDR-Bastion/**

## 🎉 Що у вас є:
✅ Сучасний дизайн з анімаціями  
✅ Темна тема за замовчуванням  
✅ Responsive дизайн  
✅ Автоматичний деплой  
✅ Готові команди для копіювання  

## 🔧 Якщо щось не працює:
1. Перевірте, що репозиторій створений як **Private**
2. Переконайтеся, що ви виконали всі команди по порядку
3. Перевірте, що GitHub Pages налаштований на гілку **gh-pages**
4. Якщо Actions не працюють, використайте ручний деплой
