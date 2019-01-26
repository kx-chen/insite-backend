from flask import Flask, jsonify

from utils import summarize_from_text

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> hi </h1>'


@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    summary = summarize_from_text(
        u"There’s not a woman alive who hasn’t suffered through an unwanted "
        u"come-on from a creep. Some women are so afraid of these encounters "
        u"they feel they can’t be as nice to men as they’d like, for fear "
        u"their friendliness will be mistaken for flirtation.\nOne woman’s "
        u"encounter with a creepy come-on has received over 110,000 likes on "
        u"Twitter because of her flawless response.\nTwitter user "
        u"@LovableAndKind recently shared screenshots from a text exchange "
        u"between her sister and a Jiffy Lube employee who found her phone "
        u"number and sent her an unsolicited text.\nThe woman received a text "
        u"from an unfamiliar number that read: “You are gorgeous.” When she "
        u"asked who it was he responded, “Your favorite oil change guy.”\nThe "
        u"woman could have responded with anger or ignored the creep and "
        u"blocked him, but instead she decided to create a teachable "
        u"moment.\n“While I know you were wanting to give me a compliment, "
        u"it was completely unnecessary and unsolicited,” she replied. “I am "
        u"a customer, you are a service provider, and there should be no "
        u"communication outside of that unless I, the customer, express "
        u"interest.”\n'\n'\nShare\nEmbed\nLink\nShe then explained why his "
        u"text was so violating.\n“It is a violation of my privacy for you to "
        u"contact me from your personal phone with information that you got "
        u"without my permission,” she continued.\n“And now I know that you "
        u"are the type of person to go back in someone’s file to find their "
        u"personal information, what is to keep you from going back and "
        u"getting my address? There are men who stalk, rape and murder women "
        u"this way.”\nShe then wrote that she could call Jiffy Lube human "
        u"resources to report his actions, but she’d rather he learned from "
        u"the incident.\n“Sorry about that yes ma’am,” he responded.\nThen "
        u"she hit him back with one final diss.\n“Oh, and you didn't tell me "
        u"what the tire pressure was on the rear passenger tire like I asked, "
        u"so you're definitely not even in my top five favorite oil change "
        u"guys,\" she wrote.\n'\n'\nShare\nEmbed\nLink\nHere’s the entire "
        u"exchange.")

    return jsonify({
        "summary": summary
    })


if __name__ == '__main__':
    app.run()
