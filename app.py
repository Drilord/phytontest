from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/data', methods=['POST'])
   def handle_data():
       data = request.get_json()
       processed_data = {"received": data}
       return jsonify(processed_data)


if __name__ == '__main__':
    app.run(port=5500)