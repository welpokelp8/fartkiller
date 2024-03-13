import requests

def kill_farts():
  while True:
    try:
      response = requests.delete("http://www.ovarit.com/*")
      print(f"Sent fluff data to Ovarit at {response.elapsed.total_seconds()} seconds")
    except requests.exceptions.RequestException as e:
      print(f"An error occurred: {e}")

      

if __name__ == "__main__":
  kill_farts()
