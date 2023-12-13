import os
import dotenv
from flask import Flask

dotenv.load_dotenv('.env')
config = dict(
    debug=True,
    SECRET_KEY=os.environ['SECRET_KEY'],
    SQLALCHEMY_DATABASE_URI=os.environ['SQLALCHEMY_DATABASE_URI'],
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)


app = Flask(__name__)
app.config.update(config)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
