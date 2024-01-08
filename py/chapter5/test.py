import http.client

conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
    'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
}

conn.request("GET", "/v3/teams/statistics?league=39&season=2020&team=33", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))