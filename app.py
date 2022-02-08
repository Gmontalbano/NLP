import imp
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from nlp import data, similarity

app = Flask(__name__)
api = Api(app)


class Portuguese(Resource):
    def post(self):
       #Step 1 get the posted data
        text1, text2 = data(request.get_json())
       #Call the function similarity 
        ratio = similarity(text1, text2, "portuguese")

        retJson = {
            "status":200,
            "ratio": ratio,
            "msg":"Similaridade calculada com sucesso"
        }

        
        return jsonify(retJson)


class English(Resource):
    def post(self):
       #Step 1 get the posted data
        text1, text2 = data(request.get_json())
       #Call the function similarity 
        ratio = similarity(text1, text2, "english")

        retJson = {
            "status":200,
            "ratio": ratio,
            "msg":"Similarity score calculated successfully"
        }

        
        return jsonify(retJson)


class Spanish(Resource):
    def post(self):
       #Step 1 get the posted data
        text1, text2 = data(request.get_json())
       #Call the function similarity 
        ratio = similarity(text1, text2, "spanish")

        retJson = {
            "status":200,
            "ratio": ratio,
            "msg":"Similitud calculada con éxito"
        }

        
        return jsonify(retJson)


api.add_resource(Portuguese, '/portuguese')
api.add_resource(English, '/english')
api.add_resource(Spanish, '/spanish')


if __name__ == "__main__":
    app.run(host='0.0.0.0')