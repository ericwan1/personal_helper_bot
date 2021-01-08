import praw
from datetime import date
import time
import string
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Acquiring the reddit content

client_id = "your id here"
client_secret = "your value here"
user_agent = "your agent name here"
username = "your username here"
password = "your password here"

reddit = praw.Reddit(
	client_id = client_id,
	client_secret = client_secret,
	user_agent = user_agent,
	username = username,
	password = password
)

# True is the default setting
# reddit.read_only = True

subreddit_list = ["aquariums", "shrimptank", "MachineLearning", "datascience", "cmu"] # Feel free to change this!
# subreddit_list = "ALL" # If we just want the most popular posts over reddit

reddit_text = ""

for sub in subreddit_list:
	subreddit = reddit.subreddit(sub)
	subreddit_hot_posts = subreddit.hot(limit = 5) # Number can be adjusted to personal desires (care for email length!)

	subreddit_html = "Subredddit: <b>" + subreddit.display_name + "</b><br>"
	reddit_text = reddit_text + subreddit_html

	post_counter = 1
	for posts in subreddit_hot_posts:
		post_url = "https://www.reddit.com" + posts.permalink
		post_title = posts.title

		post_html = str(post_counter) + ") " + "<a href=\"" + post_url + "\">" + post_title + "</a><br>"
		post_counter += 1

		reddit_text = reddit_text + post_html

	reddit_text = reddit_text + "<br>"


reddit_html = """\
				<html> <body> <p>Hi Pal,<br><br> Below are your daily subreddit updates, enjoy!<br><br>
			""" + reddit_text + """</p></body></html>"""

# Formatting and sending acquired links to email address

subject_str = "My Hot Reddit Posts: " + str(date.today())

sender_email = "sending email here"
receiver_email = "recieving email here"
password = "sender email password"

message = MIMEMultipart('alternative')
message["Subject"] = subject_str
message["From"] = sender_email
message["To"] = receiver_email

email_text = MIMEText(reddit_html, "html")
message.attach(email_text)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
