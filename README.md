# flask_initial

### Shows how to deploy a bare Python Flask application to Heroku.

### 3 options for running the project:
1. **Local run for testing** - run just as a python file `flask_example.py` without Gunicorn.  Since environment variable `'PORT'` does not exist, will listen on port `5000`
2. **Heroku without Gunicorn** - same as above, uses the following line in `Procfile`:
   `web: python flask_example.py`.  Will listen on port given by Heroku in environment variable `PORT`
3. **Heroku with Gunicorn** - change `Procfile` line to: 
   `web: gunicorn flask_example:example_app`
   Then Gunicorn will run inside Heroku dyno with multiple instances of the `flask_example.py` depending on available and used memory using ` WEB_CONCURRENCY` variable given by Heroku.
   