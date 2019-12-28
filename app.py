from flask import Flask,render_template
from ueditor import bp
import config


app = Flask(__name__)
app.register_blueprint(bp)
app.config.from_object(config )

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
