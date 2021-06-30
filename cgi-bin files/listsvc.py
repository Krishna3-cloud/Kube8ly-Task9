#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

# List of all services
print("\nList of all services .....\n\n")
list_svc = subprocess.getoutput("kubectl get svc --kubeconfig admin.conf")
print(list_svc)

