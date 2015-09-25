# Add and Remove Protocol


Add and Remove protocol is a commication protocol implemented between ConvServer and DiscovServer.

<img src="https://cdn.rawgit.com/wenhuizhang/dist-sys-exercises/lec_3_prototype/lec-3/discovery/img/arch.png" >


ConvServer is a server provides converstion services; DiscovServer is acting as a DNS server, which provides ip and port number lookups for clients, who query a `unit1 <-> unit2` convertion. 



<img src="https://cdn.rawgit.com/wenhuizhang/dist-sys-exercises/lec_3_prototype/lec-3/discovery/img/add_remove.svg">


A basic data structure for Add and Remove protocol is listed as below. 


| Property      | Protocol: ConvServer Send             | Protocol: ProxyServer Send             |
| ------------- |:------------------------------------- | :------------------------------------- | 
| Add           | ADD UNIT1 UNIT2 IPADD PORTNO          |  ADDED UNIT1 UNIT2 IPADD PORTNO        |
| Remove        | REMOVE UNIT1 UNIT2 IPADD PORTNO       |  REMOVED UNIT1 UNIT2 IPADD PORTNO      |



## Add Protocol

- Step 1: Once ConvServer is boot up, it needs to tell DiscovServer that its service `unit1 <-> unit2` is on market, and sending `ADD UNIT1 UNIT2 IPADD PORTNO`

- Step 2: And DiscovServer will then help get it registered, so when clients query the information, DiscovServer will return the converting service provider ip and port number, and sending `ADDED UNIT1 UNIT2 IPADD PORTNO`

- Step 3: If ConvServer did not get the replyed message, it simply perform ***Step 1*** again.  



## Remove Protocol 

- Step 1: When ConvServer is shut down, it needs to tell DiscovServer that its service is down, by sending `REMOVE UNIT1 UNIT2 IPADD PORTNO`. 

- Step 2: And DiscovServer will then help get it unregistered, so when clients query the information, DiscovServer will return the `Not Found` information. 

- Step 3: DiscovServer then send `REMOVED UNIT1 UNIT2 IPADD PORTNO` to ConvServer.

- Step 4: If ConvServer did not get the replyed message, it simply perform ***Step 1*** again.




### P.S.

- If you are feeling ambitious, have someone make a figure with a tool like this: http://bramp.github.io/js-sequence-diagrams/

- Then use http://rawgit.com/ for svg support. 
