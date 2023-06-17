# IP Pinger

This script is used to check the reachability of IP addresses by sending ICMP echo requests (pings). It reads a file containing IP addresses or network alarms and determines whether each IP is pingable or not. The script provides additional functionality by returning the full line of text associated with each IP.

## Prerequisites

Make sure you have the following requirements installed:

- Python 3.x
- Operating System: Windows

## Installation

1. Clone the repository:

```shell
git clone https://github.com/CalebFIN/TEXTFILEIPCHECK.git
```

2. Change to the project directory:

```shell
cd TEXTFILEIPCHECK
```

## Usage

1. Prepare a file named `ips.txt` in the project directory. The file should contain the IP addresses you want to check, with each IP on a separate line and any additional information related to the IP (such as NODE Name, Website, etc.).

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the script:

```shell
python script.py
```

4. The script will start pinging each IP address and display the results in the console, including the full line of text associated with each IP.

5. After all IPs have been pinged, the script will output whether all IPs are pingable or provide a list of lines that contain IPs that are not pingable or have TTL expired in transit.

6. Press Enter to exit the script.

Please note that this script is designed to work on Windows operating systems. If you are using a different operating system, you may need to modify the script accordingly.
