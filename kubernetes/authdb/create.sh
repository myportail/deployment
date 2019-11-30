#!/bin/sh
kubectl apply -f authdb.storage.do.yml --namespace=myportail
kubectl apply -f authdb.configmap.yml --namespace=myportail
kubectl apply -f authdb-mariadb.service.yml --namespace=myportail
