#!/usr/bin/python

from kubernetes import client, config
import os
import argparse

parser = argparse.ArgumentParser(description='Generate a Kubernetes \
        Pod manifest.')
parser.add_argument('context', type=str, \
                   help='kubectl context to use')
parser.add_argument('-o', '--outputfile', metavar='-o', type=str, \
                    help='Name of the file to output the manifest to. \
                    Defaults to "manifest.ini"')
args = parser.parse_args()

manifestFilename = 'manifest.ini'
if args.outputfile:
    manifestFilename = args.outputfile

contextName = args.context

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config(context=contextName)

outputManifest = open(manifestFilename, 'w')

v1 = client.CoreV1Api()
print("Listing pods with their versions:")
ret = v1.list_namespaced_pod("jenkins", pretty=True)
for i in ret.items:
    for j in i.spec.containers:
        if j.image.find(':') != -1:
            version = j.image.split(':')[1]
        else:
            version = 'latest'

        print("\n[%s]" % j.name)
        outputManifest.write("\n[%s]" % j.name)
        print("service.name=%s" % j.name)
        outputManifest.write("\nservice.name=%s" % j.name)
        print("service.image=%s" % j.image)
        outputManifest.write("\nservice.image=%s" % j.image)
        print("service.version=%s" % version)
        outputManifest.write("\nservice.version=%s\n" % version)
        #print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
outputManifest.close()
