Deploying a Stand-Alone Application
===================================

## Introduction
In earlier chapters, we looked at the Kubernetes architecture and its building blocks (objects). We also saw how we can deploy and access an All-in-One Kubernetes cluster using minikube. In this chapter, we will learn to deploy an application using the GUI or CLI. We will also expose an application with NodePort, and access it from the external world.

## Learning Objectives
+ Deploy an application from the dashboard.
+ Deploy an application from a YAML file using kubectl.
+ Expose a Service using NodePort.
+ Access the application from the external world.

## Deploying an Application Using the Minikube GUI
In the next few pages, we will learn how to deploy an nginx webserver using the `nginx:alpine` Docker image.

### Make sure that minikube is running

To ensure that minikube is running, run the following command:
```bash
$ minikube status
minikubeVM: Running
localkube: Running
```

### Start the minikube Dashboard

To access the GUI (Dashboard), we need to run the following command:
```bash
$ minikube dashboard
```
Running this command will open up a browser with the Kubernetes GUI, which we can use to manage containerized applications. By default, the Dashboard is connected to the `default` Namespace. So, all the operations that we will do in this chapter will be performed inside the `default` Namespace.

![Deploying an Application - Accessing the Dashboard](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/8700005b7c29bbaef6d5debd20f93b9b/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/deploy1.png)

### Deploy a webserver using the `nginx:alpine` image
From the Dashboard, click on _Deploy a Containerized App_, which will open an interface like the one below:

![Deploy a Containerized application web interface](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/706b9e71c3c73cd1a20b021fe8372f49/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/deploy2update.png)

We can either provide the application details here, or we can upload a YAML file with our Deployment details. As shown, we are providing the following application details:

+ The application name is`webserver`
+ The Docker image to use is `nginx:alpine`, where `alpine` is the image tag
+ The replica count, or the number of Pods, is 3
+ No Service, as we will be creating it later.

If we click on _SHOW ADVANCED OPTIONS_, we can specify options such as Labels, Environment Variables, etc. By default, the `app` Label is set to the application name. In our example, an `app:webserver` Label is set to different objects created by this Deployment.

By clicking on the _DEPLOY_ button, we can trigger the deployment. As expected, the Deployment `webserver` will create a ReplicaSet (`webserver-1529352408`), which will eventually create three Pods (`webserver-1529352408-xxxx`).

![Deployment details](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/469c79c4125fe9e4f0b7c5dc62a00b31/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/deploy3.png)

### Check out Deployments, ReplicaSets, and Pods from the CLI
We can also list the Deployments, ReplicaSets, and Pods from the CLI, which we created using the GUI. They will match one-to-one.

#### List the Deployments
We can list all the Deployments in the given Namespace using the `kubectl get deployments` command:
```bash
$ kubectl get deployments
NAME        DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
webserver   3         3         3            3           3m
```
#### List the ReplicaSets
We can list all the ReplicaSets in the given Namespace using the `kubectl get replicasets` command:
```bash
$ kubectl get replicasets
NAME                   DESIRED   CURRENT   READY   AGE
webserver-3101375161   3         3         3       4m
```
#### List the Pods
We can list all the Pods in the given Namespace using the `kubectl get pods` command:
```bash
$ kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
webserver-3101375161-jzk57    1/1     Running   0          4m
webserver-3101375161-vxw2g    1/1     Running   0          4m
webserver-31013755161-w1flz   1/1     Running   0          4m 
```

## Exploring Labels and Selectors
Earlier, we have seen that Labels and Selectors play an important role in grouping a subset of objects on which we can perform operations. Next, we will take a closer look at them.

### Look at a Pod's details
We can look at an object's details using __kubectl__'s `describe` subcommand. In the following example, you can see a Pod's description:  
```bash
$ kubectl describe pod webserver-3101375161-jzk57
Name:        webserver-3101375161-jzk57
Namespace:   default
Node:        minikube/192.168.99.100
Start Time:  Mon, 29 May 2017 12:58:34 +0530
Labels:      app=webserver
             pod-template-hash=3101375161
             version=alpine
Annotations: kubernetes.io/created-by={"kind":"SerializedReference","apiVersion":"v1","reference":{"kind":"ReplicaSet","namespace":"default","name":"webserver-3101375161","uid":"6c85e06b-4440-11e7-9c3b-080027a4605...
Status:      Running
IP:          172.17.0.4
........
........
```
As you were able to see, with kubectl's `describe` subcommand we can get all the details about a Pod. For now, we will focus on the `Labels` field, in which we have a Label set to `app=webserver`.

### List the Pods, along with their attached Labels
With the `-L` option to the `kubectl get pods` command, we can add additional columns in the output to list Pods with their attached Labels and their values. In the following example,  we are listing Pods with the Labels `app` and `label2`:
```bash
$ kubectl get pods -L app,label2
NAME                         READY   STATUS    RESTARTS   AGE   APP         LABEL2
webserver-3101375161-jzk57   1/1     Running   0          12m   webserver   <none>
webserver-3101375161-vxw2g   1/1     Running   0          12m   webserver   <none>
webserver-3101375161-w1flz   1/1     Running   0          12m   webserver   <none>
```
All of the Pods are listed, as each Pod has the Label `app`, whose value is set to `webserver`. We can see that from the `APP` column. As none of the Pods has the `label2` Label, the value `<none>` is listed under the `LABEL2` column.

### Select the Pods with a given Label
To use a Selector with the `kubectl get pods` command, we can use the `-l` option. In the following example, we are selecting all the Pods that have the `app` Label's value set to `webserver`:
```bash
$ kubectl get pods -l app=webserver
NAME                         READY   STATUS    RESTARTS   AGE
webserver-3101375161-jzk57   1/1     Running   0          16m  
webserver-3101375161-vxw2g   1/1     Running   0          16m 
webserver-3101375161-w1flz   1/1     Running   0          16m
```
In the example above, we listed all the Pods we created, as all of them have the `app` Label, whose value is set to `webserver`.

