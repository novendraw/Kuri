from flask import Flask, request
from flask_restful import Api, Resource
from pycipher import Vigenere, Caesar

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def post(self, name):
          if (name == "1"):
            content = request.get_json()
            vig = Vigenere(key='fortification')
            cipher = vig.encipher(content['plaintext'])
            return 'ciphertext : '+cipher, 200
          if (name == "2"):
            content = request.get_json()
            vig = Vigenere(key='fortification')
            cipher = vig.decipher(content['ciphertext'])
            return 'plaintext : '+cipher, 200
          if (name == "3"):
            content = request.get_json()
            caes = Caesar(key=13)
            cipher = caes.encipher(content['plaintext'])
            return 'ciphertext : '+cipher, 200
          if (name == "4"):
            content = request.get_json()
            caes = Caesar(key=13)
            cipher = caes.decipher(content['ciphertext'])
            return 'plaintext : '+cipher, 200

          return "cipher not found", 404

api.add_resource(User, "/crypto/<string:name>")