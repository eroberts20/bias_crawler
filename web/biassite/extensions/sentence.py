import requests


def sentiment_api(text):
    response = requests.post("http://text-processing.com/api/sentiment/",
      data={
        "text": text
      }
    )

    ret = {}

    ret["pos"] = response.json()["probability"]["pos"]
    ret["neg"] =  response.json()["probability"]["neg"]
    ret["neu"] = response.json()["probability"]["neutral"]
    '''
    print("request is here " ,response.status_code)
    print(response.json())

    pos_percent = response.json()["probability"]["pos"]
    neg_percent = response.json()["probability"]["neg"]
    neutral_percent = response.json()["probability"]["neutral"]
    '''
    ret = (text, ret)
    return ret
