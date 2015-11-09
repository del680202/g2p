# g2p
A Proxy that convert GET request to POST request

# Install
python setup install

# Usage
g2p.py --port 8080 [--config action.yaml]

#action.yaml

You can setup config file to support basic authentication

```
auth1:
    type: BasicAuthenticationAction
    match: 'www.example.com'
    user: 'test'
    password: 'test'
```
