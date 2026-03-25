#!/usr/bin/python3

# INET4031
# Name: Neeraj Manavalan
# Date Created: 03/24/2026
# Date Last Modified: 03

# os: used to execute system commands
import os
# re: used to detect comment lines in input
import re
# sys: used to read input from stdin
import sys

def main():
    # Read each line from input file
    for line in sys.stdin:

        # Check if line starts with '#'
        match = re.match("^#", line)

        # Split line into fields using ':' delimiter
        fields = line.strip().split(':')

        # Skip lines that are comments OR that do not have exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Extracts user data
        username = fields[0]
        password = fields[1]

        # Format full name in correct order for /etc/passwd
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split group list into individual groups
        groups = fields[4].split(',')

        # Create new user
        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        os.system(cmd)

        # Set password
        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        os.system(cmd)

        # Assign user to groups
        for group in groups:
            # Skip '-' which means no group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)

if __name__ == '__main__':
    main()
