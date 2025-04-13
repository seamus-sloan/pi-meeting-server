from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

current_status = {
    "inMeeting": False,
    "videoOn": False,
    "droneOn": False,
}

@app.route('/update', methods=['POST'])
def update_code():
    try:
        repo_dir = "/home/sesloan/pi-meeting-server"
        venv_python = f"{repo_dir}/venv/bin/python"
        venv_pip = f"{repo_dir}/venv/bin/pip"

        # Pull the new changes & update dependencies
        pull_output = subprocess.check_output(['git', '-C', repo_dir, 'pull'], stderr=subprocess.STDOUT)
        pip_output = subprocess.check_output([venv_pip, 'install', '-r', f'{repo_dir}/requirements.txt'], stderr=subprocess.STDOUT)
        
        # Restart scripts (kill old, run fresh)
        subprocess.call(['pkill', '-f', 'server.py'])
        subprocess.call(['pkill', '-f', 'display_status.py'])

        subprocess.Popen([venv_python, f'{repo_dir}/server.py'])
        subprocess.Popen([venv_python, f'{repo_dir}/display_status.py'])

        return jsonify({
            "status": "Updated successfully",
            "git": pull_output.decode(),
            "pip": pip_output.decode()
        })

    except subprocess.CalledProcessError as e:
        return jsonify({
            "error": "Update failed",
            "output": e.output.decode()
        }), 500

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(current_status), 200


@app.route('/status', methods=['POST'])
def update_status():
    data = request.get_json()

    for key in current_status:
        if key in data:
            current_status[key] = data[key]
    
    return jsonify(current_status), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)