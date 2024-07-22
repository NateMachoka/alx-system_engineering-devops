# Run Software as Another User

This project includes a Bash script that allows you to run the `whoami` command as a specified user. It demonstrates how to execute commands with the privileges of another user using `sudo`.

## Requirements

- The script must be run on Ubuntu 20.04 LTS.
- All Bash script files must be executable.
- The first line of the script should be `#!/usr/bin/env bash`.
- The second line should be a comment explaining what the script does.
- The script should pass Shellcheck without errors.

## Usage

To use the script, execute it with the username you want to run the `whoami` command as:

```bash
./0-iamsomeoneelse <username>
