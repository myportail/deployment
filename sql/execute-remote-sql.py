import argparse
from paramiko import SSHClient

sqlCommands = [
    {
        'database': None,
        'cmd': 'CREATE DATABASE test2;'
    }
]

parser = argparse.ArgumentParser(description='run sql scripts remotely')

parser.add_argument('--server', required=True, nargs='?', dest='server', help='server address')
parser.add_argument('--username', required=True, nargs='?', dest='username', help='server username')
parser.add_argument('--password', required=True, nargs='?', dest='password', help='server password')
parser.add_argument('--sqlusername', required=True, nargs='?', dest='sqlusername', help='sql username')
parser.add_argument('--sqlpassword', required=True, nargs='?', dest='sqlpassword', help='sql password')
parser.add_argument('--var', metavar='N', dest='variables', nargs='*', action="append", help='variables')

args = parser.parse_args()
print(args)

ssh = SSHClient()
ssh.load_system_host_keys()

# sshConnString = args.username + ':' + args.password + '@' + args.server
# print(sshConnString)

ssh.connect(hostname=args.server, username=args.username, password=args.password)
# ssh.connect(sshConnString)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls -al')
print(ssh_stdout.read()) #print the output of ls command
# print(ssh_stderr)

for cmd in sqlCommands:
    sshCmd = 'mysql --user=\''+ args.sqlusername + '\' --password=\'' + args.sqlpassword + '\''

    if cmd['database'] is not None:
        sshCmd += ' --database=\'' + cmd['database'] + '\''

    if cmd['cmd'] is not None:
        sshCmd += ' --execute=\'' + cmd['cmd'] + '\''

    print(sshCmd)

    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(sshCmd)
    print(ssh_stdout.read())
    print(ssh_stderr.read())

