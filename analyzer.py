import re
from collections import Counter

log_file = "sample.log"

failed_ips = []
error_count = 0

with open(log_file, "r") as file:
    logs = file.readlines()

for line in logs:

    if "FAILED LOGIN" in line:
        ip = re.search(r'\d+\.\d+\.\d+\.\d+', line)

        if ip:
            failed_ips.append(ip.group())

    if "ERROR" in line:
        error_count += 1

ip_counter = Counter(failed_ips)

print("\n=== Threat Analysis Report ===\n")

print(f"Total Failed Logins: {len(failed_ips)}")
print(f"Total Errors: {error_count}\n")

print("Top Suspicious IPs:")

for ip, count in ip_counter.items():
    print(f"{ip} --> {count} failed attempts")

print("\nAnalysis Complete.")