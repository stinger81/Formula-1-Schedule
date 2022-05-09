import os.path
import json
import datetime

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']

if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
try:
    season = str(int(input('Enter Season to add (YYYY) ['+str(datetime.date.today().year)+']: ')))
except:
    season = str(datetime.date.today().year)

with open('Formula_1_events_'+str(season)+'_season.json', 'r') as f:
    events = json.load(f)

# get list of calendars
try:
    calList = []
    service = build('calendar', 'v3', credentials=creds)
    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            calList.append((calendar_list_entry['summary'], calendar_list_entry['id']))
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break
except:
    None

for i in range(len(calList)):
    print(str(str(i)+" - "+calList[i][0]))

print('WARNING:Iif no calender is sected will use default')

listID = input('Select Calendar (int)[None]: ')

calendarID = ''
if listID == '':
    calendarID = 'primary'
    listID = 'None'
    calName = 'None'
try:
    listID = int(listID)
except:
    raise SystemExit('Exiting Invalid List Selection')
    
if isinstance(int(listID), int):
    calendarID = calList[int(listID)][1]
    calName = calList[int(listID)][0]
else:
    raise SystemExit('Exiting Invalid List Selection')

print('Will add to the following calendar: '+str(listID)+" | "+calName+" | "+calendarID)

confirm = input('Confirm? ("CONFIRM") [None]: ')
if confirm == 'CONFIRM':
    pass
else:
    raise SystemExit('Exiting Calender NOT Confirmed')

print('The Following Events will be added:')

print('Name | Season | Start Time(UTC)')
print('----------------------------------------')
for i in events:
    print(i['summary']+" | "+i['start']['dateTime']+i['start']['timeZone'])
print('Confirm that the events above will be added to the following calendar: '+str(listID)+" | "+calName+" | "+calendarID)

confirm = input('Confirm? ("CONFIRM") [None]: ')
if confirm == 'CONFIRM':
    pass
else:
    raise SystemExit('Exiting Event List NOT Confirmed')

print('''
The events that were approved above will be added to the google calender selected.
This must manually be undone through google calender if you are not satisfied.
As per the GNU GPLv3 license, this software is provided as is, without warranty of any kind.
''')    

confirm = input('Confirm Adding to calender. This can not be undone through this program ("CONFIRM") [None]: ')
if confirm == 'CONFIRM':
    pass
else:
    raise SystemExit('Exiting NOT Confirmed')

for i in events:
    try:
        service = build('calendar', 'v3', credentials=creds)
        events_result = service.events().insert(calendarId=calendarID, body=i).execute()
        print('Event created: %s' % (events_result.get('htmlLink')))
        with open('events_added.txt', 'a') as f:
            f.write(str(events_result.get('htmlLink'))+'\n')
    except HttpError as error:
        print('An error occurred: %s' % error)
