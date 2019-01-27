import requests
import os


def summarize_from_text(text_for_processing):
    api_key = os.environ.get('SUMMARIZE_API_KEY')
    post_body = bytes(text_for_processing.encode('utf-8'))

    api_url = f"https://www.summarizebot.com/api/summarize?apiKey={api_key}&url={text_for_processing}&size=18&keywords=10&fragments=15&language=English"
    header = {'Content-Type': "application/octet-stream"}
    r = requests.get(api_url)
    # r = requests.get(api_url, headers=header, data=post_body)
    json_res = r.json()
    print(json_res)

    summary_string = ""
    for summary in json_res[0]['summary']:
        summary_string += summary['sentence']

    return summary_string
