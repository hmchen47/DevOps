# Course Introduction


## CCNP Security Certification Goals
+ Get industry level recognition and knowledge
    + Knowledge is power
+ Wrong but common approach
    + Memorize commands and theory
    + Get certified by any means, read one book, go take exam
    + Will take you nowhere on the long term
+ Correct but rare approach
    + Read as many resources as possible
    + Build knowledge by understanding technologies
    + Practice as much as possible to enforce knowledge
    + At CCNP level, configure, verify and troubleshooting
    + Will pay off in the end, as you’ll become a true expert

## About SISAS

+ Current Version is 1.0
+ Exam Topics – Blueprint
    + Divided into 5 sections
    + https://learningnetwork.cisco.com/community/certifications/ccnpsecurity/sisas/exam-topics
    + Additional related topics may show up in the exam, fair game

## Course Pre-Requisites

Technical Knowledge

+ Basic knowledge of networking technologies
    + Ideally CCNA R&S certified or equivalent knowledge
    + E.g. what is OSI, TCP/IP, Ethernet, etc.
    + E.g. what are switches, routers, servers, etc.
+ Basic knowledge of security technologies
    + Ideally CCNA Security certified or equivalent knowledge
+ Working knowledge of Cisco IOS and ASA operating system
+ Working knowledge of Windows operating system

## Course Scope

What is the scope of this class?

+ Provide a structured learning methodology
    + Move away from the command memorization concept
    + Learn technologies, not commands
    + To gain knowledge there is no shortcut
+ Understand the technologies relevant to the blueprint
+ Help you pass the exam for getting certified
    + There is no one single resource (book, video series) that can get you certified

## What is CCNP Security?

> “Cisco Certified Network Professional Security (CCNP Security) certification program is aligned specifically to the job role of the Cisco Network Security Engineer responsible for Security in Routers, Switches, Networking devices and appliances, as well as choosing, deploying, supporting and troubleshooting Firewalls, VPNS, and IDS/IPS solutions for their networking environments.”

## What is SISAS?

+ Cisco’s Identity Services Engine
+ Cisco’s Description

    > “The Implementing Cisco Secure Access Solutions (SISAS) (300-208) exam tests whether a network security engineer knows the components and architecture of secure access, by utilizing 802.1X and Cisco TrustSec. This 90-minute exam consists of 65-75 questions and assesses knowledge of Cisco Identity Services Engine (ISE) architecture, solution, and components as an overall network threat mitigation and endpoint control solutions. It also includes the fundamental concepts of bring your own device (BYOD) using posture and profiling services of ISE. Candidates can prepare for this exam by taking the Implementing Cisco Secure Access Solutions (SISAS) course.”

## Description

+ Course is based on SISAS v1.0 Blueprint
    + Implementing Cisco Secure Access Solutions (300-208)
    + More specifics at http://www.cisco.com/go/ccnpsecurity
+ Course Outline
    + AAA and ISE Concepts
    + Authentication and Authorization
    + Secure Access Deployment Modes
    + Web Services
    + Profiling and Posture
    + Trustsec

## About CCNP Security Certification

+ CCNP Security Exams
    + 300-208 SISAS (Implementing Cisco Secure Access Solutions)
    + 300-206 SENSS (Implementing Cisco Edge Network Security Solutions)
    + 300-209 SIMOS (Implementing Cisco Secure Mobility Solutions)
    + 300-210 SITCS	(Implementing Cisco Threat Control Solutions)
    + 300-207 SITCS (Implementing Cisco Threat Control Solutions) - obsolete


## Study Materials

+ iNE Materials
    + CCNA / CCNP Routing and Switching Videos
    + CCNP Security Technologies Courses
    + One class for each of the four courses
    + CCNP Security Bootcamp Course
    + Available in INE Course Library, focused mostly on examples
    + CCIE Security Materials
+ Additional Materials
    + Books
    + Cisco Documentation

+ Recommended Books
    + General Networking
        + [The TCP/IP Guide](http://www.tcpipguide.com/free/)
        + [TCP/IP Illustrated, Volume 1: The Protocols](http://www.cs.newpaltz.edu/~pletcha/NET_PY/the-protocols-tcp-ip-illustrated-volume-1.9780201633467.24290.pdf)
        + [Internetworking with TCP/IP Volume 1](http://dl4.libgen.io/get.php?md5=B994EBC8603E0C53746AE97723B67B97&key=ZZC0IJXQP2LVN05G)
        + [Network Security Fundamentals](http://b-ok.org/dl/459536/e6c0e6)
    + CCNA Routing and Switching
        + CCENT Official Certification Guide
        + CCNA Official Certification Guide
    + CCNA Security
        + CCNA Security Official Certification Guide
    + CCNP Security SISAS
        + Cisco ISE for BYOD and Secure Unified Access
        + SISAS Official Certification Guide
        + AAA Identity Management Security

+ Cisco Documentation
    + Product / Software Documentation
        + Technology White Papers
        + Configuration Guides
        + Command References
    + Cisco Live Presentations
        + http://www.ciscolive365.com
        + Sort by technology and difficulty level
    + Cisco Validated Designs
        + http://www.cisco.com/go/cvd
        + Sort by technology

+ Additional Information
    + CCNP Security Study Group
        + https://learningnetwork.cisco.com/groups/ccnp-security-studygroup
    + Sample Exam Questions
        + https://learningnetwork.cisco.com/community/certifications/ccnpsecurity/sisas/practice
    + Huge demand for Security experts on the market
        + Especially Cyber Security Experts
    + Networking and Security Salaries
        + https://learningnetwork.cisco.com/blogs/certifications/2015/04/03/lets-talk-money-networking-and-security-salaries

## Logical Network Topologies

+ Base Network Topology

    <img src="./diagrams/sisas-net0.png" width="600" alt="tBase Network Diagram">

    + SRV-A (INELAB-local): DNS server, AD Domain controller for PC-A
    + SRV-B: DNS Server for PC-B
    + ASA3 - FW, SXP: 
        + Inside interface: Gi0/1.83
        + Outside interface: Gi0/1.92
        + DMZ interface: Gi0/1.91
    + SW3: Security ACL

+ Network Topology A

    <img src="./diagrams/sisas-net1.png" width="600" alt="Network Diagram A">

+ Network Topology B

    <img src="./diagrams/sisas-net2.png" width="600" alt="Network Diagram B">

+ Physical Network Diagram

    <img src="./diagrams/sisas-phy.png" width="450" alt="Physical Network Connection">

+ Software List
    + ASA 9.1 Software Image w/ ASDM 7.1 - SXP
    + ISE 1.2 (17) NFR kit
    + SW: IOS 15.0(2) SE2 or IOS 12.2(37) SE7


