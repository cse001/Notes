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





