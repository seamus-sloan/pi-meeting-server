from flask import Flask, request, jsonify

app = Flask(__name__)

current_status = {
    "inMeeting": False,
    "videoOn": False,
    "droneOn": False,
}

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(current_status), 200


@app.route('/status', methods=['POST'])
def update_status():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    for key in current_status:
        if key in data:
            current_status[key] = data[key]
    
    return jsonify(current_status), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)