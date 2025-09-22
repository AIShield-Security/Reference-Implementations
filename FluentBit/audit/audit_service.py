from flask import Flask, request

app = Flask(__name__)

@app.route('/ingest', methods=['POST'])
def ingest():
    log_data = request.json
    print("Received log:", log_data, flush=True)
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
