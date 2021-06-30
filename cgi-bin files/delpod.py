#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html\r\n")

f = cgi.FieldStorage()

# Delete Pods
del_pod_name = f.getvalue("del_podname")

del_pod =  subprocess.getoutput('kubectl delete pod ' + del_pod_name + ' --kubeconfig admin.conf')
print(del_pod)
print("\n\nPod {} Deleted Successfully ...... \n\n".format(del_pod_name))
