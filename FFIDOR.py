# I created this python script to automate testing for IDOR vulnerabilities.
import requests
import string
import random

# Define the target URL
url = 'https://example.com/some-page'

# Define the input fields to fuzz
fields = ['id', 'user_id', 'product_id']

# Define a set of characters to use for fuzzing
# This can be customized based on the target application
characters = string.ascii_letters + string.digits + '-_'

# Define a list of values to use for fuzzing
values = [
    '',   # empty value
    '0',  # zero value
    '1',  # integer value
    '99999',  # large integer value
    '0.0',  # float value
    '1.234',  # decimal value
    'true',  # boolean value
    'false',
    'null',  # null value
    '[]',  # empty array
    '{}',  # empty object
]

# Define a list of headers to fuzz
headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36 Edge/15.15063'},
]

# Define a function to generate random values
def generate_random_value(length=10):
    return ''.join(random.choice(characters) for i in range(length))

# Loop over the input fields and fuzz them with different techniques
for field in fields:
    # Fuzz with the predefined values
    for value in values:
        params = {field: value}
        response = requests.get(url, params=params)
        if response.status_code == 200 and 'Unauthorized Data' in response.text:
            print('IDOR Vulnerability Detected!')
            print('Field:', field)
            print('Value:', value)

    # Fuzz with random values
    for i in range(10):
        value = generate_random_value()
        params = {field: value}
        response = requests.get(url, params=params)
        if response.status_code == 200 and 'Unauthorized Data' in response.text:
            print('IDOR Vulnerability Detected!')
            print('Field:', field)
            print('Value:', value)

    # Fuzz with combinations of values
    for value1 in values:
        for value2 in values:
            value = f'{value1}/{value2}'
            params = {field: value}
            response = requests.get(url, params=params)
            if response.status_code == 200
            print('IDOR Vulnerability Detected!')
            print('Field:', field)
            print('Value:', value)
    # Finish script...
