#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

f = cgi.FieldStorage()

# Launch Pod
podname = f.getvalue("podname")
imgname = f.getvalue("podimage")

start_pod = subprocess.getoutput("kubectl run {} --image={} --kubeconfig admin.conf".format(podname,imgname))
print(start_pod)
print("\n\nPod {} launched successfully ....\n\n".format(podname))
