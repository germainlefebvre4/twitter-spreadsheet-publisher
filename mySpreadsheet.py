"""
Spreadsheet data structure:

   | A    | B       | C     | D                
---|------|---------|-------|------------------|
 1 | Next | Message | Image | Publication date |
 --|------|---------|-------|------------------|
 2 |      | Oh my ! |       | 14/34/2020 15:34 | # Already published tweet
 3 | x    | Okey ;) |       |                  | < Tweet to be publisehd
 4 |      | Good !! |       |                  |

"""
import httplib2
import os
from datetime import datetime

from apiclient import discovery
from google.oauth2 import service_account


GCP_SVC_SCOPES = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]
GCP_SVC_SECRET_FILE = os.path.join(os.getcwd(), 'credentials.json')

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
SPREADSHEET_RANGE = os.getenv("SPREADSHEET_RANGE")

def getTweet():
    try:
        # Authenticate GCP with service account
        credentials = service_account.Credentials.from_service_account_file(GCP_SVC_SECRET_FILE, scopes=GCP_SVC_SCOPES)
        # Connect to Google Spreadsheet service
        service = discovery.build('sheets', 'v4', credentials=credentials)

        # Spreadsheet query
        request = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE)
        response = request.execute()

        message_selected = selectMessage(response.get("values"))

        message_all = response.get("values")
        #print(f"All messages: {message_all}")
    
        return message_selected
    
    except OSError as e:
        print(e)
    

def selectMessage(message_list):
    message_filter = [x for x in message_list if x[1] != ""]
    message_selected = [x[1] for x in message_filter if x[0] == "x"][0]

    print(f"Selected message: {message_selected}")
    return message_selected

def moveNextCursor():
    # Authenticate GCP with service account
    credentials = service_account.Credentials.from_service_account_file(GCP_SVC_SECRET_FILE, scopes=GCP_SVC_SCOPES)
    # Connect to Google Spreadsheet service
    service = discovery.build('sheets', 'v4', credentials=credentials)

    # Spreadsheet query
    request = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE)
    response = request.execute()
    message_all = response.get("values")

    # Determine the current line
    line_current = None
    for index, value in enumerate(message_all):
        if value[0] == "x":
          line_current = index + 2

    # Determine the next line
    if len(message_all) > (line_current-2+1):
        if message_all[line_current-2+1] != "":
            line_next = line_current+1
        else:
            line_next = 2
    else:
        line_next = 2

    # Show informations
    print(f"Current line: {line_current}")
    print(f"Next line: {line_next}")

    # Update current line in spreadsheet
    data = {
        'values' : [["", None, None, datetime.now().strftime("%d/%M/%Y %H:%M")]]
    }
    service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEET_ID, 
            body=data, 
            range=f"Queue!A{line_current}", 
            valueInputOption='USER_ENTERED').execute()

    # Update next line in spreadsheet
    data = {
        'values' : [["x"]]
    }
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, 
        body=data, 
        range=f"Queue!A{line_next}:D", 
        valueInputOption='USER_ENTERED').execute()

    return

