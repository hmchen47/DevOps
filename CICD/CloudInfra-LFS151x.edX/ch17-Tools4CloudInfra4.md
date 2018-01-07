# Chapter 17. Tools for Cloud Infrastructure IV (Image Building)

## Introduction and Learning Objectives
### Tools for Cloud Infrastructure: Image Building
In an immutable infrastructure environment we prefer to replace an existing service with a new one, to fix any problems/bugs or to perform an update.

To start a new service or replace an older service with a new one, we need the image from which the service can be started. These images should be created in an automated fashion. In this section, we will take a look into the creation of __Docker__ images and VM images for different cloud platforms using __Packer__.

### Learning Objectives
By the end of this chapter you should be able to:

+ Create __Docker__ images and VM images for different cloud platforms using __Packer__.


## Building Docker Images
### Dockerfiles
We can create a custom Docker image by starting a container from the base image and, after making the required changes (e.g. installing the software), commit it to persistent storage. This is not a scalable and efficient solution.

Docker has a feature by which it can read the instructions from a file and then generate the requested image. Internally, it creates a container after each instruction and then commits it to persistent storage. The file with instructions is referred to as a __Dockerfile__. Below you can see a sample Dockerfile:
```docker
FROM fedora
MAINTAINER Neependra Khare <neependra.khare@gmail.com>
RUN dnf -y update && dnf clean all
RUN dnf -y install nginx && dnf clean all
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN echo "nginx on Fedora" > /usr/share/nginx/html/index.html

EXPOSE 80

CMD [ "/usr/sbin/nginx" ]
```
FROM, MAINTAINER, RUN, EXPOSE, CMD are different kinds of instructions which are followed by arguments. The instructions are well documented in the [Docker Documentation][docdoc].

### Demo
You may have noticed that we always start with a base image when creating an image from Dockerfile. Someone has to build those images for the first time. There are tools like [Debootstrap][deboot] or [supermin][supmin] which can help you build base images.

The [Docker GitHub source code][docgit] repository also has helper scripts to create base images.

In the following video we will see how we can create a custom image from __Dockerfile__.

[video][vid1]

### References
+ https://docs.docker.com/engine/reference/builder/
+ https://docs.docker.com/engine/userguide/eng-image/baseimages/

## Packer
### Introduction to Packer
[Packer][packer] from [Hashicorp][hashi] is an Open Source tool for creating virtual images from a configuration file for different platforms.

Below is a sample configuration file:
```json
{
  "variables": {
    "aws_access_key": "abc",
    "aws_secret_key": "xyz",
    "atlas_token": "123"
  },
  "builders": [{
    "type": "amazon-ebs",
    "access_key": "{{user `aws_access_key`}}",
    "secret_key": "{{user `aws_secret_key`}}",
    "region": "us-west-2",
    "source_ami": "ami-9abea4fb",
    "instance_type": "t2.micro",
    "ssh_username": "ubuntu",
    "ami_name": "packer-example {{timestamp}}"
  }, {
  "type": "googlecompute",
  "account_file": "user.json",
  "project_id": "useapp",
  "source_image": "ubuntu-1404-trusty-v20160114e",
  "zone": "us-central1-a",
  "image_name": "myimage"
  }],
  "provisioners": [{
    "type": "shell",
    "inline": [
      "sleep 30",
      "#!/bin/bash",
      "sudo apt-get -y update",
      "sudo apt-get -y install apache2",
      .....
      .....
    ]
  }],
  "post-processors": [{
        "type": "atlas",
        "only": ["amazon-ebs"],
        "token": "{{user `atlas_token`}}",
        "artifact": "user/stack",
        "artifact_type": "amazon.image",
        "metadata": {
          "created_at": "{{timestamp}}"
        }
      }, {
        "type": "atlas",
        "only": ["googlecompute"],
        "token": "{{user `atlas_token`}}",
        "artifact": "user/stack",
        "artifact_type": "googlecompute.image",
        "metadata": {
          "created_at": "{{timestamp}}"
        }
  }]
}
```

### Steps to Create Virtual Images
In general, creating virtual images requires the following three steps:

+ __Building the base image__

    This is defined under the `builders` section of the configuration file. __Packer__ supports the following platforms: __Amazon EC2 (AMI), DigitalOcean, Docker, Google Compute Engine, OpenStack, Parallels (PVM), QEMU, VirtualBox (OVF)__, and __VMware (VMX)__. 

    Other platforms can be added via plugins.

    In the example we provided we have created images for __Amazon EC2__ and __Google Compute Engine__.

+ __Provision the base image to do configuration__ 

    Once we built a base image, we can then provision it to do further configuration changes, install software, etc. __Packer__ supports different provisioners like __Shell, Ansible, Puppet, Chef__, etc. In the example provided, we are doing provisioning with __Shell__.

+ __Perform post build operations__ 

    In the post operations we can copy/move the resulted image to a central repository, create a __Vagrant__ box, etc. In the example we provided, we are pushing the resulted image to [Atlas][atlas].

### Demo
Next, let's see how we can generate an image from a configuration file and then store it in a central location using __Packer__.

[video][vid2]

### Benefits for Using Packer
Some of the benefits for using Packer are:

+ It is an Open Source tool for creating virtual images from a configuration file for different platforms.
+ It is easy to use.
+ It automates the creation of images.
+ It provides an extremely fast infrastructure deployment, from which both development and production are benefiting. 
+ It offers multi-provider portability.

### References
+ https://www.packer.io/docs/


## Knowledge Check
Q. Which of the following is not an instruction which is used in Dockerfile? Please select the correct answer.

    A. Run
    B. Add
    C. Expose
    D. Check

    Ans: D




[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V003500_DTH.mp4
[vid2]: https://edx-video.net/LINLFS15/LINLFS152016-V003800_DTH.mp4

[docdoc]: https://docs.docker.com/engine/reference/builder/
[deboot]: https://wiki.debian.org/Debootstrap
[supmin]: https://github.com/libguestfs/supermin
[docgit]: https://github.com/docker/docker/tree/master/contrib
[packer]: https://www.packer.io/
[hashi]: https://www.hashicorp.com/
[atlas]: https://atlas.hashicorp.com/




