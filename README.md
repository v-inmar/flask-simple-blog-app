
# Flask Simple Blog App

A mini full-stack blogging web app using Flask (python). The web application structure is modular which allows more features to be added as modules. A slight decoupling is also enforced by having a service layer to allow for more thorough testing.

This project was done in a weekend (O.O)

## Features

- User Authentication using Flask-Login
- ORM for MySQL using Flask-SQLAlchemy
- Database migration with Flask-Migrate
- Jinja2 Frontend (comes package with Flask) with basic HTML, CSS (inline), (Currently no JS)
- Flask-WTF for working with Forms and Validations for user login and registration, blog creation and update
- PyMySQL for connecting to MySQL Server


## Considerations (Not Exhaustive)
 - Email Support
    - Flask-Mail for building email messages
    - Celery for background task (or something similar)
    - Redis as message broker (or something similar)
- Security
    - Rate Limit
    - ReCaptcha
- Tech
    - Better error handling
    - Image handling / CDN
    - Reverse Proxy / Load Balancer
    - WSGI server
    - A better css framework
    - CI/CD pipeline when Testing is included
- Testing
    - Integration
    - Unit
    - End-to-End
    - PenTest (if you want)
## Deployment

Not adviced to be deployed at its current state. But good enough as a project.
## Run Locally

```bash
No Particular order
 - install python3
 - install mysql (you can use any rdbms but this app has been made with mysql in mind)
 - create virtual environment
 - download and unzip code repo
```

```bash
In mysql server, create flask_simple_blog_app_db database
```

```bash
Make sure you have virtual environment active
i.e. source venv/bin/activate
(on unix with venv as virtualenv name)

then install requirements
pip install -r requirements.txt
```

```bash
In root directory add environment files
 - root/.env
 - root/.flaskenv

Populate .env with
SECRET_KEY="your-super-secret-key"
DATABASE_URL='mysql+pymysql://<username>:<password>@<host>:<port>/flask_simple_blog_app_db'

Populate .flaskenv
FLASK_APP=run.py
FLASK_ENV=development
```

```
flask db init
flask db migrate
flask db upgrade

flask run --host="0.0.0.0" --port=5000 --debug --reload
```


