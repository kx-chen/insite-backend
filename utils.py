import requests
import os


def summarize_from_text(text_for_processing):
    api_key = os.environ.get('SUMMARIZE_API_KEY')
    post_body = bytes(text_for_processing.encode('utf-8'))
    api_url = f"https://www.summarizebot.com/api/summarize?apiKey={api_key}&size=18&keywords=10&fragments=15&language=English"
    header = {'Content-Type': "application/octet-stream"}

    r = requests.post(api_url, headers=header, data=post_body)
    json_res = r.json()

    summary_string = ""
    print(json_res)
    for summary in json_res[0]['summary']:
        summary_string += summary['sentence']

    return summary_string


def url_encode(url):
    return requests.utils.quote(url, safe='')


def extract_text_from_url(url):
    diffbot_api_key = os.environ.get('DIFFBOT_API_KEY')
    url = url_encode(url)
    text_json = requests.get(f"https://api.diffbot.com/v3/article?token={diffbot_api_key}&url={url}")
    return text_json.json()['objects'][0]['text']


def check_fake(url):
    api_key = os.environ.get('SUMMARIZE_API_KEY')
    r = requests.get(f"https://www.summarizebot.com/api/checkfake"
                     f"?apiKey={api_key}&url={url}")
    confidence_counter = {"confidence": 0}
    for i in r.json()['predictions']:
        if i['confidence'] > confidence_counter['confidence']:
            confidence_counter = i

    return confidence_counter


print(check_fake("https://bizstandardnews.com/2019/01/13/taylor-fbi-trump-investigation-motivated-by-contract-wizards/"))


