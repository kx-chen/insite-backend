from flask import Flask, jsonify, request

from utils import summarize_from_text

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> hi </h1>'


@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    url_to_summarize = request.args.get('url')
    summary = summarize_from_text(url_to_summarize)

    return jsonify({
        "summary": summary
    })


if __name__ == '__main__':
    app.run()
