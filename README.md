# rced

Basic script to manage your [reddit](https://www.reddit.com/) comment history

## How to use this script

### Dependencies

[PRAW](https://praw.readthedocs.io/en/stable/) is the only dependency.

Make sure to set up a venv and install it with `pip install praw`

**Tested with PRAW 7.7.0**

### Authorization

1. From [old.reddit](https://old.reddit.com/prefs/apps/) click on the "create another app..." button
2. Give it a name and set `http://localhost:8080` as "redirect uri"
3. Copy the secret and put it as the value of the `rced_secret` global variable in the script
4. Now check your email, the "APP ID" has been sent to you, put it as the value of the `rced_id` global variable
5. Fill the two remaining global variables in the script with your reddit username and password and you are good to go.

## Discalimer

Using this script or modifications of this script to wipe your comment history is against Reddit terms.

Such behaviour can lead to your account being temporary or permanently locked.

**Do not use this script in violation of Reddit terms**
