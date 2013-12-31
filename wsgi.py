from os import path
from webhook import app
app.config.from_pyfile(path.join(path.dirname(path.abspath(__file__)), 'config', 'webhook.py'))
if __name__ == '__main__':
    app.run(debug=True)
