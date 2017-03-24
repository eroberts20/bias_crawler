import requests



response = requests.post("http://text-processing.com/api/sentiment/",
  data={
    "text": "ettysburg College professor Allen C. Guelzo described Lincoln as “surrounded by smiling enemies,” which prompted him to embed his friends into army camps as well as some federal departments."
  }
)


print(response.status_code)
print(response.json())

pos_percent = response.json()["probability"]["pos"]
neg_percent = response.json()["probability"]["neg"]
neutral_percent = response.json()["probability"]["neutral"]
print(pos_percent, neg_percent, neutral_percent)
