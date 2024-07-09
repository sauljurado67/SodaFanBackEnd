from flask import Flask
from app.views import *
from app.viewUser import *
from app.database import init_app
from flask_cors import CORS

# inicializacion de la apliacion con Flask
app = Flask(__name__)
# permitir solicitudes desde cualquier origin
CORS(app)
init_app(app)

# registrar una ruta asociada a una vista de temas
app.route('/', methods=['GET'])(index)
app.route('/api/sodafan/', methods=['GET'])(get_all_temas)
app.route('/api/sodafan/', methods=['POST'])(create_tema)
app.route('/api/sodafan/<int:idtemas>', methods=['GET'])(get_tema)
app.route('/api/sodafan/<int:idtemas>', methods=['PUT'])(update_tema)
app.route('/api/sodafan/<int:idtemas>', methods=['DELETE'])(delete_tema)

# registrar una ruta asociada a una vista de usuarios
app.route('/', methods=['GET'])(index_user)
app.route('/api/sodafan/user/', methods=['GET'])(get_all_users)
app.route('/api/sodafan/user/', methods=['POST', 'GET'])(create_user)
app.route('/api/sodafan/user/<int:id>', methods=['GET'])(get_user)
app.route('/api/sodafan/user/<int:id>', methods=['PUT'])(update_user)
app.route('/api/sodafan/user/<int:id>', methods=['DELETE'])(delete_user)


if __name__ == '__main__':
    # levanta servidor de desarrollo flask
    app.run(debug=True)
