from urllib.parse import urlparse
url = 'https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/'
parsed_url = urlparse(url)
print(parsed_url.scheme)    #it print https
print(parsed_url.netloc)    # it print domain name
print(parsed_url.path)      #prints path to page
print(parsed_url.query)     #prints parameter values
print(parsed_url.fragment)   #prints fragments
