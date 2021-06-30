#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

# List Pods
print("\n\nList of all pods .....\n")
list_pod = subprocess.getoutput("kubectl get pod --kubeconfig admin.conf")
print(list_pod)

