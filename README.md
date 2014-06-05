# Setting up

 1. Install virtualenvironment
 ```$ virtualenv venv
New python executable in venv/bin/python
Installing Setuptools..............................................................................................................................................................................................................................done.
Installing Pip.....................................................................................................................................................................................................................................................................................................................................done.```
 2. Load virtualenv ```$ . venv/bin/activate```
 3. Install the requirements ```pip install -r requirements.txt```

# Running token generation
```
> python token_generator.py

```

This will tell you to go to a signed url to generate your key. Ex:
```
$ python token_generator.py 
Request Token:
    - oauth_token        = 1O88gBzC0p6UBvrECdaFHCZv0WxHmG0qV7rLXURqXI
    - oauth_token_secret = 49zxmuNK9yhRXtJXCSpKAqm1VLqiy2zWz1i8bpfvQ

Go to the following link in your browser:
https://api.twitter.com/oauth/authorize?oauth_token=1O88gBzC0p6UBvrECdaFHCZv0WxHmG0qV7rLXURqXI

What is the PIN? 682****
Access Token:
    - oauth_token        = 432782577-32pqGCYe0fpOafZSSQ3yp0wD5vtzXNT44cUDDwW3
    - oauth_token_secret = DzHG56Vfpuft0mHjh23ntLjOwUo3gcMsQuJa6gn7oTLtf

You may now access protected resources using the access tokens above.
```

You can then use the generated values in the client
