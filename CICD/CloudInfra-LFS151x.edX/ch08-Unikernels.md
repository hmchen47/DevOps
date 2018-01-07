# Chapter 8. Unikernels

## Introduction and Learning Objectives
### Unikernels
Earlier in the course we mentioned that in today's world our end goal is, most of the time, to run an application. We also explained how container technology is helping us achieve this end goal. We learned that, to run containers, we also need to ship the entire user-space libraries of the respective distribution with the application. In most cases, the majority of the libraries would not be consumed by the application. Therefore, it makes sense to ship the application only with the set of user-space libraries which are needed by the application.  

With __Unikernels__, we can also select the part of the kernel needed to run with the specific application. With __Unikernels__, we can create a single address space executable, which has both application and kernel components. The image can be deployed on VMs or bare-metal, based on the unikernel's type.

According to the [Unikernels website][uniker],

> "Unikernels are specialised, single-address-space machine images constructed by using library operating systems." 

In this chapter, we will discuss __unikernels__, their characteristics, implementations, and benefits.

### Learning Objectives
By the end of this chapter you should be able to:

+ Explain the concept of unikernels.
+ Compare and contrast unikernels and containers.

## Unikernels
### Creating Specialized VM Images
[Unikernel][uniker] goes one step further than other technologies, creating specialized Virtual Machine images with just:

+ The application code.
+ The configuration files of the application.
+ The user-space libraries needed by the application.
+ The application runtime (like __JVM__).
+ The system libraries of the __unikernel__, which allow back and forth communication with the __Hypervisor__.

According to the [protection ring][protect] of the x86 architecture, we run Kernel on `ring0` and application on `ring3`, which has the least privileges. `Ring0` has the most privileges, like access to hardware, and a typical OS Kernel runs on that.  With unikernels, a combined binary of the application and the kernel run on `ring0`.

__Unikernel__ images would run directly on top of a __Hypervisor__ like Xen or on bare-metal, based on the __unikernel types__. The following figure shows how the _Mirage Compiler_ creates a unikernel VM image. 

![image][img1]

Figure 8.1: Comparison of a Traditional OS Stack and a MirageOS Unikernel (by AmirMC/[CC BY-SA 3.0][byas], retrieved from [Wikipedia][wiki])

### Demo
Next, we will see how we can use the __Unik__ tool to create a very basic unikernel and then deploy it over __VirtualBox__.

[video][vid1]

### Benefits of Unikernels
+ A minimalistic VM image to run an application, which allows us to have more applications per host.
+ A faster boot time.
+ Efficient resource utilization.
+ A simplified development and management model.
+ A more secured application than the traditional VM, as the attack surface is reduced.
+ An easily-reproducible VM environment, which can be managed through a source control system like __Git__.

### Unikernel Implementations
There are many implementations of __Unikernels__, and they are divided into two categories:

+ Specialized and purpose-built unikernels

    They utilize all the modern features of software and hardware, without worrying about the backward compatibility. They are not POSIX-compliant. Some examples of specialized and purpose-built unikernels are __ING, HalVM, MirageOS__, and __Clive__.
+ Generalized 'fat' unikernels 

    They run unmodified applications, which make them fat. Some examples of generalized fat unikernels are __BSD Rump kernels, OSv, Drawbridge__, etc.

### Unikernels and Docker
In January of 2016, Docker bought __Unikernels__ to make them first-class citizen of the Docker ecosystem. Both containers and unikernels can co-exist on the same host. They can be managed by the same Docker binary.

__Unikernels__ helped Docker to run the __Docker Engine__ on top of [Alpine Linux][alpine] on Mac and Windows with their default hypervisors, which are __xhyve Virtual Machine__ and __Hyper-V VM__ respectively. 

![image][img2]

Figure 8.2: Shared Kernel vs. Unikernel

### References
+ http://unikernel.org/
+ http://slides.com/technolo-g/intro-to-unikernels-and-erlang-on-xen-ling-demo

## Knowledge Check
1. With Unikernels, the resulting image is a _____________. Please select the correct answer.

        A. Container image
        B. VM image 
        C. Container or VM image
        D. Container and VM image

        Ans: B

2. Do Unikernels run directly on the Host OS?

        Ans: No, Hypervisor

3. Are all Unikernels POSIX-compliant? 

        Ans: No, only generalized 'fat' unikernels do


[vid1]: https://edx-video.net/LINLFS15/LINLFS152016-V005000_DTH.mp4

[img1]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/06dee41f4d33cfda12ee8452e7936e1a/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig8.1_-_Example_of_a_Unikernel_Architecture__as_Compared_to_a_Traditional_OS_Stack_.png
[img2]: https://prod-edxapp.edx-cdn.org/assets/courseware/v1/49002a28650cb5cd1b750d8c9926ac60/asset-v1:LinuxFoundationX+LFS151.x+2T2016+type@asset+block/Fig8.2-SharedKernel-vs-Unikernel.png

[uniker]: http://unikernel.org/
[protect]: https://en.wikipedia.org/wiki/Protection_ring
[byas]: http://creativecommons.org/licenses/by-sa/3.0/
[wiki]: https://courses.edx.org/courses/course-v1:LinuxFoundationX+LFS151.x+2T2016/courseware/c7e16edc1d824f218ef5998934289c0c/45a7c6cdf0b146a38e2d19ae09928aff/Comparison%20of%20a%20traditional%20OS%20stack%20and%20a%20MirageOS%20unikernel
[alpine]: http://www.alpinelinux.org/


