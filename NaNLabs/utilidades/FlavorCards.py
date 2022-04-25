import requests
from random_word import RandomWords
import random
from utilidades.getFuntions import get_random_member,getLabel
from utilidades.decrypt import decrypt

key = decrypt("NzE4YmY4MDcyYmQ5YzVkOWM0NjE1MWNiMTJiOTg3NTg=")
token = decrypt("NzMxYjdjNWQyZDY2OTYwZjI5NDgyMWRhM2YwMDYzMzgxMzY0NjdmZTA3MDNlN2Q1YjZjMzE2YzhhNWY1MGFjOQ==")

def issue_card(card_name,description):
    url = f"https://api.trello.com/1/cards"
    querystring = {"name": card_name, "idList": "6266b7d00136df5b8778f69b", "desc":description, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id

def bug_card(description):
    url = f"https://api.trello.com/1/cards"
    r = RandomWords()
    card_name = "bug-{0}-{1}".format(r.get_random_word(),random.randint(1,100))
    randomMembers = get_random_member(key,token)
    querystring = {"name": card_name, "idList": "6266b7d00136df5b8778f69b", "desc":description,"idLabels":"6266c1d16f1dfb4c638b63a6","idMembers" : randomMembers, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id

def task_card(card_name,category):
    url = f"https://api.trello.com/1/cards"
    label = getLabel(category,key,token)
    querystring = {"name": card_name, "idList": "6266b7d00136df5b8778f69b", "idLabels":label, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id