import sys, os
filename = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(1, filename)
from zoomapi import JWTZoomClient

import json
from configparser import ConfigParser

api_key = "ZvOczog1SO2jhyj9OAQclg"
api_secret = "BICOCB5GBjkahFZTVhpAnCdpNHDqO8EuLR8T"

# print(f'id: {api_key} secret: {api_secret}')


def run():
    
    client = JWTZoomClient(api_key, api_secret)

    user_list_response = client.user.list()
    user_list = json.loads(user_list_response.content)

    # print (user_list)

    for user in user_list['users']:
        user_id = user['id']
        print(json.loads(client.meeting.list(user_id=user_id).content))

    print ('---')

    meetings_list = client.meeting.list(user_id='franklinselva10@gmail.com')
    print(json.loads(meetings_list.content))

    meeting = client.meeting.create
    
    print ('---')
    recording_list = client.recording.list(user_id='franklinselva10@gmail.com')
    
    print(recording_list)
    
    
if __name__ == "__main__":
    run()