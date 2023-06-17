# This script is only designed for windows based Systems.

import os
import subprocess
import re

def is_pingable(ip):
    """Ping the IP to check if it's reachable."""
    print(f"Pinging IP: {ip}")
    try:
        output = subprocess.check_output(f"ping -n 1 -w 5000 {ip}", shell=True).decode()
        if 'Received = 1' in output:
            print(f"IP {ip} is reachable.")
            return True
        elif 'TTL expired in transit' in output:
            print(f"IP {ip} has TTL expired in transit.")
            return False
        else:
            print(f"IP {ip} is not reachable.")
            return False
    except Exception:
        print(f"Failed to ping IP {ip}.")
        return False

def extract_ips_from_file(file_name):
    """Extract IP addresses from the given file."""
    print(f"Reading IP addresses from file: {file_name}")
    with open(file_name, 'r') as file:
        content = file.readlines()

    ip_lines = [(line.strip(), re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line)) 
                for line in content]
    print(f"Read {len(ip_lines)} lines from file.")
    return ip_lines


def main():
    """Main function that reads the file and pings the IP addresses."""
    file_name = 'ips.txt'  # Replace this with your file name.
    ip_lines = extract_ips_from_file(file_name)
    failed_lines = []

    for line, ips in ip_lines:
        for ip in ips:
            if not is_pingable(ip):
                failed_lines.append(line)
                break  # If one IP in a line fails, no need to check the others


    if failed_lines:
        print("The following lines contain IPs that are not pingable or have TTL expired in transit:")
        for line in failed_lines:
            print(line)
    else:
        print("All IPs are pingable.")

    input("Press Enter to continue...")

if __name__ == "__main__":
    main()
