import os
import json
from datetime import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Define the scope
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_sheets_service():
    """
    Authenticate and return Google Sheets API service
    """
    # Get credentials from environment variable
    creds_json = os.environ.get('GOOGLE_CREDENTIALS')
    if not creds_json:
        raise ValueError('GOOGLE_CREDENTIALS environment variable not set')
    
    # Parse credentials
    creds_dict = json.loads(creds_json)
    credentials = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    
    # Build the service
    service = build('sheets', 'v4', credentials=credentials)
    return service

def update_sheet(sheet_id, range_name, values):
    """
    Update Google Sheet with given values
    
    Args:
        sheet_id: The ID of the Google Sheet
        range_name: The A1 notation range (e.g., 'Sheet1!A1:B2')
        values: List of lists containing values to write
    """
    service = get_sheets_service()
    
    body = {
        'values': values
    }
    
    result = service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()
    
    print(f"{result.get('updatedCells')} cells updated.")
    return result

def append_to_sheet(sheet_id, range_name, values):
    """
    Append values to Google Sheet
    
    Args:
        sheet_id: The ID of the Google Sheet
        range_name: The A1 notation range (e.g., 'Sheet1!A:B')
        values: List of lists containing values to append
    """
    service = get_sheets_service()
    
    body = {
        'values': values
    }
    
    result = service.spreadsheets().values().append(
        spreadsheetId=sheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()
    
    print(f"{result.get('updates').get('updatedCells')} cells appended.")
    return result

if __name__ == '__main__':
    # Get Sheet ID from environment variable
    SHEET_ID = os.environ.get('SHEET_ID')
    if not SHEET_ID:
        raise ValueError('SHEET_ID environment variable not set')
    
    # Get current timestamp
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Example: Append timestamp to Sheet1
    # Modify this section according to your needs
    values = [
        [current_time, 'Auto-updated by GitHub Actions']
    ]
    
    # Append to sheet
    result = append_to_sheet(SHEET_ID, 'Sheet1!A:B', values)
    print(f'Successfully updated sheet at {current_time}')
