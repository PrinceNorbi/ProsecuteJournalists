from flask import Flask, request
from flask_restful import Resource, Api

#To make favicon work 1/2
import os
from flask import send_from_directory

#App
app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
   def get(self):
      return { "message" : "Hello Flask API World!" }
api.add_resource(Greeting, '/') # Route_1

if __name__ == '__main__':
   app.run('0.0.0.0')


#To make favicon work 2/2
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
