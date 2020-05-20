# flask_initial

### Shows how to deploy a bare Python Flask application to Heroku.

### 3 options for running the project:
1. **Local run for testing** - run as a python file `flask_example.py` without Gunicorn locally.  Since environment variable `'PORT'` does not exist, will listen on default Flask port `5000` on `localhost` only.
2. **Heroku without Gunicorn** - run as a python file `flask_example.py` without Gunicorn on Heroku.  Use the following line in `Procfile`:
   `web: python flask_example.py`.  Will listen on port given by Heroku in environment variable `PORT`
3. **Heroku with Gunicorn** - change `Procfile` file to: 
   `web: gunicorn flask_example:example_app`.
   Then Gunicorn will run inside Heroku dyno with multiple instances of the `flask_example.py` specified by Heroku in environment variable `WEB_CONCURRENCY` depending on available and used memory in the dyno.
   