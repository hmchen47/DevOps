# Using a Certificate Assigning by a CA

+ CA Assigned ISE Certificate: Using PKI for ISE Authentication
    1. Download/Install Root CA Certificate on ISE
    2. Generate a certificate signing request from ISE
    3. Submit request to CA
    4. Install ISE Identity certificate on ISE

+ Root Certificate
    + Public Key Infrastructure
        + __Public Key Infrastructure (PKI)__: a system of digital Certificates, Certificate Authorities, and other registration authorities that verify and authenticate the validity of each party involved in an online transaction.
        + Certificate Authority (CA) or the Registration Authority: a trusted third-party organization or company that issues digital certificates and signs them with their own Trust Anchor to prove the origin of the certificates. 
        + One of the roles of the Certificate Authority or the Registration Authority in this process is to guarantee that the individual granted the unique certificate is, in fact, who he or she claims to be.
        <a href="https://ldapwiki.com/wiki/Public%20Key%20Infrastructure">
            <br/><img src="https://ldapwiki.com/attach/Public%20Key%20Infrastructure/PKI%20Infrastructure%20Overview.png" alt="Process to issue Certificate" width="350">
        </a>
        <a href="http://software-engineer-tips-and-tricks.blogspot.com/2012/09/what-is-pki.html">
            <img src="http://2.bp.blogspot.com/-_fWrkvGJ7iY/UFrZPpFoXLI/AAAAAAACk_4/pV2EiEbXfUk/s640/pki1.gif" alt="PKI Infrastructure" width="350">
        </a>
    + SSL/TLS and PKI
        + __Symmetric-key algorithms/secret key algorithms__ <br/> That key is used for both encryption of plaintext and decryption of ciphertext, it represents a shared secret between two or more parties that can be used to maintain a private information link.
        + __Public-key algorithms/asymmetric-key algorithms__ <br/> These algorithms require two separate (and different) keys, one of which is secret and one of which is public. The public key can be freely distributed and the secret key is secret.<br/> These keys are mathematically linked, however it is extremely difficult (or effectively impossible) for anyone to derive the private key, based only on their knowledge of the public key. <br/> Therefore, a message encrypted with the public key, it can only be decrypted with its corresponding private key and vice-versa. This last is known as digital signature.
        + __Message digest__: It is the result of applying a hash function (or function without inverse) on a message. That result is easy to compute and infeasible to find two different messages with the same hash. <br/> The message digest are used to generate a small (fixed length) representation of usually longer (variable length) messages.
        + __Digital signature__: Digital signatures are equivalent to traditional handwritten signatures. The digital signature scheme is usually formed by three algorithms:
            + First generates the public and private keys.
            + Second "signs" (encrypts) a message or document with the private key.
            + Third verifies the digital signature using the corresponding public key.
        
            In conclusion, the digital signature scheme is a mathematical scheme for demonstrating the authenticity of a digital message or document.
        + __Digital certificate/public key certificate/identity certificate__: It is an electronic document that uses a digital signature to bind a public key with an identity (information such as the name of a person or an organization, their address, etc.). The signature will be of a certificate authority (CA), that attests the contained public key belongs to the associated identity. <br/> Digital certificates can be used to verify that a public key belongs to an individual or Company. If a site provides a digital certificate, the users that connect to that site can verify its identity (as well as securely communicate with it). On top of that, if the user also provides a digital certificate, the site will also be able to identify the user.
        + __Certificate authority__: A CA is a trusted third party that is trusted by both the subject (owner) of the certificate and the party relying upon the certificate. Its main purpose is to issue digital certificates to individuals, organizations, domains and other entities, and control the status of the issued digital certificates. Example of CA's: Verisign, Thawte, Equifax, etc.
        <a href="https://darizotas.blogspot.com/2013/02/understanding-secure-web-communications.html">
            <br/><img src="http://2.bp.blogspot.com/-sU3oge29pNI/UPwnwOmcoSI/AAAAAAAAAO0/M4j3TxJFEFs/s1600/pki.jpg" alt="Concept interaction" width="450">
        </a>
    + Chain of Trust 
        + A root certificate is a public key certificate that identifies a root certificate authority (CA)
        <a href="https://en.wikipedia.org/wiki/Root_certificate">
            <br/><img src="https://upload.wikimedia.org/wikipedia/commons/d/d1/Chain_of_trust.svg" alt="The role of root certificate as in the chain of trust." width="450">
        </a>
    + AAA = Authentication, Authorization, and Accounting
    + Digital Certificate for authentication
        + Validation
        + Signature -> CA -> PKI
    + ISE public key including in certificate
    + Certificate Signing Request (CSR)
        + A __block of encoded text__ given to a Certificate Authority when applying for an SSL Certificate.
        + Usually generated on the server where the certificate will be installed
        + Containing information included in the certificate such as the organization name, common name (domain name), locality, and country. 
        + Containing the public key that will be included in the certificate. 
        + A private key usually created at the same time when creating the CSR, making a key pair. 
        + Generally encoded using ASN.1 according to the PKCS #10 specification.

