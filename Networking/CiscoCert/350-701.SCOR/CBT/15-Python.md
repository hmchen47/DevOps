# 15. Interpret Basic Python Scripts used with Cisco Security

Trainer: Knox Hutchinson


## Introducing Basic Python Security Scripts

- Learning goals
  - Python scripts
  - impact on Cisco security platform
  - authentication w/ Python scripts
  - monitoring w/ Python scrippts



## Extending Python and Setting Variables

- Python fundamentals
  - task: get a list of FirePower management center apps
  - import libraries
    - `json`: working w/ JSON data format
    - `sys`: working w/ actual operating system
    - `requests`: perform HTTP requests w/ REST API
  - other important libraries for 
    - `ncclient`: working w/ Netconf protocol
    - `lxml`: workign w/ XML data
    - `openpyxl`: working w/ excel file
    - `selenium`: emulate web browser
  - global variables
    - `url`: base URL of DevNet Sandbox
    - `login_url`: generated token for FirePower authentication
    - `headers`: specify what kind of data to request and post
    - `user` & `pw`: username and password, insecure way

  ```python
  import sys
  import json
  import requests

  # Set up global variables
  url = "https://fmcrestapisandbox.cisco.com"
  login_url = "/api/fmc_platform/v1/auth/generatetoken"
  headers = {"Content-Type": "application/json"}

  user = "knox"
  pw = "BtNdJM9k"
  ```


## Getting Authenticated

- Retrieving token from FirePower Sandbox in DevNet
  - task: login to web to get token
  - FirePower mgmt center sending back a token if login successfully
  - web browser using the token to work on proceeding activities
  - try-except block to handle error, same as try/catch block in other languages
  - HTTP methods
    - `requests.post`:
      - submit a request w/ data
      - `auth=(user, pw)`: authenticating `user` w/ the password `pw`
      - `verify=False`: not using self-signed certificate for authentication
    - `requests.get`: retrieve HTML doc
  - obtain token from response headers:
    - extract headers from response:`resp_headers = login_response.headers`
    - get token from header: `token = resp_headers.get("X-auth-access-token", default=None)`
    - not token existed $\to$ exit the program
  - add retrieved token into own headers: `headers["X-auth-access-token"] = token`


  ```python
  try:
      # POST the login ans password to the login endpoint
      login_response = requests.post(f"{url}{login_url}", auth=(user, pw), verify=False)

      # Parse out the headers
      resp_headers = login_response.headers

      # Grab the token from the response headers
      token = resp_headers.get("X-auth-access-token", default=None)
      if token == None:
          print("Failed to get a token. Try again")
          sys.exit()

      # Set the token in the headers to be used in the next call
      headers["X-auth-access-token"] = token
  except Exception as err:
      print(f"error raised! {err}")
  ```


## Getting Monitored Applications

- Retrieving monitoring data from FirePower in DevNet Sandbox
  - utilizing the token retrieved from login
  - `e276abec-e0f2-11e3-8169-6d9ed49b625f`: get from the FirePower Management Center doc
  - `requests.get`: retrieve data from specified apps
    - `headers=headers`: using token within headers for authentication
    - `.json()`: parsing return data into JSON format
  - JSON just a formated text string
  - print JSON in formated output: `print(json.dumps(apps_response, indent=2, sort_keys=True))`

  ```python

  # Get monitored apps
  apps_url = (
      "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/applications"
  )

  try:
      apps_response = requests.get(
          f"{url}{apps_url}", headers=headers, verify=False
      ).json()

      print(json.dumps(apps_response, indent=2, sort_keys=True))
  except Exception as err:
      print(f"error raised! {err}")
  finally:
      if apps_response:
          apps_response.close()
  ```


## Summarizing Interpreting Python Scripts


