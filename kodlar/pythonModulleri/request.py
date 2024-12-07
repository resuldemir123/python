import request #bize http adteslerini getirir
import json

result=request.get("https://jsonplaceholder.typicode.com/todos")
result=json.loads(result.text())

print(result)

for i in result:
    print(i["title"])


