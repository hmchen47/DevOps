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




## Getting Monitored Applications




## Summarizing Interpreting Python Scripts

- Summary
  - [original code](https://bit.ly/3pL8duZ)
  - [local Python copy](src/)

