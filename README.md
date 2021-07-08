# Py Port Scanner
Superfast port scanner written in Python.

It uses multiprocessing to utilize all cores and speed up the scanning.

## How to use
Run `./portscanner.py <options>` to scan. By default, it scans all ports on the local machine.
> Note: if the above command doesn't work then make `portscanner.py` executable by running `chmod +x portscanner.py`

## Options
- Use `-h` to get help
- Use `-p <port_number>` to check for a specific port.
- Use `-i <ip_address>` to scan for another IP Address.
