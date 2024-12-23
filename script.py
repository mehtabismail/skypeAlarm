import os
import time
import pygame
from skpy import Skype, SkypeEventLoop, SkypeChats


# # Define your Skype credentials
username = "Shafqatbari786@gmail.com"
password = "Jazz@0303"
chatId = ["8:live:.cid.ba87c568a26eedc3", "19:0ff473be1d2a4b108463561fdeaefd48@thread.skype"]
file_path = "/Users/shafqatbari/Documents/ringtone_iphone_14_pro.mp3"
file_path = os.path.join(os.getcwd() ,"ringtone_iphone_14_pro.mp3")

# Initialize Skype object with your credentials
sk = Skype(username, password)


# Function to ring the bell in macOS
def ring_bell():
    print('a')
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    # process = subprocess.Popen(["start", file_path])
    # time.sleep(24)
    # process.terminate()
    print('b')


# Event handler for incoming messages
class MySkypeEventLoop(SkypeEventLoop):
    def __init__(self, username, password):

        super(MySkypeEventLoop, self).__init__(username, password)

    def onEvent(self, event):
        print(":=>  ", event)
        try:
            if (event.type == "ConversationUpdate" or event.type == "NewMessage") and event.chatId in chatId:
                try:
                    ring_bell()
                except Exception as e:
                    print(e)
        except:
            print("abnormal event data")

# Create an instance of your event loop    event.type == "ConversationUpdate" and 

skype_event_loop = MySkypeEventLoop(username, password)



# Get all chatId's
sk = Skype(username, password)
skc = SkypeChats(sk)
print("name:=>  ",skc.recent())
# Start listening for events
while True:
    try:
        skype_event_loop.loop()
    except Exception as e:
        print("[#] Error occur in event_loop : {}".format(e))
        ring_bell()
        time.sleep(60)

# import os

# # Directory to search for sound files
# directory = '/System/Library/Sounds/'

# # List all files in the directory
# files = os.listdir(directory)

# # Print all files in the directory
# print("Files in directory:")
# for file in files:
#     print(file)


