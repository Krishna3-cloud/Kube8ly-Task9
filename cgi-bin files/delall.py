#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

# Delete all Kubernetes Resources
del_all = subprocess.getoutput("kubectl delete all --all --kubeconfig admin.conf")
print(del_all)
print("\n\nAll resources are deleted successfully.....\n\n")
