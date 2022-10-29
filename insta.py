import time
import os
if os.path.isfile("config/follow_wallpaper_hd_uuid_and_cookie.json"):
	os.remove("config/follow_wallpaper_hd_uuid_and_cookie.json")

from instabot import Bot

image = 0
i = 0
bot = Bot()

bot.login(username="<username>", password="<password>")
print("sleeping")
time.sleep(10)
loc= ("images/") # all photos are in folder images 

while True:
	while i < 150:   # will post 149 images
			 photo = str(image)
			 bot.upload_photo(f"{loc}{image}.jpg",'<caption here>')
			 time.sleep(3600) #will wait for 1hour after posting
			 i +=1
			 image += 1
