# Proxy Server

* Usage
    - Start Server1, Server2, ...., ServerN
    - Edit path.txt. Add Server1, server2, ... , ServerN
    - Start Proxy
    - Start Client to connect Proxy
    


#How to Execute: 

* Example 
    - start server `python convServer.py 3334`
    - start server `java ConvServer 3336`
    - start server  ...
    - start proxy on port 1112  `python ProxyServer.py 1112`
    - request `telnet 127.0.0.1 1112`
