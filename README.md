
# Instagram Sent Request Deletion Script

This script helps you delete sent requests on Instagram.

## Prerequisites

- Python 3.x
- Google Chrome browser

## Setup Instructions

1. **Clone and Navigate to the Repository:**

   ```bash
   git clone https://github.com/cjs0h/Instagram-Sent-Follow-Request-Remover.git
   cd Instagram-Sent-Follow-Request-Remover
   ```

2. **Ensure you have Python installed.**

3. **Install Required Libraries:**

   ```bash
   pip install selenium
   pip install beautifulsoup4
   ```

4. **Download Google Chrome Driver:**

   - Go to [Google Chrome Help -> About Google Chrome](chrome://settings/help) to find your Chrome version number.
   - Download the ChromeDriver that matches your Chrome version from this link: 
     ```
     https://storage.googleapis.com/chrome-for-testing-public/{replace-with-your-version-number}/win64/chromedriver-win64.zip
     ```
   - Extract the downloaded ZIP file.

5. **Set Up ChromeDriver:**

   - Create a directory called `bin` in your `C:` drive.
   - Copy the extracted `chromedriver.exe` to `C:\bin`.
   - Add `C:\bin` to your system PATH.

6. **Download Your Instagram Data:**

   - Go to your Instagram settings and request to download your data.
   - Once the data is ready, download it and extract the sent requests HTML file.

7. **Edit the Script:**

   - Open the script file in a text editor.
   - Add your Instagram username and password to the script.

8. **Update HTML File Path:**

   - Change the HTML file path in the script to point to the location of your downloaded sent requests HTML file.

9. **Run the Script:**

   ```bash
   instagram-Sent-Follow-Request-Remover.py
   ```

   - If you have two-step verification enabled, be prepared to enter the code when the browser opens.

10. **Script Functionality:**

    - The script will remove all of the sent requests one by one with a 5-second delay.

## Disclaimer

This script is for educational purposes only. Use it at your own risk.
