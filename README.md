# Google Sheets Automation with GitHub Actions

Automated Python script to update Google Sheets every 5 minutes using GitHub Actions. This project demonstrates how to use GitHub Actions as a free scheduler to periodically update a Google Spreadsheet.

## Features

- ⏰ **Automated Updates**: Runs every 5 minutes using GitHub Actions cron schedule
- 🔄 **Continuous Operation**: No server maintenance required
- 🔐 **Secure**: Uses GitHub Secrets to store sensitive credentials
- 📊 **Google Sheets Integration**: Full read/write access to your spreadsheets
- 🚀 **Easy Deployment**: Simple setup process

## Prerequisites

- GitHub account
- Google Cloud Platform account
- Google Sheets spreadsheet

## Setup Instructions

### 1. Create Google Cloud Project and Enable APIs

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the **Google Sheets API**:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Google Sheets API"
   - Click "Enable"

### 2. Create Service Account

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "Service Account"
3. Fill in the service account details and click "Create"
4. Skip optional steps and click "Done"
5. Click on the created service account
6. Go to "Keys" tab
7. Click "Add Key" > "Create new key"
8. Choose JSON format and click "Create"
9. Save the downloaded JSON file securely

### 3. Share Google Sheet with Service Account

1. Open your Google Sheet
2. Click the "Share" button
3. Add the service account email (found in the JSON file as `client_email`)
4. Give it "Editor" permission
5. Copy your Sheet ID from the URL: `https://docs.google.com/spreadsheets/d/SHEET_ID/edit`

### 4. Configure GitHub Repository Secrets

1. Go to your repository on GitHub
2. Navigate to "Settings" > "Secrets and variables" > "Actions"
3. Add the following secrets:

   **GOOGLE_CREDENTIALS**
   - Click "New repository secret"
   - Name: `GOOGLE_CREDENTIALS`
   - Value: Paste the entire content of the JSON file you downloaded
   - Click "Add secret"

   **SHEET_ID**
   - Click "New repository secret"
   - Name: `SHEET_ID`
   - Value: Your Google Sheet ID
   - Click "Add secret"

## How It Works

1. **GitHub Actions Workflow** (`.github/workflows/update_sheets.yml`):
   - Triggers every 5 minutes using cron schedule: `*/5 * * * *`
   - Can also be triggered manually via workflow_dispatch
   - Sets up Python environment
   - Installs dependencies from `requirements.txt`
   - Runs the Python script with credentials from secrets

2. **Python Script** (`update_sheets.py`):
   - Authenticates using Google Service Account credentials
   - Connects to Google Sheets API
   - Appends timestamp and message to Sheet1
   - Can be customized for your specific use case

## Customization

### Modify Update Frequency

Edit the cron schedule in `.github/workflows/update_sheets.yml`:

```yaml
schedule:
  - cron: '*/5 * * * *'  # Every 5 minutes
  # - cron: '0 * * * *'    # Every hour
  # - cron: '0 0 * * *'    # Every day at midnight
```

### Customize Data Being Written

Modify the `update_sheets.py` script:

```python
# Example: Add custom data
values = [
    [current_time, 'Your custom message', additional_data]
]
```

### Change Sheet and Range

Update the range in `update_sheets.py`:

```python
# Current: Sheet1!A:B
result = append_to_sheet(SHEET_ID, 'Sheet1!A:B', values)

# Change to: MySheet!A:D
result = append_to_sheet(SHEET_ID, 'MySheet!A:D', values)
```

## Manual Trigger

To manually run the workflow:

1. Go to "Actions" tab in your repository
2. Select "Update Google Sheets" workflow
3. Click "Run workflow"
4. Select branch and click "Run workflow"

## Monitoring

- Check workflow runs in the "Actions" tab
- View logs for each run to debug issues
- Monitor your Google Sheet for updates

## Important Notes

⚠️ **GitHub Actions Limitations**:
- Free tier: 2,000 minutes/month for private repos
- Public repos: Unlimited minutes
- Workflows running every 5 minutes use approximately 8,640 minutes/month

⚠️ **Google Sheets API Quotas**:
- 500 requests per 100 seconds per project
- 100 requests per 100 seconds per user

## Troubleshooting

### Workflow Not Running
- Check if Actions are enabled in repository settings
- Verify cron syntax is correct
- Ensure repository is not archived

### Authentication Errors
- Verify `GOOGLE_CREDENTIALS` secret contains valid JSON
- Check if service account has access to the sheet
- Ensure Google Sheets API is enabled

### Permission Denied
- Share the sheet with service account email
- Grant "Editor" permission to service account

## License

MIT License - Feel free to use this project for your needs.

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## Support

If you encounter any issues, please create an issue in this repository.
