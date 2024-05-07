import requests

def test_reponse():
    reponse = requests.get("https://f-to-c-microservice-a24a3db4caa7.herokuapp.com/convert?fahrenheit=")

    if reponse.status_code == 200:
        return reponse.json()
    elif reponse.status_code == 400:
        return f"Error with status code: {reponse.status_code}"
    else:
        return "Error not indicated"
    
if __name__ == "__main__":
    print(test_reponse())