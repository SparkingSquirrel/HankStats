import requests

def main():
    print("HankStats")
    r = requests.get('http://10.0.0.50/RAWSTATUS')
    print(r.status_code)
    print(r.content)

if __name__ == "__main__":
    main()