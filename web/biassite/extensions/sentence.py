import requests


def sentiment_api(text):
    if(text != ""):
        response = requests.post("http://text-processing.com/api/sentiment/",
          data={
            "text": text
          }
        )

        ret = {}
        try:
            ret["pos"] = response.json()["probability"]["pos"]
        except:
            ret["pos"] = 0
        try:
            ret["neg"] =  response.json()["probability"]["neg"]
        except:
            ret['neg'] = 0
        try:
            ret["neu"] = response.json()["probability"]["neutral"]
        except:
            ret['neu'] = 0
        '''
        print("request is here " ,response.status_code)
        print(response.json())

        pos_percent = response.json()["probability"]["pos"]
        neg_percent = response.json()["probability"]["neg"]
        neutral_percent = response.json()["probability"]["neutral"]
        '''
        ret = (text, ret)
        return ret
    else:
        return None
