# FFIDOR - FUZZ FOR INSECURE DIRECT OBJECT REFERENCES
### A python script to fuzz for IDOR vulnerabilities. 

### FFIDOR1 Description:
This script is designed to fuzz websites for Insecure Direct Object Reference (IDOR) vulnerabilities. It uses the Python requests library to send GET requests to the target URL with different input values for specified input fields. The script takes input arguments from the command line using argparse module, such as the target URL, input fields to fuzz, values to use for fuzzing, and characters to use for fuzzing.

The script defines a function generate_random_value() to generate random values for fuzzing. The input fields are looped over, and for each field, the script fuzzes with predefined values, random values, and combinations of predefined values. If a fuzzed value is found in the response text and the response status code is 200, the script prints a message indicating that an IDOR vulnerability has been detected and outputs the vulnerable input field and value. The script finishes after all input fields have been fuzzed.

### FFIDOR Description:
This script is a Python script that fuzzes (tests for vulnerabilities by inputting various types of data) the input fields of a web application. Specifically, it defines a target URL and a list of input fields to fuzz, as well as a set of characters to use for fuzzing and a list of values to use for fuzzing. The script then loops over each input field and fuzzes it with different techniques, including predefined values, random values, and combinations of values. For each input field, the script sends HTTP GET requests to the target URL with the fuzzed input and checks the response for the presence of the string "Unauthorized Data". If the response contains this string, the script prints a message indicating that an IDOR (Insecure Direct Object Reference) vulnerability has been detected, along with the field and value that triggered the vulnerability. Finally, the script ends.
