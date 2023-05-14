import praw
import time
import random

rced_id = '' # app id you get in the mail after app creation
rced_secret = ''
reddit_username = ''
reddit_password = ''

reddit = praw.Reddit(client_id=rced_id,
                     client_secret=rced_secret,
                     user_agent='Comment Manager (u/{})'.format(reddit_username),
                     username=reddit_username,
                     password=reddit_password)

def get_random_sentence():
    with open('sentences.txt', 'r') as file:
        lines = file.readlines()
    return random.choice(lines).strip()

def overwrite_comment(comment):
    new_text = input('Enter a new line of text for the comment: ')
    reddit.validate_on_submit = True
    comment.edit(new_text)

def delete_comment(comment):
    comment.delete()

def safe_delete_comment(comment):
    random_sentence = get_random_sentence()
    comment.edit(random_sentence)
    time.sleep(random.uniform(5, 10))
    comment.delete()

for comment in reddit.redditor(reddit_username).comments.new(limit=None):
    print('\nComment:')
    print('\n')
    print(comment.body)
    print('\n')

    while True:
        action = input('Choose an action (overwrite, delete, safe-delete, skip): ')

        if action.lower() == 'overwrite':
            print('\n')
            overwrite_comment(comment)
            break
        elif action.lower() == 'delete':
            delete_comment(comment)
            break
        elif action.lower() == 'safe-delete':
            safe_delete_comment(comment)
            break
        elif action.lower() == 'skip':
            break
        else:
            print('Invalid input. Please try again.')
