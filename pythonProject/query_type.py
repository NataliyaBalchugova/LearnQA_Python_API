import requests

# params=
#
# data =
payload = {"method": "PUT"}
method = ['POST', 'GET', 'PUT', 'DELETE', 'HEAD', "value"]
real_methods = ['get', 'post', 'put', 'delete']

# 1
for method in real_methods:
    response = requests.request(method, "https://playground.learnqa.ru/ajax/api/compare_query_type")
    print(response.text)

# 2
response = requests.request("https://playground.learnqa.ru/ajax/api/compare_query_type", data = )




# response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
# response1 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
# response2 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
# response3 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
# print(response.text)
# print(response1)
# print(response2)
# print(response3)