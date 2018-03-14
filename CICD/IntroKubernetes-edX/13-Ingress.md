Ingress
=======

## Introduction
In the _Services_ chapter, we saw how we can access our deployed containerized application from the external world. Among the _ServiceTypes_ mentioned in that chapter, NodePort and LoadBalancer are the most often used. For the LoadBalancer _ServiceType_, we need to have the support from the underlying infrastructure. Even after having the support, we may not want to use it for every Service, as LoadBalancer resources are limited and they can increase costs significantly. Managing the NodePort _ServiceType_ can also be tricky at times, as we need to keep updating our proxy settings and keep track of the assigned ports. In this chapter, we will explore the Ingress, which is another method we can use to access our applications from the external world.

## Learning Objectives
+ Discuss about Ingress and Ingress Controllers.
+ Learn when to use Ingress.
+ Access an application from the external world using Ingress.

## Ingress 
With Services, routing rules are attached to a given Service. They exist for as long as the Service exists. If we can somehow decouple the routing rules from the application, we can then update our application without worrying about its external access. This can be done using the Ingress resource. 

According to [kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/ingress/),

> "An Ingress is a collection of rules that allow inbound connections to reach the cluster Services."

To allow the inbound connection to reach the cluster Services, Ingress configures a Layer 7 HTTP load balancer for Services and provides the following:

+ TLS (Transport Layer Security)
+ Name-based virtual hosting 
+ Path-based routing
+ Custom rules.

![Ingress](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/321249e03e5c385f7b94f7651beebecd/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/ingress.png)

With Ingress, users don't connect directly to a Service. Users reach the Ingress endpoint, and, from there, the request is forwarded to the respective Service. You can see an example of a sample Ingress definition below:
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: web-ingress
spec:
  rules:
  - host: blue.myweb.com
    http:
      paths:
      - backend: 
          serviceName: blue-service
          servicePort: 80
  - host: green.myweb.com
    http:
      paths:
      - backend:
          serviceName: green-service
          servicePort: 80
```
According to the example we provided, users requests to both `blue.myweb.com` and `green.myweb.com` would go to the same Ingress endpoint, and, from there, they would be forwarded to `blue-service`, and `green-service`, respectively. Here, we have seen an example of a Name-Based Virtual Hosting Ingress rule. 

We can also have Fan Out Ingress rules, in which we send requests like `myweb.com/blue` and `myweb.com/green`, which would be forwarded to blue-service and green-service, respectively.

![Ingress URL Mapping](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/d80931c9035169af0fdd77ab2cf7df44/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/urlmap.jpg)

The Ingress resource does not do any request forwarding by itself. All of the magic is done using the Ingress Controller, which we will discuss next.

## Ingress Controller
An [Ingress Controller](https://kubernetes.io/docs/concepts/services-networking/ingress/#ingress-controllers) is an application which watches the Master Node's API Server for changes in the Ingress resources and updates the Layer 7 load balancer accordingly. Kubernetes has different Ingress Controllers, and, if needed, we can also build our own. [GCE L7 Load Balancer](https://github.com/kubernetes/ingress/tree/master/controllers/gce) and [Nginx Ingress Controller](https://github.com/kubernetes/ingress/tree/master/controllers/nginx) are examples of Ingress Controllers.

### Start the Ingress Controller with minikube
Minikube v0.14.0 and above ships the Nginx Ingress Controller setup as an add-on. It can be easily enabled by running the following command:
```bash
$ minikube addons enable ingress
```

## Deploy an Ingress Resource
Once the Ingress Controller is deployed, we can create an Ingress resource using the `kubectl create` command. For example, if we create a `myweb-ingress.yaml` file with the content that we saw on the _Ingress_ page, then, we will use the following command to create an Ingress resource:
```bash
$ kubectl create -f myweb-ingress.yaml
```

## Access Services Using Ingress
With the Ingress resource we just created, we should now be able to access the `blue-service` or `green-service` services using `blue.myweb.com` and `green.myweb.com` URLs. As our current setup is on minikube, we will need to update the host configuration file (`/etc/hosts` on Mac and Linux) on our workstation to the minikube's IP for those URLs:
```bash
$ cat /etc/hosts
127.0.0.1        localhost
::1              localhost
192.168.99.100   blue.myweb.com green.myweb.com 
```
Once this is done, we can now open `blue.myweb.com` and `green.myweb.com` on the browser and access the application.


## Using Ingress Rules to Access an Application Demo
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://youtu.be/XKbV-vurBzg)

