from instagrapi import Client
import config
cl = Client()
cl.login(config.username,config.password)

media=cl.photo_upload(path="D:/Downloads/srk.jpg",caption="srk is love")

