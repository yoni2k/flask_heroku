from flask import Flask
example_app = Flask(__name__)


@example_app.route('/')
def hello_world():
    return 'Hello Full Stack Cohort Winter 2020. You are awesome! ' \
           'This really works automatically!'


@example_app.route('/aviad')
def hello_world():
    return 'Aviad is the king of the world!'


if __name__ == '__main__':
    example_app.run()
