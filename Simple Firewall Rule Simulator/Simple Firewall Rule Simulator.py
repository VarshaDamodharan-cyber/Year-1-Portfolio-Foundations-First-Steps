def firewall(ip, whitelist):
    if ip in whitelist:
        return "ALLOWED ✅"
    else:
        return "BLOCKED ❌"

whitelist = ["192.168.1.10", "127.0.0.1"]
ips = ["192.168.1.10", "10.0.0.5", "127.0.0.1"]

for ip in ips:
    print(ip, "->", firewall(ip, whitelist))
