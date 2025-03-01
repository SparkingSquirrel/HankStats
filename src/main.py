import requests
import json

def main():
    print("HankStats")
    r = requests.get('http://10.0.0.50/RAWSTATUS')
    print(r.status_code)
    #print(r.content)

    snake_data = json.loads(r.content)
    print(snake_data)

if __name__ == "__main__":
    main()