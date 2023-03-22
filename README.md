# YouTube Comments Sentiment Analysis Web App
This is a web application built with Flask and Python that uses the YouTube Data API to retrieve comments from a live chat and perform sentiment analysis on them using the TextBlob library.

# Installation
To use this application, you will need to have Python 3.x installed on your system.

Clone this repository to your local machine.

 Install the required packages using pip:
    pip install Flask google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client textblob
Set up your API key and YouTube channel ID by replacing the values in the api_key and channel_id variables in the show_comments() function.

Run the application using the following command:

python app.py

# Usage
Once the application is running, you can access it in your web browser at http://localhost:5000/.

Click the "Show Comments" button to retrieve the latest comments from the live chat of the specified YouTube video and display them along with their sentiment scores.

The sentiment scores are calculated using the TextBlob library, which assigns a polarity score (ranging from -1 to 1) and a subjectivity score (ranging from 0 to 1) to each comment.

# Credits
This project was developed by [Sher Ali , Hassan Saif]. It uses the following third-party libraries:

Flask

Google API Client

TextBlob