+ Download/Install Root CA Certificate
    + Microsoft AD Certificate Service: IE (http://192.168.1.123/certsrv)
    + Tasks: Download a CA certificate, certificate chain, or CRL
        + Encoding: _DER_, Base 64
        + Download CA certificate
        + Save; Root-CA-Cert.cer
    + Install on ISE w/ Windows certificate (Root-CA-Cert.cer): Administration > System - Certificates > Certificate Options > Certificate Store > Import: Certificate File=Root-CA-Cert.cer, Friendly Name=Lab CA, enable 'Trust for cleint authentication or Secure Syslog services' > Submit

+ Generate a certificate signing request
    <a href="https://asecuritysite.com/encryption/csr">
        <br/><img src="https://asecuritysite.com/certs.png" alt="Process for generating keys and creating the CSR" width="300">
    </a>
    + Check: Administration > System-Certificates > Certificate Operations > Certificate Signing Request > (None)
    + Creat local certificate: Administration > System-Certificates > Certificate Operations > Local Certificates > Add (Generate Certificate Signing Request): Certificate Subject = (CN=ise.nuglab.com), key length=2048, Digest to sign with=SHA=256 > Submit
    + Generate CSR: Administration > System-Certificates > Certificate Operations > Certificate Signing Requests: select 'ise.nuglab.com' > Export > Save: CSR from ISE.pem
    + Windows `Wordpad` > Open 'CSR from ISE.pem' (Not `Notepad` for carry return issue) > Ctrl+A > Ctrl+C
    + AD CS Server (htp://192.168.1.123)
        + Task=Request a certificate
        + Submit an 'Advanced certificate request'
        + Submit a certificate request by using a base-64-encoded CMC or PKCS#10 file or submit a renewal request by using a base-64-encoded
            + Save Request: Base-64-encoded certificate request (CMC or PKCS#10 or PKCS#7)= [certificate test string from Ctrl+V] > Submit > Certificate Pending, id=3
            + Certificate pending: certificate request has been received, wait for an administrator to issue the certificate requested.  Request Id=3, Return to this web site in a day or two to retrieve your certificate (max=10 days)
    + Windows 2012 Server: Approve certificate
        + Server Manager > Tools > Certificate Authority
        + certsrv [Certification uthority (Local)] > SERVER1-CA > Pending Request > Request ID=3 (rc) > All Tasks > Issue

+ Submit Certificate to CA - AD CS Server
    + Task = View the status of a pending certificate request
    + view = Saved-Request Certificate (...)
    + Certificate Issued:
        + DER encoded
        + Download certificate: ISE AD Cert.cer

+ Download CA Certificate from CA Server to Local Host
    + Task: Download a CA certificate, certificate chain, or CRL
    + Encoding = DER, Download CA Certificate
    + Save: root-cert.cer

+ Install ISE Identity Certificate on ISE: Administration > System-Certificates > Certificate Operations > Local Certifciate > Add (Bind CA Signed Certificate): Certificate File=ISE ID Cert.cer, Friendly Name=ISE ID Certificate, Protocols=(EAP, HTTPS) > Submit > System Restart

+ Verification:
    + PC: `ping 192.168.1.117` - ok; `ping ise.nuglab.com` - ok
    + IE (https://192.168.1.117) -> page shown problem with security certificate
    + IE (https://ise.nuglab.com) -> page shown problem with security certificate
    + Add Root Certificate to IE: IE > Settings > Internet Options > Contents > Certificate-Certificates > Trusted Root Certificate Authorities > Import: root-cert.cer > Open > Certificate Store = Trusted Root Certificate Authorities > Next > Finish
    + IE (https://ise.nuglab.com): login prompt
    + NIC > Properties > Authentication > PEAP Settings: 'enable 'Validate server certificate', Trusted Root Certificate Authorities=SERVER1-CA > Cancel (lab env. not to enable this)











