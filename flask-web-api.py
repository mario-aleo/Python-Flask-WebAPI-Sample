#!flask/bin/python
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

## Data Sample
data = [
    {
        'id': 1,
        'title': 'Teste Title',
        'description': 'Teste Description'
    }
]

@app.route('/teste/api/getData', methods=['POST'])
def get_tasks():
    print(request.json)
    return jsonify({'data': data})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
