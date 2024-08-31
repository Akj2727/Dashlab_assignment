from flask import Flask, request, jsonify
import requests
import google.generativeai as genai
import time
app = Flask(__name__)

genai.configure(api_key='AIzaSyAtOw0rANAGCDGp_YIg95B5mzEHgzdUI10')

model = genai.GenerativeModel('gemini-1.5-flash')


def make_api_call(prompt):
    output = {}
    output["Prompt"] = prompt
    req_sent_time = int(time.time())
    response = model.generate_content(prompt)
    res_rec_time = int(time.time())
    output["Message"] = (response.text).strip()
    output["TimeSent"] = req_sent_time
    output["TimeRecvd"] = res_rec_time
    output["Source"] = "Gemini"

    return output

@app.route('/', methods=['GET'])
def home():
    return jsonify({"server-status":"OK"})


@app.route('/process_prompt', methods=['GET'])
def process_prompt():
    prompt = request.args.get('prompt')
    client_id = request.args.get('clientID')

    if not prompt or not client_id:
        return jsonify({"error": "No prompt or clientID provided"}), 400

    response = make_api_call(prompt)
    response["Client ID"] = client_id
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)