# coding: utf-8

import itchat, pyttsx3
from itchat.content import *

newInstance = itchat.new_instance()
newInstance.auto_login(hotReload=True, enableCmdQR=True, statusStorageDir='newInstance.pkl')
engine = pyttsx3.init()

@newInstance.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def reply(msg):
        print(msg.user['RemarkName'], ":", msg.text)
        engine.say("Message From" + msg.user['RemarkName'] + msg.text)
        engine.runAndWait()

@newInstance.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    print(msg.user['RemarkName'], ":", 'Received %s, look on phone' % msg.fileName)
    msg.download(msg.fileName)

@newInstance.msg_register(TEXT, isGroupChat = True)
def text_reply(msg):
    print("[Group]", msg.user['NickName'], '-', msg.actualNickName, ":", msg.text)
    engine.say("Message From Group" + msg.user['NickName'] + msg.actualNickName + msg.text)
    engine.runAndWait()

newInstance.run()
