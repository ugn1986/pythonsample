from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from database.db import initialize_db
from resource.route import initialize_routes
from resource.errors import errors 

app = Flask(__name__)
api = Api(app, errors=errors) 
app.config['PROPAGATE_EXCEPTIONS']=False

initialize_db(app)
initialize_routes(api)
        
if __name__ == "__main__":
    app.run(debug=True)