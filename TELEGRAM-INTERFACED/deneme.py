import ast
userDict = {"username": "whilefalse27", "channel-data": {"said's group": "-642743936", "avi's group": "-1001668532284", "denemechannel": "-343"}, "post-data": {"said": "what a nice text for test", "berk": "deneme", "deneme": "denemenenem"}, "folder-data": {"folder1": ["berk"], "folder2": ["sadecebu"]}}

print(userDict["channel-data"])
userDict["channel-data"].pop("said's group")
print(userDict["channel-data"])
