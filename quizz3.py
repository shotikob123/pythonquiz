import requests
import json
#
# url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"
#
# querystring = {"league":"39","season":"2020","team":"33"}
#
# headers = {
#     'x-rapidapi-key': "cdb4221587msh1abbf742983ebcdp1df4bdjsn83be88b96ffb",
#     'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
#     }
# დავალება 1. ეს requests მოდულის 4 ფუნქცია/ატრიბუტი
# response = requests.get(url, headers=headers, params=querystring)
# print(requests.status_codes)
# print(response.text)
# print(response.headers)

# # ეს დავალება 2
# res = json.loads(response.text)
# print(json.dumps(res, indent=4))
#
# ეს დავალება 3. მანჩესტერის ლოგოს კოდი მომაქვს APIდან, ფაილს ვხსნი wb რეჟიმში და ვწერ ამ კოდს შიგნით.
# შედეგი იქნება png სურათი, მანჩესტერის ლოგოთი.
# logo = res["response"]['team']['logo']
# resp = requests.get(str(logo))
# with open('mu.png', 'wb') as mu:
#     mu.write(resp.content)

# დავალება 4
# წესით სწორად უნდა დამეწერა, ვერ ვამოწმებ ცხრილი შეიქმნა თუარა.
# რაღაც ამერია ფაიჩარმში და დათაბეიზის ცხრილს ვეღარ ვხედავ :დ
# import sqlite3
# conn = sqlite3.connect('Quiz.sqlite')
# games = res['response']['fixtures']['played']['total']
# wins = res['response']['fixtures']['wins']['total']
# draws = res['response']['fixtures']['draws']['total']
# loses = res['response']['fixtures']['loses']['total']
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS quizz (
#             games integer,
#             wins integer,
#             draws integer,
#             loses integer)''')
# #
# insert = f"INSERT INTO quizz VALUES ({games}, {wins}, {draws}, {loses})"
# c.execute(insert)
# conn.commit()
# conn.close()

