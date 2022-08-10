# kubernetes-experiments

Currently experimenting with services interconnection inside kubernetes

## How-to run:
* Prepare kubernetes cluster(docker desktop for mac already has on, you should only go to setting and turn in on)
* Build the api container image(but change repository in justfile before, so you won't use mine)
```
just build-http-api
```
* Publish image to docker hub(i wasn't been able to make k8s work with locally stored images)
```
docker push whatever/http-api
```
* Edit image name in container spec in deployment/api.yaml
* Apply manifests to the cluster
```
kubectl apply -f deployment/redis.yaml
kubectl apply -f deployment/api.yaml
```
Note that http-api connects to redis via `redis.default.svc.cluster.local` - this is the examples of dns service discovery enabled by default in recent kubernetes versions
* Check http-api externals
```
kubectl get svc http-api-service
```
You will see something like that:
```
NAME               TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
http-api-service   LoadBalancer   10.109.226.134   localhost     8080:31763/TCP   12s
```
You can navigate to http://localhost:8080/docs and try api yourself and see it working(use /set with key hello and value world, then verify it with /get and key hello)
* Optionally - expose Redis(by adding `type: LoadBalancer` into redis.yaml service definition) and connect to redis with some gui client to see that http-api indeed places keys with values
