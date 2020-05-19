from flask import Flask
example_app = Flask(__name__)


@example_app.route('/')
def hello_world():
    return 'Hello Full Stack Cohort Winter 2020. You are awesome! ' \
           'This really works automatically!'


if __name__ == '__main__':
    example_app.run()
