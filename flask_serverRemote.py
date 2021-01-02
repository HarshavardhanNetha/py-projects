from flask import Flask
import subprocess
import urllib.parse


app=Flask('__main__')


@app.route("/")
def home():
    
    hello(x)
@app.route("/a/<cmd>")
def hello(cmd):
    #x=urllib.parse.quote_plus(cmd)
    cmd="cd myproject &"+cmd
    print(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return output,p_status

if __name__ == '__main__':
    app.run()
