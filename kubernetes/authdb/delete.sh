#!/bin/sh
kubectl delete -f authdb-mariadb.service.yml --namespace=myportail
kubectl delete -f authdb.storage.do.yml --namespace=myportail
kubectl delete -f authdb.configmap.yml --namespace=myportail
