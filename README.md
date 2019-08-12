# SUG-POLL-WEBSITE

A simple Django project for Voting for SUG Polls in FUTMinna 

- [Getting Started](#getting-started)
- [Installation](#installation)
- [Running Locally](#running-locally)

## Getting Started

Clone the repo

```bash
    # SSH
    git@github.com:NUKSI911/SUG-POLL-WEBSITE.git
    # HTTPS
    git clone https://gitlab.com/NUKSI911/SUG-POLL-WEBSITE.git
```

Activate virtual environment. All project work should be done in virtualenvs and virtualenv names must be added to gitignore

### Installation

- Install the requirements

```bash
    # install requirements
    pip install -r requirements.txt
```

Run migrations before starting the django-server

```bash
    python manage.py migrate
```

## Running Locally

To view the API locally

```bash
    python manage.py runserver
```

