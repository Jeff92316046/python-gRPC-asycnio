import client.client as clt

if __name__ == "__main__":
    client = clt.UnaryClient()
    while True:
        a = str(input())
        result = client.get_url(message=a)
        print(result)