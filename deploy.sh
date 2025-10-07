#!/bin/bash

# Скрипт для деплою документації на GitHub Pages
# Використання: ./deploy.sh

set -e

echo "🚀 Початок деплою документації AIDR-Bastion..."

# Перевіряємо, чи ми в правильній директорії
if [ ! -f "package.json" ]; then
    echo "❌ Помилка: Запустіть скрипт з папки docs-site"
    exit 1
fi

# Встановлюємо залежності
echo "📦 Встановлення залежностей..."
npm ci

# Очищаємо попередню збірку
echo "🧹 Очищення попередньої збірки..."
npm run clear

# Збираємо документацію
echo "🔨 Збірка документації..."
npm run build

# Деплоюємо на GitHub Pages
echo "🚀 Деплой на GitHub Pages..."
npm run deploy

echo "✅ Деплой завершено успішно!"
echo "📖 Документація доступна за адресою: https://artnebo.github.io/AIDR-Bastion/"
