# F1 Schedule Import Tool

```
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
```

# Add Formula 1 Schedule to Google Calender ![Version](https://img.shields.io/badge/python-v3-green) ![Version](https://img.shields.io/github/v/release/stinger81/Formula-1?include_prereleases)
- [Summary](#summary)
- [Google Development API](#google-API)
- [Required Python Libraries](#libraries)
<!--- - [Future Plans](#future)-->

<a name = 'summary'></a>
## Summary
This program is designed to be executed in three distinct steps. This will allow for the end user to remove specific races from a generated json file if needed. As well as to allow for past season to be uploaded to Google Calender if needed.

There are multiple places where authorization is needed ensure that it is typed correctly.

Execute the scripts in the following order:
1. step0_quickstart.py
    - Check that Google Cloud API is configured correctly. Must exit with no errors and show up coming calender event to move on.
2. step1_generateData.py
    - Get currnet race times from the internet and then save them to a json file
3. step2_add_to_Google_Calender.py
    - Will take the generated json file and then add it to the selected Google Calender.
<a name = 'google-API'></a>
## Google Development API

Must set up Google Development API Client to add to calender
- [Google Developers Website](https://developers.google.com/)
- [Google Cloud Platform](https://console.cloud.google.com/apis/dashboard)
- [Google Calender for Developers](https://developers.google.com/calendar/api/quickstart/python)

Ensure that your email is registered as a test user in order to get private token.

From main dashboard execute the following steps to add test user
1. APIs & Services -> Credential
2. Select OAuth consent screen
3. Add authorized users under test users (Max 100 users on free plan)

<a name = 'libraries'></a>
## Required Python Libraries
- json
- os
- datetime
- urllib
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib



