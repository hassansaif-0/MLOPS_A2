
from flask import Flask, render_template,jsonify
import textblob as tb
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import time

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/comments")
def show_comments():
    print("I am called");
    # Set up authentication
    os.environ["API_KEY"] = "AIzaSyCRro0uxYmMN55w-1TJRwrTl-Hc6EN-LNU"
    # Set your API key and YouTube channel ID
    api_key = os.environ["API_KEY"]
    channel_id = 'UC8w4I8t2OpqoOpzzNT1c2dg'

    # Authenticate with the YouTube Data API
    scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']
    credentials = service_account.Credentials.from_service_account_file('youtubecommentsmlops-12dbd42056ab.json', scopes=scopes)
    youtube = build('youtube', 'v3', credentials=credentials)
    # Get the live chat ID of the video

    
    live_chat_id = youtube.videos().list(
        part="liveStreamingDetails",
        id="gCNeDWCI0vo"
    ).execute()["items"][0]["liveStreamingDetails"]["activeLiveChatId"]

    # Retrieve comments
    comments = []
    next_page_token = None
    while True:
        response = youtube.liveChatMessages().list(
            liveChatId=live_chat_id,
            part="snippet, authorDetails",
            pageToken=next_page_token
        ).execute()

        for item in response["items"]:
            comment_text = item["snippet"]["textMessageDetails"]["messageText"]
            author_name = item["authorDetails"]["displayName"]
            tb_msg = tb.TextBlob(comment_text)
            score = tb_msg.sentiment
            comments.append(( comment_text,score))
        next_page_token = response.get("nextPageToken")
        # time.sleep(10)  # Wait for 10 seconds before making the next request

        # Only show the latest 10 comments
        if len(comments) >= 10:
            break
    comments.reverse();
    # Render the template with the comments
    return jsonify({"comments": comments})

if __name__ == "__main__":
    app.run(debug=True)




# def sentiment_analysis(post):

#     # Here's where the magic happens
#     tb_msg = tb(post)
#     score = tb_msg.sentiment
#     print(post,"   ",score)







# # Continuously retrieve new comments
# ext_page_token = None
# while True:
#     response = youtube.liveChatMessages().list(
#         liveChatId=live_chat_id,
#         part="snippet, authorDetails",
#         pageToken=next_page_token
#     ).execute()

#     for item in response["items"]:
#         comment_text = item["snippet"]["textMessageDetails"]["messageText"]
#         author_name = item["authorDetails"]["displayName"]
     
#         print(f"{comment_text}     n         score:{score}")

#     next_page_token = response.get("nextPageToken")
#     time.sleep(10) 

# # # Print the comments
# # for item in comment_response['items']:
# #     comment = item['snippet']['topLevelComment']['snippet']['textDisplay']

    


