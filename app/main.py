from flask import Flask, request
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the insecure app!"

@app.route("/ping")
def ping():
    ip = request.args.get("ip", "127.0.0.1")
    return subprocess.getoutput(f"ping -c 1 {ip}")

@app.route("/readfile")
def read_file():
    filename = request.args.get("file", "README.md")
    with open(filename, "r") as f:
        return f.read()

@app.route("/env")
def environment():
    key = request.args.get("key")
    return os.getenv(key, "Not found")

if __name__ == "__main__":
    app.run()
