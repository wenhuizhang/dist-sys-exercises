# Discovery Server

(in process)

  1. `simple.py` A server that calls different functions depending on whether a client sends a string where the first word is "set" or "get". Try to make this very flexible so it is easy to add different message types later (This is the most basic server prototype, and you should be able to reuse your old code)
  2. `print.py` A server that simply displays any messages that are sent to it.  (This will be useful for debugging/testing later on)
  3. `store.py` A server that can store a single value. For example a client sending `set value1` would cause the server to save the string `value1` in memory.  Later, if a client sends the message `get`, the server should return `value1`. (This will help you figure out how to build a "stateful" server, i.e., one that stores data and can return it later)
  4. conversion server and proxy,  when start, send a message to the 'print.py'. 

#How to Execute: 

* Example ConvServer and Proxy
    - start server `python ConvServer.py 3334`
    - start server `java ConvServer 3336`
    - start server  ...
    - start proxy on port 1112  `python ProxyServer.py 1112`
    - request `telnet 127.0.0.1 1112`

* Example print, store, simple are listed in file headers


