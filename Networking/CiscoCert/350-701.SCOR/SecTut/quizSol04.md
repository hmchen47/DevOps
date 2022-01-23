# Quiz Set 4


## 13. Malware Protection & AMP

- <span style="color: blue; font-weight: blue;">Question 1</span>

  Which Cisco AMP file disposition valid?

  A. pristine>br>
  B. malware>br>
  C. dirty>br>
  D. non malicious>br>

  Answer: B


- <span style="color: blue; font-weight: blue;">Question 2</span>

  When using Cisco AMP for Networks which feature copies a file to the Cisco AMP cloud for analysis?

  A. Spero analysis<br>
  B. dynamic analysis<br>
  C. sandbox analysis<br>
  D. malware analysis<br>

  Answer: B

  Explanation

  Spero analysis examines structural characteristics such as metadata and header information in executable files. After generating a Spero signature based on this information, if the file is an eligible executable file, the device submits it to the Spero heuristic engine in the AMP cloud. Based on the Spero signature, the Spero engine determines whether the file is malware.

  Reference: https://www.cisco.com/c/en/us/td/docs/security/firepower/60/configuration/guide/fpmc-config-guide-v60/Reference_a_wrapper_Chapter_topic_here.html

  -> Spero analysis only uploads the signature of the (executable) files to the AMP cloud. It does not upload the whole file. Dynamic analysis sends files to AMP ThreatGrid.

  Dynamic Analysis submits (the whole) files to Cisco Threat Grid (formerly AMP Threat Grid). Cisco Threat Grid runs the file in a sandbox environment, analyzes the file’s behavior to determine whether the file is malicious, and returns a threat score that indicates the likelihood that a file contains malware. From the threat score, you can view a dynamic analysis summary report with the reasons for the assigned threat score. You can also look in Cisco Threat Grid to view detailed reports for files that your organization submitted, as well as scrubbed reports with limited data for files that your organization did not submit.

  Local malware analysis allows a managed device to locally inspect executables, PDFs, office documents, and other types of files for the most common types of malware, using a detection rule set provided by the Cisco Talos Security Intelligence and Research Group (Talos). Because local analysis does not query the AMP cloud, and does not run the file, local malware analysis saves time and system resources. -> Malware analysis does not upload files to anywhere, it only checks the files locally.

  There is no sandbox analysis feature, it is just a method of dynamic analysis that runs suspicious files in a virtual machine.


- <span style="color: blue; font-weight: blue;">Question 3</span>

  Which Cisco Advanced Malware protection for Endpoints deployment architecture is designed to keep data within a network perimeter?

  A. cloud web services<br>
  B. network AMP<br>
  C. private cloud<br>
  D. public cloud<br>

  Answer: C


- <span style="color: blue; font-weight: blue;">Question 4</span>

  Which capability is exclusive to a Cisco AMP public cloud instance as compared to a private cloud instance?

  A. RBAC<br>
  B. ETHOS detection engine<br>
  C. SPERO detection engine<br>
  D. TETRA detection engine<br>

  Answer: B


- <span style="color: blue; font-weight: blue;">Question 5</span>

  An engineer is configuring AMP for endpoints and wants to block certain files from executing. Which outbreak control method is used to accomplish this task?

  A. device flow correlation<br>
  B. simple detections<br>
  C. application blocking list<br>
  D. advanced custom detections<br>

  Answer: C


- <span style="color: blue; font-weight: blue;">Question 6</span>

  Which function is the primary function of Cisco AMP threat Grid?

  A. automated email encryption<br>
  B. applying a real-time URI blacklist<br>
  C. automated malware analysis<br>
  D. monitoring network traffic<br>

  Answer: C


- <span style="color: blue; font-weight: blue;">Question 7</span>

  What are two list types within AMP for Endpoints Outbreak Control? (Choose two)

  A. blocked ports<br>
  B. simple custom detections<br>
  C. command and control<br>
  D. allowed applications<br>
  E. URL<br>

  Answer: B D

  Explanation

  Advanced Malware Protection (AMP) for Endpoints offers a variety of lists, referred to as Outbreak Control, that allow you to customize it to your needs. The main lists are: Simple Custom Detections, Blocked Applications, Allowed Applications, Advanced Custom Detections, and IP Blocked and Allowed Lists.

  A Simple Custom Detection list is similar to a blocked list. These are files that you want to detect and quarantine.

  Allowed applications lists are for files you never want to convict. Some examples are a custom application that is detected by a generic engine or a standard image that you use throughout the company

  Reference: https://docs.amp.cisco.com/AMP%20for%20Endpoints%20User%20Guide.pdf


- <span style="color: blue; font-weight: blue;">Question 8</span>

  What is a required prerequisite to enable malware file scanning for the Secure Internet Gateway?

  A. Enable IP Layer enforcement.<br>
  B. Activate the Advanced Malware Protection license<br>
  C. Activate SSL decryption.<br>
  D. Enable Intelligent Proxy.<br>

  Answer: D



## 14. AAA




## 15. Endpoint Protection & Detection




## 16. Cisco Umbrella



