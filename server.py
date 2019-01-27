from flask import Flask, jsonify, request

from utils import summarize_from_text, extract_text_from_url

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> hi </h1>'


@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    url_to_summarize = request.args.get('url')
    page_text = extract_text_from_url(url_to_summarize)
    summary = summarize_from_text(page_text)

    return jsonify({
        "summary": summary
    })


if __name__ == '__main__':
    app.run()
