#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

f = cgi.FieldStorage()

# Create Replicas
deployname = f.getvalue("deploy_name")
no_of_replica = f.getvalue("replicas")

scale_deploy = subprocess.getoutput("kubectl scale deployment {} --replicas={} --kubeconfig admin.conf".format(deployname,no_of_replica))
print(scale_deploy)
print("\n\n{} replicas created successfully ....\n".format(no_of_replica))

