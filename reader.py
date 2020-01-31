import json
import ast

def read(json_to_read):
    with open(json_to_read, "r") as f:
        data=f.read().splitlines()
        data=data[0]
        return json.loads(data)

rankings=read("ranking.json")
heroids=read("character.json")

for hero in rankings:
    heroid=hero['heroId']
    heroname=heroids[heroid]
    print("Rank %s | Hero: %s | Vote: %s" % (hero["rank"], heroname, hero["voteCount"]))
    
