# Sponsor Portal

## Sponsor Portal with Guest Access

+ Guest Accessing using ISE: Provisioning Temporary User Accounts for Guests
    + Portals
    + Redirect adn Wen Authentication
    + Credential Options
        + Sponsors
        + Self-Registration

+ Portals
    + Administrator portals: config policy, reports, etc.
    + Sponsor Portal: lobby ambassador, PSN (print, email, text)
        + CWA = Centralized Web Authentication =  Web Based User Authentication
        + Self registration - useful identifier


## Implementing a Server Portal on ISE

+ Implementing the ISE Sponsor Portal: Allowing the Lobby Ambassador
    + SMTP Service on ICE
    + Web Portal Configuration
    + Creating Guest Accounts

+ Demo: ISE
    + Standard Guest Identity Groups <br/>
        Administration > Identity Management > Groups > User Identity Groups (default: ActivatedGuest, Employee, Guest, SponsorAllAccount, SponsorGroupAccounts, SponsorOwnAccount)
    + Send Outbound Message <br/>
        Administration > System > Settings > SMTP Server > SMTP Server Settings: SMTP Server=??
    + Create Guest Account
        + Administration > Web Portal Management > Settings > General > Ports: Black List Portal(HTTPS=8443), Guest Portal and Client Provisioning Portal (HTTPS=8443), My Device Portal (HTTPS=8443), Sponsor Portal (HTTPS=8443)
        + Administration > Web Portal Management > Settings > Sponsor > Language Template > (English, ...) > Config Email Notification > Subject=..., Self-registry Credentials, Config SMS Text Message Notification
        + Administration > Web Portal Management > Settings > Guest > Details policy - select fields required (Mandatory, Optional, Unused) to create Guest Account > Save
    + Authority to Create Guest Account
        + Administration > Web Portal Management > Sponsor Group Policy > Manage All Account: Identity Group=Any, Aconditions=(AD1:ExternalGroups EQUALS nuglab.com/Users/Domain Users), Sponsor Groups_SponsorAllAccounts
        + Administration > Web Portal Management > Settings > Sponsor > Authentication sources: Identity Store Sequence=Use_AD_then_Local
    + Content of Identity Sequence <br/>
        Administration > Web Portal Management > Identity Source Sequences > Use_AD_then_Local: Search List=(AD1, Internal Users, Guest Users)

+ Demo: Sponsor Portal 
    + IE (https://www.google.com) > Sponsor Portal (port 8443) > user=it-bob, pwd=Nugget!23, Create Account: first name, last name, Guest Role=(Guest/Activated Guest), Account Duration=DefaultEightHours > Submit
    + Account List - functions: Edit | Email, Print | Reinstate, Suspend | Delete | Change Account Duration



    