# Todo App

A simple and clean task management web application built with **Python Flask**. Add, update, delete, and prioritize your daily todos with ease.

**Live Demo:** [todoapp-f4pv.onrender.com](https://todoapp-f4pv.onrender.com/)

---

## Screenshots

### Home Page
<img width="1919" height="970" alt="Screenshot 2026-05-05 165706" src="https://github.com/user-attachments/assets/f24e8bca-4ae8-4af1-913a-bd549c8b7b80" />


### Add Todo
<img width="1901" height="966" alt="Screenshot 2026-05-05 170811" src="https://github.com/user-attachments/assets/a6006fb9-7176-4dfb-88f0-16b26318453a" />


### Edit Task
<img width="1919" height="626" alt="Screenshot 2026-05-05 165939" src="https://github.com/user-attachments/assets/4b50b81d-f699-413b-8711-7ebba7fe0abb" />

---

## Features

- **Add Todos** — Create tasks with a title, description, and optional importance flag
- **Priority Marking** — Star important tasks to highlight them at a glance
- **Update & Delete** — Edit or remove any task from the list
- **Search** — Quickly find tasks by keyword
- **Timestamps** — Each task shows its creation date and time
- **About Page** — Simple navigation between Home and About sections

---

## Tech Stack

| Layer      | Technology         |
|------------|--------------------|
| Backend    | Python, Flask      |
| Frontend   | HTML, Jinja2       |
| Database   | SQLite             |
| Deployment | Render             |

---

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/dadsena01/todoapp.git
cd todoapp

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open your browser and visit `http://localhost:5000`

---

## Project Structure

```
todoapp/
├── templates/          # HTML templates (Jinja2)
├── instance/           # SQLite database (auto-generated)
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile            # Deployment config
└── .gitignore
```

---

## Deployment

This app is deployed on **Render**. You can also deploy it on **Heroku** using the included `Procfile`.

---

## License

This project is open source and available under the [MIT License](LICENSE).