In the next example, we are using `app=webserver1` as the Selector:
```bash
$ kubectl get pods -l app=webserver1
No resources found.
```
and, as expected, no Pods are listed.

## Deploying the Application Using the CLI
To deploy an application using the CLI, let us first delete the Deployment we created earlier.

### Delete the Deployment we created earlier
We can delete any object using the `kubectl delete` command. In the following example, we are deleting the `webserver` Deployment which we created in the previous section using the Dashboard:
```bash
$ kubectl delete deployments webserver
deployment "webserver" deleted
```
Deleting a Deployment also deletes the ReplicaSets and the Pods we created:
```bash
$ kubectl get replicasets
No resources found.

$ kubectl get pods
No resources found.
```

### Create a YAML file with Deployment details
Let us now create the webserver.yaml file with the following content:
```bash
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
    name: webserver
spec:
    replicas: 3
    template:
        metadata:
            labels:
                app: webserver
        spec:
            containers:
                - name: webserver
                    image: nginx:alpine
                    ports:
                    - containerPort: 80
```
Using __kubectl__, we will create the Deployment from the YAML file. With the `-f` option to the `kubectl create` command we can pass a YAML file as an object's specification. In the following example, we are creating a `webserver` Deployment:
```bash
$ kubectl create -f webserver.yaml
deployment "webserver" created
```
While creating the deployment, we are using the `extensions/v1beta1` API endpoint. With Kubernetes 1.6, a new API group called "apps" was added, and, in the future, the  `v1`  Deployment object would reside there. As of now, both `extensions/v1beta1` and `apps/v1beta1` are identical. 

This will also create a ReplicaSet and Pods, as defined.
```bash
$ kubectl get replicasets
NAME                   DESIRED   CURRENT   READY   AGE
webserver-1529352408   3         3         3       3s

$ kubectl get pods
NAME                         READY   STATUS    RESTARTS   AGE
webserver-1529352408-5xln6   1/1     Running   0          6s
webserver-1529352408-9st86   1/1     Running   0          6s
webserver-1529352408-tlz4m   1/1     Running   0          6s
```

## Create a Service and Expose It to the External World with NodePort
In the previous chapter, we took a look at different _ServiceTypes_, with which we can define the access method for a given Service. For a given Service, with the NodePort _ServiceType_, Kubernetes opens up a static port on all the Worker Nodes. If we connect to that port from any node, we are forwarded to the respective Service. Next, let us use the NodePort _ServiceType_ and create a Service.

Create a `webserver-svc.yaml` file with the following content:
```bash
apiVersion: v1
kind: Service
metadata:
    name: web-service
    labels:
        run: web-service
spec:
    type: NodePort
    ports:
    - port: 80
        protocol: TCP
    selector:
        app: webserver 
```
Using `kubectl`, create the Service:
```bash
$ kubectl create -f webserver-svc.yaml
service "web-service" created
```

List the Services:
```bash
$ kubectl get service
NAME            CLUSTER      EXTERNAL-IP   PORT(S)        AGE
kubernetes      10.0.0.1     <none>        443/TCP        23d
web-service     10.0.0.133   <nodes>       80:32636/TCP   15s
```
Our `web-service` is now created and its ClusterIP is `10.0.0.133`. In the `PORT(S)` section we can see a mapping of `80:32636`, which means that we have reserved a static port `32636` on the node. If we connect to the node on that port, our requests will be forwarded to the ClusterIP on port `80`.

It is not necessary to create the Deployment first, and the Service after. They can be created in any order. A Service will connect Pods based on the Selector.

To get more details about the Service, we can use the `kubectl describe` command, like in the following example:
```bash
$ kubectl describe svc web-service
Name:                 web-service
Namespace:            default
Labels:               run=web-service
Annotations:          <none>
Selector:             app=webserver 
Type:                 NodePort
IP:                   10.0.0.133    
Port:                 <unset> 80/TCP  
NodePort:             <unset> 32636/TCP
Endpoints:            172.17.0.4:80,172.17.0.5:80,172.17.0.6:80  
Session Affinity:     None
Events:               <none>
```

`web-service` uses `app=webserver` as a Selector, through which it selected our three Pods, which are listed as endpoints. So, whenever we send a request to our Service, it will be served by one of the Pods listed in the `Endpoints` section.

## Accessing the Application Using the Exposed NodePort
Our application is running inside the minikube VM. To access the application from our workstation, let's first get the IP address of the minikube VM:
```bash
$ minikube ip
192.168.99.100
```
Now, open the browser and access the application on 192.168.99.100 at port 32636.

![Accessing the application in the browser](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/50118e3cfc800348ccb175c58f834329/asset-v1:LinuxFoundationX+LFS158x+2T2017+type@asset+block/service_nodeport.jpg)

We can see the _Nginx_ welcome page, through which we can access a `webserver` running inside one of the Pods created. Our requests can be served by any one of the three endpoints selected via our Service.

## Deploying a Containerized Application Demo

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://youtu.be/_e-Oqxbt6eo)

## Knowledge Check
Q1. We can manage the application from the CLI which we deployed using the GUI (Dashboard). 

    Ans: True

Q2. Which of the following subcommands of 'kubectl' we need to use to look at an object's details? Select the correct answer.

    A. info
    B. details
    C. describe
    D. check

    Ans: c

Q3. In Kubernetes, we must create the Deployment first, and the respective Service later. True or False?

    Ans: False

