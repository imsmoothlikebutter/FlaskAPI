from flask import Flask

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_api():
    return {
        'data': 'Hello, World!'
    }

# if __name__ == '__main__':
#     app.run(debug=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
