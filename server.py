import traceback

from flask import Flask, jsonify, request

from utils import summarize_from_text, extract_text_from_url
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '<h1> hi </h1>'

@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    url_to_summarize = request.args.get('url')
    try:
        page_text = extract_text_from_url(url_to_summarize)
        summary = summarize_from_text(page_text)
    except:
        traceback.print_exc()
        summary = ("There was an error processing the request, "
                   "please try a different article.")
        return jsonify({
            "summary": summary
        }), 400

    return jsonify({
        "summary": summary
    })


if __name__ == '__main__':
    app.run()
