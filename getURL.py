# getUrl
# by Iain Brown
#


import time
import praw
import urllib2
import urllib
import webbrowser
import os

Sub = raw_input('Which subreddit would you like to use? - ')

#r.login()
already_done = []
URLS = []

#while True:
#	subreddit = submissions = r.get_subreddit(Sub).get_hot(limit=5)

for i in range (1):
    subreddit = r.get_subreddit(Sub)
    for submission in subreddit.get_hot(limit=200):
 
          if ((".jpg") in (submission.url) and ((submission.id) not in already_done)):
        	URLS.append(submission.url)
        	already_done.append(submission.id)
        	
          else:
            already_done.append(submission.id)
            
    
   
i = 0;

for URL in URLS:


	picture_page = URL

	
	opener1 = urllib2.build_opener()
	page1 = opener1.open(picture_page)
	my_picture = page1.read()

	filename = str(i) + ".jpg"
	i+=1
	print "downloading..." + picture_page
	fout = open(filename, "wb")
	fout.write(my_picture)
	fout.close()
	webbrowser.open(filename)




