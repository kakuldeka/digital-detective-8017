# Mission 7 — How Computers Communicate

## 1. Task / objective

Understand how computers communicate over networks and how different networking concepts work together to exchange information.

The objective was to learn about LAN, MAN, WAN, DNS, routers, protocols, packet switching and the client-server model. I also used Terminal to test network connectivity, perform DNS lookups and understand what happens when a website is opened in a browser.

## 2. Work completed

### Task 7.1 — Explain network concepts

Explored the basic networking concepts and understood their roles in computer communication.

| Concept | Explanation | Example |
|---|---|---|
| LAN (Local Area Network) | A network that connects devices within a small geographical area, such as a home, office or computer lab. | Computers connected to the same network in a college lab. |
| MAN (Metropolitan Area Network) | A network that covers a city or a large campus area and can connect multiple smaller networks. | A network connecting different university buildings across a city. |
| WAN (Wide Area Network) | A network that covers large geographical areas and connects networks over long distances. | The Internet. |
| DNS (Domain Name System) | Translates human-readable domain names into IP addresses so devices can locate servers. | Resolving `example.com` into its IP addresses. |
| Router | Connects different networks and forwards data packets towards their destinations. | A Wi-Fi router connecting devices to the Internet. |
| Protocol | A set of rules that devices follow when communicating over a network. | HTTP, HTTPS, TCP and IP. |
| Packet switching | Divides data into smaller packets that travel across a network and are reassembled at their destination. | Sending a file over the Internet. |
| Client-server | A communication model in which a client requests a service or resource and a server provides it. | A browser requesting a webpage from a web server. |

### Task 7.2 — Observe network information

Used Terminal to check connectivity with a public example domain and inspect the DNS records associated with it.

#### 1. Connectivity test using ping

**Command:**

```bash
ping -c 3 example.com
```

**Observed output:**

```text
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=47 time=58.460 ms
64 bytes from 104.20.23.154: icmp_seq=1 ttl=47 time=69.009 ms
64 bytes from 104.20.23.154: icmp_seq=2 ttl=47 time=124.314 ms

--- example.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 58.460/83.928/124.314/28.880 ms
```

**Observations:**

| Information | Result |
|---|---|
| Destination | `example.com` |
| Resolved IPv4 address | `104.20.23.154` |
| Packets transmitted | 3 |
| Packets received | 3 |
| Packet loss | 0% |
| Minimum response time | 58.460 ms |
| Average response time | 83.928 ms |
| Maximum response time | 124.314 ms |

All packets received a response, with 0% packet loss during this test.

This helped me understand how a connectivity test can be used to check whether a destination is reachable and observe the time taken for packets to travel to it and back.

#### 2. DNS lookup using nslookup

**Command:**

```bash
nslookup example.com
```

**Observed output:**

```text
Server:		[redacted]
Address:	[redacted]#53

Non-authoritative answer:
Name:	example.com
Address: 172.66.147.243
Name:	example.com
Address: 104.20.23.154
```

**Observations:**

The lookup used the configured DNS resolver on port 53 and returned the resolved IPv4 addresses for `example.com`.

The result was marked as non-authoritative because it came from a DNS caching resolver rather than directly from an authoritative nameserver for the domain.

#### Answers

**1. What does a connectivity test help you check?**

A connectivity test helps determine whether a destination can be reached over a network. It can also provide information about response time and packet loss.

**2. What information does a DNS lookup display?**

A DNS lookup displays records associated with a domain name, such as its IPv4 and IPv6 addresses, depending on the query.

**3. What is the role of DNS when entering a website name in a browser?**

DNS resolves the website's domain name into an IP address, allowing the browser to locate the server hosting the website.

### Task 7.3 — What happens when you open a website?

Consider opening `https://example.com` in a web browser. The following steps describe the typical communication process.

1. **The browser receives the request:** The user enters a website URL. The browser acts as a client and identifies the domain name and resource that needs to be accessed.

2. **DNS resolves the domain name:** The browser or operating system checks available DNS caches. If necessary, it contacts a DNS resolver to obtain the IP address associated with the domain.

3. **A connection is established:** Using the resolved IP address, the browser locates the server. Routers forward packets through the network towards their destination. For HTTPS, a secure TLS connection is established over TCP.

4. **The client sends a request:** The browser sends an HTTP request to the server using the appropriate communication protocols.

5. **The server processes the request:** The server receives the request, processes it and sends an HTTP response containing the requested webpage and other resources.

6. **The browser displays the website:** The browser receives and interprets the response, loads the required resources and renders the webpage for the user.

This process allows a client and server to communicate using networking protocols while DNS and network devices help the request reach the correct destination.

## 3. Commands / tools used

| Command / Tool | Purpose |
|---|---|
| `ping -c 3 example.com` | Sends connectivity test requests to the example domain and displays response times and packet loss. |
| `nslookup example.com` | Looks up DNS information associated with a domain name. |
| Terminal | Used to execute network commands and observe their output. |

## 4. My understanding

I learned how computers communicate over networks and how different networking concepts work together.

A LAN connects devices within a small area, while a MAN covers a larger area such as a city. A WAN connects networks across much greater geographical distances. The Internet is a familiar example of a WAN.

I also understood the role of DNS in translating domain names into IP addresses. Instead of remembering numerical addresses for websites, users can enter readable domain names, and DNS helps the computer locate the corresponding servers.

Routers forward packets between networks, while protocols define the rules devices follow when exchanging information. Packet switching allows data to be divided into smaller packets and transmitted across a network.

The client-server model helped me understand how a web browser requests resources from a server and receives a response.

Testing connectivity using `ping` and performing DNS lookups using `nslookup` helped connect these concepts with actual network operations on my computer.

I also understood the basic sequence involved in opening a website, starting from entering its URL to resolving its domain, communicating with the server and displaying the returned webpage.

## 5. Difficulties faced

No major difficulties were encountered during the network checks. Commands executed successfully and returned usable results.

## 6. How I resolved them

No troubleshooting was required. Observed DNS and ping outputs, verifying that identifying local network information was redacted.

## 7. Evidence / files

- `README.md` — Contains the networking concepts, actual connectivity and DNS observations, command explanations and the website communication process.

The recorded network observations use the public example domain `example.com`. No personal IP address, Wi-Fi name or other identifying network details have been included.

## 8. Commit details

**Commit message:** `Explain networking concepts and website communication`

**Push status:** Successfully committed and pushed to GitHub.
