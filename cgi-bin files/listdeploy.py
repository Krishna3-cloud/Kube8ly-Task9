#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

print("\n\nList of all deployments .....\n")
list_deploy = subprocess.getoutput("kubectl get deploy --kubeconfig admin.conf")
print(list_deploy)
