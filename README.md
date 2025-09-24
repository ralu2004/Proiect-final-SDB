# 🛒 Proiect Final SDB – Supermarket Management System

**A small Python console application to manage products and promotions in a supermarket.**  
A student project demonstrating modular design, simple persistence, and CLI interaction.

---

## 📌 Overview
This repository contains a **console-based supermarket management system** implemented in Python.  
It supports basic product and promotion management via two roles: **admin** and **client**.  
This project was developed as a study assignment and is one of my earlier full-project efforts to practice software design patterns and modularization.

---

## ✨ Features
- **Product management**
  - Add, update, delete, list products
  - Input validation for key fields (name, price, quantity, etc.)
- **Promotion management**
  - Create and manage promotions
  - Apply promotions to products based on simple rules
- **Role-based console interface**
  - Admin: full CRUD for products/promotions and repository management
  - Client: browse products and see applied promotions
- **Repository pattern**
  - Separation between business logic (services) and data access (repository)

---

## 🛠 Tech Stack
- Python 3.8+
- Standard library (no mandatory external dependencies)
- Optional: `pytest` for testing

---

## 🗂 Project Structure
```bash
Proiect-final-SDB/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── main.py
├── console.py
├── admin_service.py
├── client_service.py
├── promotion_service.py
├── product.py
├── promotion.py
├── product_validator.py
├── repository.py
├── exceptions.py
└── database/
└── ... (DB files)
```
> Note: If you reorganize into a package (e.g., `src/`), update imports and add `__init__.py` files.

---

## ⚙️ Requirements
- Python 3.8 or later
- Optional development/test dependency:
  pytest>=7.0

---

## 🚀 Installation
1. Clone the repository:
```bash
git clone https://github.com/ralu2004/Proiect-final-SDB.git
cd Proiect-final-SDB
```
2. Create and activate a virtual environment:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
```

## ▶️ Running the Application
```bash
python main.py
```

## 📖 Usage Examples
- Add product (admin): Admin → Manage Products → Add Product → enter details
- List products (client or admin): View Products → see list with promotions
- Create promotion (admin): Admin → Manage Promotions → Add Promotion → define rules

## 🗄 Configuration & Database
Currently uses file-based storage in database/.

## 🔮 Future Improvements
- Add persistent storage and migrations
- Implement REST API or GUI
- Centralize configuration
- Add unit/integration tests and CI
- Add logging and enhanced error handling
- Example data import/export scripts

## 📜 License
MIT License.

## 📬 Contact
GitHub profile: https://github.com/ralu2004
