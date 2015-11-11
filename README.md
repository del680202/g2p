# g2p
A Proxy that convert GET request to POST request

# Install
python setup install

# Usage
g2p.py --port 8080 [--config action.yaml]

```
http://host?url=target_url
http://host?url=target_url&src=target_src
```

url: Send POST request to target_url
src: Fetch resource from string of src is matched by target_src when result of target_url is html.

#action.yaml

You can setup config file to support basic authentication

```
auth1:
    type: BasicAuthenticationAction
    match: 'www.example.com'
    user: 'test'
    password: 'test'
```
