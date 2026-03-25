# This script includes an interactive dry-run mode

# The user is prompted to choose whether to run in dry-run mode (Y) or normal mode (N)
# In dry-run mode, the script prints the commands that would be executed without actually running them which allows 
# In normal mode, the script executes the commands to create users, set passwords, and assign groups
#!/usr/bin/python3

import os
import re
import sys

def main():
    # Ask user if they want dry-run mode
    choice = input("Run in dry-run mode? (Y/N): ").strip().lower()
    dry_run = (choice == 'y')

    for line in open("create-users.input"):

        # Check for comment line
        match = re.match("^#", line)

        # Split fields
        fields = line.strip().split(':')

        # Handles invalid or skipped lines
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print("Skipping commented line:", line.strip())
                else:
                    print("Skipping invalid line:", line.strip())
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        # Creates thew new user
        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        if dry_run:
            print("DRY RUN:", cmd)
        else:
            os.system(cmd)

        # Set password
        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        if dry_run:
            print("DRY RUN:", cmd)
        else:
            os.system(cmd)

        # Assign groups by loooping through each group and assiging the user
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                if dry_run:
                    print("DRY RUN:", cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
