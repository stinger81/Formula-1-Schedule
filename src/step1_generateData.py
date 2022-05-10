from urllib.request import urlopen
import json
import datetime
"""
API Documnetation: https://documenter.getpostman.com/view/11586746/SztEa7bL
"""
schedule_link = "http://ergast.com/api/f1/current.json"

schedule_season = "http://ergast.com/api/f1/"


selectSeason = input("Enter Season to add (YYYY) [current]: ")
if len(selectSeason) == 4:
    schedule_link = schedule_season + selectSeason + ".json"

schedule = urlopen(schedule_link).read()
schedule_json = json.loads(schedule)

data = schedule_json["MRData"]

total_races = int(data['total'])

raceTable = data['RaceTable']

season = raceTable['season']

def buildEvent(EventName, country, locality, circuit, raceDate, raceTime, duration = 1):
    startDateTime, endDateTime = build_dateTime(raceDate, raceTime[:-1],duration)
    print(EventName+" | "+startDateTime)
    return {
        'summary': EventName,
        'location': country + ", " + locality + ", " + circuit,
        'description': EventName,
        'start': {
            'dateTime': startDateTime,
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': endDateTime,
            'timeZone': 'UTC',
        },

        'reminders': {
            'useDefault': True,
        }
    }
def build_dateTime(raceDate, raceTime,duration):
    startDateTime = raceDate + "T" + raceTime + "-00:00"
    date_format = "%Y-%m-%dT%H:%M:%S%z"
    endTime = datetime.datetime.strptime(raceDate + "T" + raceTime + "-0000", date_format)
    endTime = endTime + datetime.timedelta(hours=duration)
    endTime = endTime.strftime(date_format)
    endDateTime = endTime[:-5] + "-00:00"
    return startDateTime, endDateTime

print("""
0 - Grand Prix
1 - First Practice
2 - Second Practice
3 - Third Practice
4 - Qualifying
5 - Sprints
""")
to_include = input("Enter Events to include (comma searated integers) [0,1,2,3,4,5]: ")
if to_include == '':
    to_include = "0,1,2,3,4,5"
to_include =list(map(int, to_include.split(",")))


eventsList = []

for i in raceTable['Races']:
    raceName = i['raceName']
    
    country = i['Circuit']['Location']['country']
    locality = i['Circuit']['Location']['locality']
    circuit = i['Circuit']['circuitName']

    raceDate = i['date']
    raceTime = i['time']
    eventName = raceName + " - Grand Prix | "+season +' Season'
    if 0 in to_include:
        eventsList.append(buildEvent(eventName, country, locality, circuit, raceDate, raceTime,duration=2))
    if 1 in to_include:
        try:
            firstPractice = i['FirstPractice']
            eventName = raceName + " - First Practice | "+season +' Season'
            eventsList.append(buildEvent(eventName, country, locality, circuit, firstPractice['date'], firstPractice['time'],duration=1))
        except:
            firstPractice = None
    if 2 in to_include:
        try:
            secondPractice = i['SecondPractice']
            eventName = raceName + " - Second Practice | "+season +' Season'
            eventsList.append(buildEvent(eventName, country, locality, circuit, secondPractice['date'], secondPractice['time'],duration=1))
        except:
            secondPractice = None
    if 3 in to_include:
        try:
            thirdPractice = i['ThirdPractice']
            eventName = raceName + " - Third Practice | "+season +' Season'
            eventsList.append(buildEvent(eventName, country, locality, circuit, thirdPractice['date'], thirdPractice['time'],duration=1))
        except:
            thirdPractice = None
    if 4 in to_include:
        try:
            qualifying = i['Qualifying']
            eventName = raceName + " - Qualifying | "+season +' Season'
            eventsList.append(buildEvent(eventName, country, locality, circuit, qualifying['date'], qualifying['time'],duration=1))
        except:
            qualifying = None
    if 5 in to_include:
        try:
            sprint = i['Sprint']
            eventName = raceName + " - Sprint | "+season +' Season'
            eventsList.append(buildEvent(eventName, country, locality, circuit, sprint['date'], qualifying['time'],duration=1))
        except:
            sprint = None
    
with open('Formula_1_events_'+str(season)+'_season.json', 'w') as f:
    json.dump(eventsList, f)




