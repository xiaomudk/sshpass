#!/usr/bin/python
# coding=utf-8

import os
import sys
import getopt
import pexpect

def info():
    print "Automate SSH logins when you're forced to use password authentication"
    print "version 0.1"

def usage():
    print "   -p password   Provide password as argument (security unwise)"
    print "   -e            Password is passed as env-var \"SSHPASS\""
    print
    print "   -h            Show help (this screen)"
    print "   -V            Print version information"

def run_cmd(password,cmd):
    SSH_NEWKEY = r'Are you sure you want to continue connecting \(yes/no\)\?'
    KEY_PASSPHRASE = r'Enter passphrase for key.*:'

    print 'cmd->',cmd
    p = pexpect.spawn(cmd)
    index = p.expect([pexpect.EOF, pexpect.TIMEOUT, SSH_NEWKEY,'[Pp]assword: ',KEY_PASSPHRASE])
    if index == 0 or index == 1: # Timeout
        print 'ERROR!'
        print 'SSH could not login. Here is what SSH said:'
        print p.before
        sys.exit(1)
    if index == 2: # SSH does not have the public key. Just accept it.
        p.sendline('yes')
        p.expect(['[Pp]assword: ',KEY_PASSPHRASE])
    p.sendline(password)
    print p.read()

if __name__ == '__main__':

    if len(sys.argv) <=1:
        print "\033[31;1m[Error]===>no args!\033[0m"
        usage()
        sys.exit(0)

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'f:p:ehV',
        ["help","version",])
    except getopt.GetoptError,e:
        print "\033[31;1m[Error]===>",e,"\033[0m"
        usage()
        sys.exit(0)

    password = None

    for op,value in opts:
        if op == '-p':
            password = value
        elif op == '-e':
            password = os.getenv('SSHPASS')
        elif op in ['-h','--help']:
            usage()
            sys.exit(0)
        elif op in ['-V','--version']:
            info()
            sys.exit(0)
        else:
            usage()
            sys.exit(0)

    run_cmd(str(password),' '.join(args))

