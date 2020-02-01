#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
def read_file(json_to_read):
    with open(json_to_read, "r") as f:
        data=f.read().splitlines()
        data=data[0]
        return json.loads(data)
    
def write_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text)    

rankings=read_file("ranking.json")
heroids=read_file("character.json")
series=read_file("series.json")
file_to_write="result_ranking.txt"
text_to_write=""

for hero in rankings:
    heroid=hero['heroId']
    heroname=heroids[heroid]
    series_involved=[series["game"+series_id["id"]+".title"] for series_id in hero['seriesIds']]
    text_to_write += "Rank %s | Hero: %s | Vote count: %s | Series: %s \n" % (hero["rank"], heroname, hero["voteCount"], ", ".join(series_involved))

open(file_to_write, 'w').close()
write_file(file_to_write, text_to_write)

