import requests

# Text for processing in UTF-8 encoding
text_for_processing = u"There’s not a woman alive who hasn’t suffered through an unwanted come-on from a creep. Some women are so afraid of these encounters they feel they can’t be as nice to men as they’d like, for fear their friendliness will be mistaken for flirtation.\nOne woman’s encounter with a creepy come-on has received over 110,000 likes on Twitter because of her flawless response.\nTwitter user @LovableAndKind recently shared screenshots from a text exchange between her sister and a Jiffy Lube employee who found her phone number and sent her an unsolicited text.\nThe woman received a text from an unfamiliar number that read: “You are gorgeous.” When she asked who it was he responded, “Your favorite oil change guy.”\nThe woman could have responded with anger or ignored the creep and blocked him, but instead she decided to create a teachable moment.\n“While I know you were wanting to give me a compliment, it was completely unnecessary and unsolicited,” she replied. “I am a customer, you are a service provider, and there should be no communication outside of that unless I, the customer, express interest.”\n'\n'\nShare\nEmbed\nLink\nShe then explained why his text was so violating.\n“It is a violation of my privacy for you to contact me from your personal phone with information that you got without my permission,” she continued.\n“And now I know that you are the type of person to go back in someone’s file to find their personal information, what is to keep you from going back and getting my address? There are men who stalk, rape and murder women this way.”\nShe then wrote that she could call Jiffy Lube human resources to report his actions, but she’d rather he learned from the incident.\n“Sorry about that yes ma’am,” he responded.\nThen she hit him back with one final diss.\n“Oh, and you didn't tell me what the tire pressure was on the rear passenger tire like I asked, so you're definitely not even in my top five favorite oil change guys,\" she wrote.\n'\n'\nShare\nEmbed\nLink\nHere’s the entire exchange."
# Create bytes representation of the text
post_body = bytes(text_for_processing.encode('utf-8'))

api_url = "https://www.summarizebot.com/api/summarize?apiKey=b6798d225e8f40e297dcdefaa6245175&size=20&keywords=10&fragments=15"
header = {'Content-Type': "application/octet-stream"}
r = requests.post(api_url, headers=header, data=post_body)
json_res = r.json()

summary_string = ""
for summary in json_res[0]['summary']:
    summary_string += summary['sentence']

print(summary_string)
