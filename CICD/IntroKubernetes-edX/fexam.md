Final Exam
==========

Q01. We can configure Container Orchestrators on VMs. True or False?

    Ans: true

Q02. Which project has inspired Kubernetes? Select the correct answer.

    A. Docker Swarm
    B. Borg
    C. ZFS
    D. Raft

    Ans: b

Q03. Which of the following projects are managed under the CNCF umbrella? Select all answers that apply.

    A. CNI
    B. Prometheus
    C. Linkerd
    D. gRPC

    Ans: a, b, c, d

Q04. What is 'etcd'? Select the correct answer.

    A. NoSQL database
    B. Relational database
    C. Distributed key-value store
    D. Graph database

    Ans: c

Q05. Which of the following are components of a Worker Node? Select the correct answer.

    A. Container runtime
    B. kube-proxy
    C. Container runtime and kube-proxy
    D. None of the above

    Ans: c

Q06. Which networking model is used by Kubernetes? Select the correct answer.

    A. Container Network Model (CNM)
    B. Container Network Interface (CNI)
    C. Both CNI and CNM
    D. None of the above

    Ans: b

Q07. What is the most basic Kubernetes object? Select the correct answer.

    A. Container
    B. ReplicaSet
    C. Namespace
    D. Pod

    Ans: d

Q08. What do containers share inside a Pod? Select all answers that apply.

    A. Same IP address
    B. Volumes
    C. Same name
    D. None of the above

    Ans: a, b
    Was wrong (a, b, c)

Q09. On what kind of environment can Kubernetes be installed on? Select the correct answer.

    A. VMs
    B. Bare Metal
    C. Cloud infrastructure
    D. All of the above

    Ans: d

Q10. Once an object is created, which of the following fields will give us the object's current state? Select the correct answer.

    A. status
    B. spec
    C. config
    D. current

    Ans: a

Q11. Which file format we generally use to send an object's creation details to the API Server? Select the correct answer.

    A. XML
    B. UML
    C. YAML
    D. Plain text

    Ans: c

Q12. What do we define with the 'apiVersion' field in the object's configuration file? Select the correct answer.

    A. Object name
    B. API endpoint to connect to the API Server
    C. Object type
    D. None of the above

    Ans: b

Q13. A Pod can self-heal itself. True or False?

    Ans: false

Q14. What does a Deployment automatically create? Select the correct answer.

    A. ReplicaSets
    B. Replica Controller
    C. Volumes
    D. None of the above

    Ans: a

Q15. Containers of a Pod can be scheduled on different nodes. True or False?

    Ans: flase
    Was wrong

Q16. We can give more than one label to an object. True or False?

    Ans: true

Q17. What can we use with ReplicaSets? Select the correct answer.

    A. Equality-based selectors
    B. Set-based selectors
    C. Both equality-based selectors and set-based selectors
    D. None of the above

    Ans: c

Q18. We can record a Deployment to do rollbacks, if necessary. True or False?

    Ans: true

Q19. A service can have more than one endpoints attached to it. True or False?

    Ans: true
    Was wrong

Q20. Which Master Node component is watched by the 'kube-proxy' on each Worker Node for services and endpoints? Select the correct answer.

    A. Controller Manager
    B. Scheduler
    C. API Server
    D. All of the above

    Ans: c

Q21. We can have a service for which Kubernetes does not provide a ClusterIP. True or False?

    Ans: true
    Was wrong

Q22. In which of the following ways can we do Service Discovery in Kubernetes? Select the correct answer.

    A. Environment variables
    B. DNS add-ons
    C. Environment variables and DNS add-ons
    D. None of the above

    Ans: c

Q23. While exposing a Service using NodePort, ___________. Select all answers that apply.

    A. A ClusterIP is assigned to the service
    B. A Load Balancer is configured automatically, using the underlying cloud infrastructure
    C. The service is exposed at a static port on all the Worker Nodes
    D. The port is opened only on the nodes where Pods are running for the respective service

    Ans: a, c
    Was wrong (a, c, d - perspective port)

Q24. While exposing a Service using LoadBalancer, ________________. Select all answers that apply.

    A. A ClusterIP is assigned to the service
    B. The service is exposed at a static port on all the Worker Nodes
    C. A load balancer is configured automatically using the underlying cloud infrastructure
    D. The Port is opened only on the nodes where Pods are running for the respective service

    Ans: a, b, c

Q25. Kubernetes assigns the IP address defined with the ExternalIP service to a node. True or False?

    Ans: false

Q26. Creating a PersistentVolumeClaim means that the Volume is mounted automatically inside a Pod. True or False?

    Ans: flase 
    Was wrong

Q27. While creating a PersistentVolumeClaim, a user can specify the size and access mode. True or False?

    Ans: true

Q28. Which of the following can be an argument to the 'kubectl create -f' command? Select the correct answer.

    A. YAML file with object definition
    B. Pod name
    C. XML file with object definition
    D. UML file with object definition

    Ans: a

Q29. While storing values, Secrets do data encryption. True or False?

    Ans: false

Q30. We can implement our own Ingress Controller. True or False?

    Ans: true
