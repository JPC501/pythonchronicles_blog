from blog import create_app

from config import configu


enviroment = configu['development']


if __name__ == '__main__':
    app = create_app(enviroment)
    app.run(debug=True, port=5001)
