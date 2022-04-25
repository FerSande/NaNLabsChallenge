import logging
from fastapi import APIRouter,Request
from utilidades.FlavorCards import issue_card,bug_card,task_card

logging.basicConfig(level=logging.INFO)

router = APIRouter(responses={404: {"description": "Not found"}})

@router.post("/trello_tasks")
async def executeTrelloTasks(request: Request):
    body = await request.json()
    lista = list(body)
    for i in lista:
        typeTask = (i["type"])
        if typeTask == "issue":
            task = issue_card(i["title"],i['description'])
        elif typeTask == "bug":
            task = bug_card(i["description"])
        elif typeTask == "task":
            task = task_card(i["title"],i["category"])
    return task




