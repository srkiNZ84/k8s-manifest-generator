# Kubernetes Manifest Generator

## What is this?
This is a tool to query a namespace and generate an INI format plain text file listing all of the Pods in the namespace
along with their "versions" (where, "version" is the Docker image tag).

## Why did you do this?
In order to be able to "version" all of the Pods that currently make up a namespace prior to running end to end tests on
them.

## How do I use this?
Make sure you have installed the Kubernetes Python client by running:

  pip install kubernetes

and then run:

  python2 k8smanifest.py KUBECTLCONTEXT [--outputfile -o OUTPUTFILE]

NOTE: There's also an assumption that you have access to the Kubernetes API in question.

