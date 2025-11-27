from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "world")
    return f"Hello {name}!"

@app.route("/vuln")
def vuln():
    cmd = request.args.get("cmd", "")
    return f"Command output: {cmd}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
