# Py Port Scanner
Super fast port scanner written in Python.

It uses multiprocessing to utilize all cores and speed up the scanning.

## How to use
Run `python3 portscanner.py <options>` to scan. By default, it scans all ports on the local machine.
> Use python instead of python3 if you are using windows.

## Options
- Use `-h` to get help
- Use `-p <port_number>` to check for a specific port.
- Use `-i <ip_address>` to scan for another IP Address.
