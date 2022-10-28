# ##########################################################################
# 
#   Copyright (C) 2021-2022 stinger81
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#   stinger81 - GitHub
#
# ##########################################################################

import json
import os

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

with open('events_added.json', 'r') as f:
    added_events = json.load(f)

for i in added_events:
    print(i['summary']+" | "+i['id']+" | "+i['start']['dateTime'])
confirm = input('Will Remove all of the events listed ("CONFIRM") [None]: ')
if confirm == 'CONFIRM':
    pass
else:
    raise SystemExit('Exiting NOT Confirmed')

SCOPES = ['https://www.googleapis.com/auth/calendar']

if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

events  = added_events.copy()
for i in added_events:
    try:
        service = build('calendar', 'v3', credentials=creds)
        service.events().delete(calendarId=i['organizer']['email'], eventId=i['id']).execute()
        print('Event Deleted: %s' % (i['summary']))
        events.pop(0)
    except HttpError as error:
        print('An error occurred: %s' % error)

with open('events_added.json', 'w') as f:
    json.dump(events.clear(), f)