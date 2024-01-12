# Pyttpass Password Manager Web App

### NOTE: This app is currently only used for demonstration purposes.
A web application built with Python and Flask for password management.

## Features

- **User Authentication:** Secure user authentication system to protect user accounts.
- **Password Storage:** Safely store and manage passwords for different accounts.
- **Encryption:** Utilizes encryption algorithms to ensure the security of stored passwords.
- **User-Friendly Interface:** Intuitive web interface for easy navigation and interaction.

## Technologies Used

- Python
- Flask
- SQLAlchemy (or your preferred database toolkit)
- HTML/CSS
- Bootstrap (optional for styling)

## Directory structure

```plaintext
.
├── config.py
├── Dockerfile
├── pyttpass
│   ├── app.py
│   ├── auth
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── extensions.py
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models
│   │   ├── auth.py
│   │   ├── __init__.py
│   │   └── passwords.py
│   ├── password_generator
│   │   ├── generator.py
│   │   └── __init__.py
│   ├── passwords
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── static
│   │   └── static.css
│   └── templates
│       ├── auth
│       │   ├── login.html
│       │   └── signup.html
│       ├── base.html
│       ├── index.html
│       ├── passwords
│       │   ├── add_password.html
│       │   ├── index.html
│       │   └── password.html
│       └── profile.html
├── pyttpass.db
├── requirements.txt
└── wsgi.py
```

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/dtyresson/pyttpass.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd pyttpass
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Set up a virtual environment:**

    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

3. **Configure environment variables:**

    Create a `.env` file in the root directory and define the following variables:

    ```env
    FLASK_APP=app
    FLASK_ENV=development  # Change to 'production' in a production environment
    SECRET_KEY=your_secret_key  # Generate a secret key for Flask sessions
    DATABASE_URI=your_database_uri  # Configure your database URI
    ```

## Usage

1. **Run the application:**

    ```bash
    flask run
    ```

2. **Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).**

## Contributing

If you'd like to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Made for educational and demonstrational purposes for [Opslogix](https://www.opslogix.com/).