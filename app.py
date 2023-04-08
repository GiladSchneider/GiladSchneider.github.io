# import dependencies
import flask
from flask_frozen import Freezer

# create a flask app
app = flask.Flask(__name__)
freezer = Freezer(app)

# create a route
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return flask.render_template('index.html')

# run the app
if __name__ == '__main__':
    freezer.freeze()
    freezer.run(debug=True)