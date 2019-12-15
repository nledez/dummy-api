import os
import getopt
import requests
import socket
import sys

from flask import Flask
app = Flask(__name__)


NAME  = os.environ.get('NAME',  'default')
BACK1 = os.environ.get('BACK1', 'https://api.github.com/users/nledez')
BACK2 = os.environ.get('BACK2', 'https://api.github.com/users/nledez/keys')


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hostname')
def hostname():
    return socket.gethostname()

@app.route('/name')
def name():
    return NAME

def get_url(url):
    r = requests.get(url)
    print('headers: {}'.format(r.headers))
    print('encoding: {}'.format(r.encoding))
    print('text: {}'.format(r.text))
    print('json: {}'.format(r.json()))
    return r.text

@app.route('/back1')
def back1():
    return get_url(BACK1)

@app.route('/back2')
def back2():
    return get_url(BACK2)

def usage():
    print('Usage:')
    print(sys.argv[0] + '--name=the_name')

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:v", [
            "help",
            "name=",
            "back1=",
            "back2=",
        ])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    name = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-n", "--name"):
            NAME = a
        elif o in ("--back1"):
            BACK1 = a
        elif o in ("-n", "--back2"):
            BACK2 = a
        else:
            assert False, "unhandled option"
    app.run(host='0.0.0.0')
