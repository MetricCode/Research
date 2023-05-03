# Passive Recon
- Reconnaissance (recon) can be defined as a preliminary survey to gather information about a target. It is the first step in [The Unified Kill Chain](https://www.unifiedkillchain.com/) to gain an initial foothold on a system.
- In passive reconnaissance, you rely on publicly available knowledge which can we accessed from publicly available recouces without directly engaging with the target.
- It can include:
	- DNS lookup
	- Checking job ads realted to the target website
	- Reading articles about the target.

### WHOIS
- This is a request and response protocol that follows the RFC 3912 specification. 
- A whois server listens on port 43/tcp for incoming requests.
- The domain registrar is responsible for maintaining the WHOIS records for the domain names it is leasing. 
- The WHOIS server replies with various information related to the domain requested.

we can do this by;
```
whois example.com
```

By this, we get the name server, creation, update and expiration dates, country contact of the registrant e.t.c.

## nslookup and dig
- nslookup stands for name server lookup
```
// run on terminal
nslookup <DOMAIN_NAME>

// we can run the tool with several options
nslookup <OPTIONS> <DOMAIN_NAME> <SERVER>

- Server is the DNS server that you want to query. 
nslookup -type=A tryhackme.com 1.1.1.1 can be used to return all the IPv4 addresses used by tryhackme.com.
```

![image](https://user-images.githubusercontent.com/99975622/235809979-5fc3db2d-81a5-40ce-a010-351daaa6cc9e.png)


For additional DNS Queries, we can use dig.

We can use `dig DOMAIN_NAME`, but to specify the record type, we would use `dig DOMAIN_NAME TYPE`. Optionally, we can select the server we want to query using `dig @SERVER DOMAIN_NAME TYPE`.

-   SERVER is the DNS server that you want to query.
-   DOMAIN_NAME is the domain name you are looking up.
-   TYPE contains the DNS record type, as shown in the table provided earlier.

#### More info...
```
https://book.hacktricks.xyz/network-services-pentesting/pentesting-dns
```

## DNSDumper

- This is an online tool that is used to do dns queries.
- It can be used to discover all the subdomains of a domain.
- It  will return the collected DNS information in easy-to-read tables and a graph.
- It will also provide any collected information about listening servers.

## Shodan.io

- [Shodan.io](https://www.shodan.io/) can be helpful to learn various pieces of information about the client’s network, without actively connecting to it.
-  Furthermore, on the defensive side, you can use different services from Shodan.io to learn about connected and exposed devices belonging to your organization.
- Shodan.io tries to connect to every device reachable online to build a search engine of connected “things” in contrast with a search engine for web pages. Once it gets a response, it collects all the information related to the service and saves it in the database to make it searchable.

