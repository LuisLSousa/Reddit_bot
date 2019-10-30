import sys
import traceback
import config
import time
import praw
import random
import os

# https://www.reddit.com/user/user_name to check the target's comments.

# This is a Reddit bot to reply to a user's comments using strings defined in the code.

# Disclaimer: I made this bot for educational purposes. A friend challenged me to make a Reddit bot, and I made this bot to reply to his comments
# and show him it was working, rather than telling him. This is not to be used to harass people and should be used responsibly.
# If you intend to use this code, make sure to read Reddit's rules beforehand.
# If you are making a Reddit bot, I highly recommend using r/test to test it.

# This bot could easily be changed into something more useful, like replying to a user who *invokes* the bot. 

def login():

# username, password, client_id and client_secret are all stored in the "config.py" file. This file should have your bot account's information

	print("Logging in...")
	reddit = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "my first bot v1.0") 
	print("Logged in")
	return reddit


def harass(reddit, crt):

    #in replies_list change the strings to the replies you want to comment
	replies_list = ['string_one', 'string_two', '...']
	reply = random.SystemRandom()
	
	print("Checking comments made by u/user_name")
	for comment in reddit.redditor('user_name').comments.new(limit = 4):
		if comment.id not in crt:
			print("Found comment: " + comment.id)
			crt.append(comment.id)
			with open ("comments_replied_to.txt", "a") as file:
				file.write(comment.id + "\n")
			comment.reply(reply.choice(replies_list))    
	print(crt)
	print("30 second break...")
	time.sleep(30) #this 30 second break is to make sure the bot isn't spamming the servers.

def get_comments():
	# To make sure the bot isn't replying to the same comment more than once, all the comments the bot has replied to are stored in a text file.
	if not os.path.isfile("comments_replied_to.txt"):
		crt = []
	else:
		with open("comments_replied_to.txt", "r") as file:
			crt = file.read()
			crt = crt.split("\n")

	return crt	
	
reddit = login()
crt = get_comments() 		
while True:
	harass(reddit, crt)
