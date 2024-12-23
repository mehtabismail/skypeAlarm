
import os
import time
import pygame
from skpy import Skype, SkypeEventLoop, SkypeNewMessageEvent, SkypeApiException

# Define your Skype credentials
username = "mehtab.16465@gmail.com"
password = "OutsourceNZ@6402"
# List of chat IDs to listen for messages
chat_ids = ["8:live:shafqatbari786_1", "19:0ff473be1d2a4b108463561fdeaefd48@thread.skype", "8:live:mussadiqali8643", "8:saima_sharif1", "8:live:saima_sharif1"]

token_file = "skype_token.txt"  # This is where the token will be saved

# Path to your ringtone file
file_path = os.path.join(os.getcwd(), "ringtone_iphone_14_pro.mp3")

# Function to ring the bell using pygame
def ring_bell():
    try:
        pygame.mixer.init()  # Initialize the pygame mixer
        pygame.mixer.music.load(file_path)  # Load the ringtone
        pygame.mixer.music.play()  # Play the ringtone
        while pygame.mixer.music.get_busy():  # Wait for the ringtone to finish playing
            time.sleep(1)
        print("Ringtone finished playing.")
    except Exception as e:
        print(f"Error playing ringtone: {e}")

# Event loop for receiving Skype messages
class MySkype(SkypeEventLoop):
    def __init__(self, username, password, token_file):
        # Initialize Skype session, using token if available
        try:
            super(MySkype, self).__init__(username, password, tokenFile=token_file)
            print("Logged in using token file.")
        except SkypeApiException:
            print("Token file not found or expired. Logging in with credentials...")
            self.conn.writeToken()  # Write the token after logging in

    # Handle incoming events
    def onEvent(self, event):
        # Only handle new message events
        try:
            if (event.type == "ConversationUpdate" or event.type == "NewMessage") and event.chatId in chat_ids:
                try:
                    ring_bell()
                except Exception as e:
                    print(e)
        except:
            print("abnormal event data")
            # ring_bell()
# Create an instance of your Skype event loop
try:
    skype_event_loop = MySkype(username, password, token_file)
except Exception as e:
    print(f"Error: {e}")
    exit(1)

# Start listening for events
while True:
    try:
        # Listen for new messages continuously
        skype_event_loop.loop()
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(60)  # Wait for 1 minute before retrying



# from google.oauth2 import service_account
# from google.auth.transport.requests import Request

# # Path to your service account JSON file
# service_account_file = "../../Downloads/locumbridge-firebase-adminsdk-mcnbw-38310d543c.json"

# # Define the required scope for Firebase messaging
# scope = ["https://www.googleapis.com/auth/firebase.messaging"]

# # Create the credentials from the service account file
# credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes=scope)
# credentials.refresh(Request())

# # Print the access token
# print("Access Token:", credentials.token)
