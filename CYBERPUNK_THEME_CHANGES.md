# 🟢 Cyberpunk Green Theme - Зміни

## ✅ Що було змінено:

### 🎨 Кольорова схема

**Нові кольори (зелена кіберпанк-палітра):**

```css
Primary: #00ff88 (яскраво-зелений неон)
Dark: #00e67a → #00b35e
Light: #1aff95 → #66ffbb
Background: #0a0e0d (майже чорний)
Surface: #131a17 (темно-сірий з зеленим відтінком)
```

**Старі кольори (фіолетові):**
```css
Primary: #667eea
```

---

### 🖼️ Hero Banner

**Новий градієнт:**
```css
background: linear-gradient(135deg, #0a1f17 0%, #001a0f 50%, #0a0e0d 100%);
```

**Додано:**
- Зелений неоновий overlay з радіальним градієнтом
- Ефект підсвічування

---

### 🏰 Логотип

**Замінено емоджі 🛡️ на зображення:**
```tsx
<img 
  src="/img/aidr-bastion-logo.png" 
  alt="AIDR Bastion" 
  className={styles.logo}
/>
```

**Анімації:**
- ✨ Float (плавне піднімання/опускання)
- 💚 Glow (пульсуючий зелений неон)

**Ефекти:**
```css
filter: drop-shadow(0 0 20px rgba(0, 255, 136, 0.5));
```

---

### 🏷️ Badges (Python 3.12, FastAPI, LGPL-3.0)

**Стиль:**
- Зелений неоновий border
- Прозорий фон з зеленим відтінком
- Glow ефект при hover
- Зелений текст (#00ff88)

---

### 🎯 Feature Cards

**6 карток на головній:**
- Multi-Pipeline Detection 🔍
- Flexible Configuration ⚙️
- Real-time Analysis ⚡
- Industry-Aligned 🎯
- Extensible Architecture 🔧
- Event Logging 📊

**Стилі:**
- Зелений прозорий фон
- Неоновий border
- Glow при hover
- Зелене підсвічування заголовків

---

### 💻 Tech Stack Items

**Технології:**
FastAPI, OpenSearch, OpenAI, Semgrep, Sentence Transformers, Kafka, Pydantic, Uvicorn

**Стилі:**
- Зелений неоновий вигляд
- Border з glow ефектом
- Анімація при hover

---

### 📋 Rule Cards (4 картки)

**Теми:**
- 🔐 Roota & Sigma Rules
- 🔄 Uncoder AI Integration
- 🎯 MITRE ATLAS Aligned
- 📋 OWASP Top 10 for LLMs

**Стилі:**
- Зелений прозорий фон
- Неоновий текст
- Text-shadow на заголовках

---

### 🎨 Архітектурна діаграма

**ASCII схема:**
```
┌────────────────────────────────┐
│   FastAPI Endpoint             │
│   (POST /api/v1/run_pipeline)  │
└──────────────┬─────────────────┘
               │
               ▼
      ┌─────────────────────┐
      │  Pipeline Manager   │
      ...
```

---

## 📁 Змінені файли:

1. ✅ `src/css/custom.css` - Кольорова палітра
2. ✅ `src/pages/index.module.css` - Всі стилі компонентів
3. ✅ `src/pages/index.tsx` - Заміна емоджі на зображення

---

## 🎯 Візуальні ефекти:

### 1. Неоновий Glow
```css
box-shadow: 0 0 20px rgba(0, 255, 136, 0.4);
```

### 2. Пульсуюче підсвічування
```css
@keyframes glow {
  0% { filter: drop-shadow(0 0 10px rgba(0, 255, 136, 0.3)); }
  100% { filter: drop-shadow(0 0 30px rgba(0, 255, 136, 0.8)); }
}
```

### 3. Hover ефекти
- Збільшення яскравості
- Посилення border
- Transform: scale або translateY

### 4. Text-shadow для заголовків
```css
text-shadow: 0 0 10px rgba(0, 255, 136, 0.3);
```

---

## 🌙 Dark Mode

Підтримка темної теми з зеленими акцентами:
- Темний фон (#0a0e0d)
- Яскраво-зелені акценти
- Неонові ефекти посилені в темній темі

---

## 📱 Responsive

Всі стилі адаптивні:
- Mobile: зменшені розміри
- Tablet: середні розміри
- Desktop: повний розмір з усіма ефектами

---

## 🚀 Наступний крок:

**Збережіть зображення:**

```bash
# Зберегти як:
/Users/andriibo/Desktop/github/AIDR-Bastion-site/static/img/aidr-bastion-logo.png
```

**Перезавантажте браузер:**
```
Cmd+R (Mac) або Ctrl+R (Windows/Linux)
```

---

## 🎨 Палітра кольорів для референсу:

| Колір | Hex | Використання |
|-------|-----|--------------|
| Яскраво-зелений | `#00ff88` | Primary, текст, borders |
| Світло-зелений | `#66ffbb` | Hover states, підсвічування |
| Темно-зелений | `#00b35e` | Dark states, тіні |
| Майже чорний | `#0a0e0d` | Фон |
| Темно-сірий | `#131a17` | Surface, картки |

---

**Тема готова! 🎉 Сайт виглядає як справжня кіберпанк-фортеця!**

