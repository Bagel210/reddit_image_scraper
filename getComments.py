# getUrl
# by Iain Brown
#


import time
import praw
import urllib2
import urllib
import webbrowser
import os




r = praw.Reddit("comment scraper 1.0 u/bagel210")

fp = r.get_front_page

#r.login('bagel210', 'bot_password')
submission = r.get_submission(submission_id='11v36o')
flat_comments = praw.helpers.flatten_tree(submission.comments)
for item in flat_comments:
  outfile.write("\n".join(flat_comments))