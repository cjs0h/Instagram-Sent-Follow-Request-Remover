from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_instagram(driver, username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(25)

def extract_usernames_from_html(html_path):
    # Load the HTML file
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the elements that contain the usernames
    usernames = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/'):
            username = href.split('/')[1]
            if username and username not in usernames:
                usernames.append(username)
    return usernames

def cancel_follow_requests(driver, usernames):
    for username in usernames:
        try:
            driver.get(f"https://www.instagram.com/{username}/")
            time.sleep(2)

            # Wait for the "Requested" button to be clickable and click it
            requested_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Requested']]4"))
            )
            requested_button.click()
            time.sleep(1)

            # Wait for the "Unfollow" button in the pop-up and click it
            unfollow_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Unfollow']"))
            )
            unfollow_button.click()
            time.sleep(1)

            print(f"Cancelled follow request for {username}")
        except Exception as e:
            print(f"Could not cancel follow request for {username}: {e}")


# Replace these with your Instagram login credentials and the path to the HTML file
INSTAGRAM_USERNAME = "username"
INSTAGRAM_PASSWORD = "password"
html_path = '/path/to/html'

# Set up the Selenium driver (make sure to download the correct ChromeDriver)
driver = webdriver.Chrome()

# Log in to Instagram
login_instagram(driver, INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

follow_requests = extract_usernames_from_html(html_path)
# Cancel follow requests
cancel_follow_requests(driver, follow_requests)

# Close the browser
driver.quit()
