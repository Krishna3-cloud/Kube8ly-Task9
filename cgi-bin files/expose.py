#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html\r\n")

f = cgi.FieldStorage()

# Exposing
expose_deploy_name = f.getvalue("expose_deployname")

expose_deploy =  subprocess.getoutput('kubectl expose deployment  {} --type=NodePort --port=80 --kubeconfig admin.conf'.format(expose_deploy_name))
print(expose_deploy)
print("\n\nDeployment {} is Exposed ...... \n\n".format(expose_deploy))
