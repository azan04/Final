# Flask Contact Management App

A simple Flask web application for managing contacts with SQLite database.

## Features

- Add new contacts (first name, last name, email)
- View all contacts
- Delete contacts
- SQLite database for persistence

## Requirements

- Python 3.11+
- Flask 3.1.2
- Flask-SQLAlchemy 3.1.1
- SQLAlchemy 2.0.43

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd FlaskApp
```

2. Create a virtual environment:
```bash
python -m venv env
```

3. Activate the virtual environment:
   - On Windows:
   ```bash
   env\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source env/bin/activate
   ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python App.py
```

The app will be available at `http://127.0.0.1:5000`

## Docker

To run the application in Docker:

```bash
docker build -t flaskapp .
docker run -p 5000:5000 flaskapp
```

## Project Structure

```
.
├── App.py              # Main application file
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── templates/         # HTML templates
│   ├── index.html    # Main page
│   └── update.html   # Update page
├── static/           # Static files (CSS, JS, images)
└── README.md         # This file
```

## License

MIT
