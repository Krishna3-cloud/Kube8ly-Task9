#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

f = cgi.FieldStorage()

# Launch Deployment
deployname = f.getvalue("deployname")
imgname = f.getvalue("deployimage")

start_deploy = subprocess.getoutput("kubectl create deployment {} --image={} --kubeconfig admin.conf".format(deployname,imgname))
print(start_deploy)
print("\n\n Deployment {} launched successfully ....\n\n".format(deployname))

