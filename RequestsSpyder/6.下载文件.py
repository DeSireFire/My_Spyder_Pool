import requests
with open("Sublime_Build_203207.dmg", "wb") as code:
    code.write(requests.get(url="https://download.sublimetext.com/Sublime%20Text%20Build%203207.dmg").content)