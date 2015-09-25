# Lookup Protocol


Lookup protocol is a commication protocol implemented between ProxyServer and DiscovServer.


ProxyServer is accepting queries from clients and send them to DiscovServer, where proxy server is acting as a client in view of DiscovServer. DiscovServer is acting as a DNS server, which provides ip and port number lookups for clients, who query a `unit1 <-> unit2` convertion.  


<img src="https://cdn.rawgit.com/wenhuizhang/dist-sys-exercises/lec_3_prototype/lec-3/discovery/img/arch.png" >


A basic datastructure for Lookup protocol is listed as below. 


| Property          | Protocol: ProxyServer Send            | Protocol: DiscovServer Send           |
| ----------------- |:------------------------------------- | :------------------------------------ | 
| Lookup: Found     | LOOKUP UNIT1 UNIT2 IPADD PORTNO       |  FOUND UNIT1 UNIT2 IPADD PORTNO       |
| Lookup: NOT Found | LOOKUP UNIT1 UNIT2 IPADD PORTNO       |  NOT FOUND UNIT1 UNIT2                |



- If the `unit1 <-> unit2` convertion is found, then 

<img src="https://cdn.rawgit.com/wenhuizhang/dist-sys-exercises/lec_3_prototype/lec-3/discovery/img/lookup_found.svg">


- If the `unit1 <-> unit2` convertion is not found, then 

<img src="https://cdn.rawgit.com/wenhuizhang/dist-sys-exercises/lec_3_prototype/lec-3/discovery/img/lookup_not_found.svg">




### P.S.

- If you are feeling ambitious, have someone make a figure with a tool like this: http://bramp.github.io/js-sequence-diagrams/

- Then use http://rawgit.com/ for svg support. 
