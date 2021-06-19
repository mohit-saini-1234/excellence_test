
# Question2 
# Check out this website https://reqres.in/
# It has a an api to get a list of users https://reqres.in/api/users?page=2
# This api is page wise, i.e there are a total 12 pages and u can get a list of users for each page by passing the page number.

# You need to write a function/code which will go through all pages and find the total number of users. 




# Solution 2

import requests

# comment and post api url
users_api = "https://reqres.in/api/users?page={{PageNumber}}"


# Function for get total number of users
def GetTotalUsersCount():
    # defined a blank link for users
    all_users_list = []
    # loop for get page numbers 0 to 12 as mentioned above there will be 12 pages only
    for i in range(1,13):
        # calling api for every page
        url = users_api.replace("{{PageNumber}}",str(i))
        # calling apis via requets module
        api_response = requests.get(url).json()
        # getting data list form api response
        data = api_response['data']
        # loop over users list
        for userObj in data:
            all_users_list.append(userObj)
    return len(all_users_list)


number_of_users = GetTotalUsersCount()
print(number_of_users)