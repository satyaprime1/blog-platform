# 📝 Blog Platform with Comments

A full-stack blogging platform built with **Python, Flask, SQLite, SQLAlchemy, and Flask-Login**.

The application allows users to register, log in, create and manage blog posts, and interact with other users through comments. It also provides RESTful APIs for working with posts and comments.

---

## 🚀 Features

### 👤 User Authentication
- User registration
- Secure password hashing
- User login and logout
- Session-based authentication
- Protected routes using Flask-Login

### 📝 Blog Posts
- Create blog posts
- View all blog posts
- View individual posts
- Edit your own posts
- Delete your own posts
- Post ownership authorization

### 💬 Comments
- Add comments to blog posts
- View comments
- Delete your own comments
- Comments are associated with users and posts

### 🔌 RESTful APIs
- Get all posts
- Get a single post
- Create posts using JSON
- Update posts using JSON
- Delete posts using API
- Get comments for a post
- Create comments using API
- JSON responses

### 🎨 Frontend
- Responsive Bootstrap interface
- Navigation bar
- Login and registration pages
- Blog post cards
- Post creation and editing forms
- Comment interface
- Flash messages for user feedback

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web framework |
| Flask-SQLAlchemy | Database ORM |
| SQLite | Database |
| Flask-Login | User authentication |
| Werkzeug | Password hashing |
| Bootstrap 5 | Frontend styling |
| REST API | Backend API communication |
| Jinja2 | HTML templating |

---

## 📂 Project Structure

```text
blog-platform/
│
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── post.py
│   └── comment.py
│
├── routes/
│   ├── __init__.py
│   ├── auth_routes.py
│   ├── post_routes.py
│   ├── comment_routes.py
│   └── api_routes.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── posts.html
│   ├── create_post.html
│   ├── edit_post.html
│   └── post_detail.html
│
├── instance/
│   └── blog.db
│
└── README.md
.
