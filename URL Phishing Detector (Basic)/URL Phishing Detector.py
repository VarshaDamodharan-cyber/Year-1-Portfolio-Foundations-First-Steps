def is_phishing(url):
    if "@" in url or "-" in url or url.count(".") > 3:
        return True
    return False

urls = [
    "https://secure-login.com@evil.com",
    "https://example.com",
    "http://pay-pal.verify-login.com"
]

for u in urls:
    print(u, "->", "Phishing ⚠️" if is_phishing(u) else "Safe ✅")
