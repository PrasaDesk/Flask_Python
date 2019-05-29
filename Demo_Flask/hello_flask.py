from flask import Flask, redirect, url_for, jsonify
import json
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return redirect(url_for('getFlask'))

@app.route('/flask')
def getFlask():
    return jsonify({"name":"prasad"})

if __name__ == '__main__':
    app.run(debug=True)