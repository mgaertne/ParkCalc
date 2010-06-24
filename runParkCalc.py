#! /usr/bin/env python

"""Runner Script for EWT19

Tests are run by giving a path to the tests to be executed as an argument to
this script. Possible Robot Framework options are given before the path.

Examples:
  runParkCalc.py parkCalc1                          # Run all tests in a directory
  runParkCalc.py parkCalc1/calc1.txt                # Run tests in a specific file
  runParkCalc.py --variable BROWSER:IE parkCalc1    # Override variable
  runParkCalc.py -v BROWSER:IE -v DELAY:0.5 parkCalc1

By default tests are executed with Firefox browser, but this can be changed
by overriding the `BROWSER` variable as illustrated above. Similarly it is
possible to slow down the test execution by overriding the `DELAY` variable
with a non-zero value.

When tests are run, the demo application and Selenium Server are started and
stopped automatically. It is possible to start and stop them also separately
by using `demoapp` and `selenium` options. This allows running tests with the
normal `pybot` start-up script, as well as investigating the demo application.

Running the demo requires that Robot Framework, SeleniumLibrary, Python, and
Java to be installed. For more comprehensive instructions, see the demo wiki
page at `http://code.google.com/p/robotframework-seleniumlibrary/wiki/Demo`.
"""

import os
import sys
from tempfile import TemporaryFile
from subprocess import Popen, call, STDOUT

try:
    import SeleniumLibrary
except ImportError:
    print 'Importing SeleniumLibrary module failed.'
    print 'Please make sure you have SeleniumLibrary installed.'
    sys.exit(1)

ROOT = os.path.dirname(os.path.abspath(__file__))

def run_tests(args):
    start_selenium_server()
    call(['pybot'] + args, shell=(os.sep == '\\'))
    stop_selenium_server()

def start_selenium_server():
    logfile = open(os.path.join(ROOT, 'selenium_log.txt'), 'w')
    SeleniumLibrary.start_selenium_server(logfile)

def stop_selenium_server():
    SeleniumLibrary.shut_down_selenium_server()

def print_help():
    print __doc__

def print_usage():
    print 'Usage: runParkCalc.py [options] datasource'
    print '   or: runParkCalc.py help'


if __name__ == '__main__':
    action = {'help': print_help,
              '': print_usage}.get('-'.join(sys.argv[1:]))
    if action:
        action()
    else:
        run_tests(sys.argv[1:])
