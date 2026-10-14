# 🔗 Django URL Shortener

A fast, lightweight, and efficient URL shortening web application built with **Django**. This app allows users to input long URLs, generate short, unique tracking links, and automatically redirect visitors to the original destination while tracking click analytics.

---

## 🌟 Features

- **URL Shortening:** Convert lengthy URLs into clean, short, and manageable custom or randomly generated links.
- **Instant Redirection:** Seamlessly redirect users from the short link to the original target URL.
- **Click Analytics / Counter:** Track how many times each shortened link has been visited.
- **User Authentication (Optional):** Allow registered users to manage, view history, and delete their generated short links.
- **Clean Admin Dashboard:** Manage URLs, users, and click stats directly from the Django admin interface.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (Development) / PostgreSQL (Production ready)
- **Frontend:** HTML5, CSS3, Bootstrap / Tailwind CSS
- **Deployment:** PythonAnywhere / Render / Heroku

---

## 📁 Project Structure

```text
Django-URL-Shortner/
│
├── core/                   # Project settings and configurations
├── shortener/              # Main app containing models, views, and URL mappings
├── templates/              # HTML frontend templates (home page, stats, etc.)
├── static/                 # Static assets (CSS, JS, images)
├── db.sqlite3              # Local SQLite database
├── manage.py               # Django management command-line utility
└── requirements.txt        # Project dependencies
