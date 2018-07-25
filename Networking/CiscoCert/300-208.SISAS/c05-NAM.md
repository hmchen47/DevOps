# Network Access Manager (NAM)

+ Network Access Manager (NAM): AnyConnect DOT.1x Supplicant
    + NAM install
    + Profile Editor Install
    + Adding CA certificates

+ Demo: Install AnyConnect
    + Function selected with AnyConnect ISO file
        + AnyConnect VPN
        + AnyConnect Network Access Manager
    + Cisco AnyConnect Secure Mobility Client
        + Network: Network profile for Network Access Manager
        + Create new profile: Network Details > Manage Network
            + Wired: default, EAP-FAST
            + Class Demo: create for course, PEAP

+ Demo: SW1 Basic Config
    ```cfg
    show authentication sessions int gi0/7
    ! User-Name=it-bob, Method List=(mab=Not Run, dot1x=Authz Success)

    show run int gi0/7
    ! interface GigabitEthernet0/7
    !   switchport mode access
    !   authentication host-mode multi-auth
    !   authentication open
    !   authentication order mab dot1x
    !   authentication priority dot1x mab 
    !   authentication port-control auto
    !   authentication periodic
    !   authentication time reauthentication server
    !   mab
    !   dot1x pae authenticator
    !   dot1x timeout tx-period 10
    !   spanning-tree portfast
    ! end
    ```
+ Demo: PC AnyConnect Network Profile Config
    + Config profile: AnyConnect Secure Mobility Client > Network > Configuration Add: Media=Wired, Name=Engineering, Security=802.1x, 802.1x Xonfig=(password, EAP-FAST) > Close
    + Validate Profile: AnyConnect Secure Mobility Client > Network Profile = Engineering
        + Break connectivity via RDP to current PC
        + Trusted certificate cannot be verified

+ Demo: Install AnyConnect Profile Editor
    + Download profile editor
    + Install: VPN and NAM Profile Editors
    + Domain Certificate: AD CS Server
        + Download a CA certificate, certificate chain or CRL
        + Download CA Certificate: DER encoding/Base 64 -> Root-CA-Base64.cer, Root-CA-DER.cer
    + Network Section > Wired > Edit: User Auth: Include Root Certificate Authorities (CA) certificate > Add: Root-CA-Base64.cer
    + Save profile: File > Save/Save As: Our-New-NAM-profile.xml

+ Demo: Adding CA Certificate
    + `mmc` > File > Add/Remove Snap-in > Certificate > Add > Computer Account > Next > Local Computer > Finish > ok
    + `mmc` > Console Root > Certificates > Trusted Root Certification Authorities (rc) > All Tasks > Import > Import Wizard > File Nmae=Root-CA-Base64.cer > Certificate Store=Trusted Root Certification Authorities > Next > Finish


