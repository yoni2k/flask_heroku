from flask import Flask
import os
example_app = Flask(__name__)


@example_app.route('/')
def hello_world():
    return 'Hello Full Stack Cohort Winter 2020!'


if __name__ == '__main__':
    example_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
