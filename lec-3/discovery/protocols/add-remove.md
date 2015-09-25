# Add and Remove Protocol


Add and Remove protocol is a commication implemented between ConvServer and DiscovServer.

ConvServer is a server provides converstion services, DiscovServer is acting as a DNS server, which provides ip and port number lookups for clients, who query a `unit1 <-> unit2` convertion. 

Once ConvServer is boot up, it needs to tell DiscovServer that its service `unit1 <-> unit2` is on market.

And DiscovServer will then help get it registered, so when clients query the information, DiscovServer will return the converting service provider ip and port number. 

When ConvServer is shut down, it needs to tell DiscovServer that its service is down. 

<img src="https://cdn.rawgit.com/wenhuizhang/dist-sys-exercises/lec_3_prototype/lec-3/discovery/img/add_remove.svg">


A basic datastructure for Add and Remove protocol is listed as below. 


| Property      | Protocol                              | 
| ------------- |:------------------------------------- | 
| Add           | ADD UNIT1 UNIT2 IPADD PORTNO          | 
| Remove        | REMOVE UNIT1 UNIT2 IPADD PORTNO       |  



## Add Protocol

Add 

## Remove Protocol 






### P.S.

If you are feeling ambitious, have someone make a figure with a tool like this: http://bramp.github.io/js-sequence-diagrams/

Then use http://rawgit.com/ for svg support. 
