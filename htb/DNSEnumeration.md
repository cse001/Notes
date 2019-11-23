# DNS Enumeration Techniques

### NSLookup

```bash
nslookup
> SERVER <IP>

Then try different ips and hostnames to get any enumerations
```

### DNS Reckon

```bash
dnsreckon -r ip/netmask

## Example dnsreckon -r 127.0.0.1/24
```

### Dig

```bash
dig axfr @ip
```

 



<hr>

Important Note :  DNS runs on port 53 and thus we can add that ip to the /etc/resolve.conf and will be able to access the domain names local to the machine.





