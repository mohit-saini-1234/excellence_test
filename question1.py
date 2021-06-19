# Question 1

# Check this page https://my-json-server.typicode.com/typicode/demo
# Here you will find two api’s one for posts and comments 
# https://my-json-server.typicode.com/typicode/demo/posts
# https://my-json-server.typicode.com/typicode/demo/comments

# What you need to do is write a code which will read data from both these api’s and assign comment to its respective post and finally return an object (dict/json) which has the combined data of both posts/comments.





# Solution 1

# Function for return combined data

# imported request module
import requests


# comment and post api url
comment_api = "https://my-json-server.typicode.com/typicode/demo/comments"
post_api = "https://my-json-server.typicode.com/typicode/demo/posts"


# Function for assign comments to post

def AssignCommentsToPost():
    # calling apis via requets module
    post_response = requests.get(post_api).json()
    comment_response = requests.get(comment_api).json()
    # defined a list
    all_post_list = []
    # for loop on all post list 
    for post in post_response:
        comments_list = []
        # for loop on all comments list
        for comment in comment_response:
            # checking if post and commet id match
            if post['id'] == comment['postId']:
                comments_list.append(comment)
        post['comments'] = comments_list
        all_post_list.append(post)
    # doing return combined data
    return all_post_list



# Calling above function
output = AssignCommentsToPost()
print(output)