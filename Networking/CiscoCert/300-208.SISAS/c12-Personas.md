# ISE Personas

+ Identity Service Engine (ISE) Personas: The Faces of ISE
    + Administration
    + Policy Service
    + Monitoring and Troubleshooting
    + Inline Posture
    + Nodes and Roles

+ Personas
    + Node=ISE
    + Responsibility/Functions ISE providing/include Administration
    + Configuring in the authentication and authorization policies
    + ISE Server:
        + Single server: standalone node, responsible for administration persona and others
        + Multi-servers: primary and secondary implement policies in primary
    + PSN: Policy Service Node, persona for policy serviced
    + Administration Persona: config policy while PSN implement rep policy
    + Most likely having more than one PSN due to large network with many nodes and users
    + Multiple PSNs:
        + fault tolerance
        + load balancing
    + 

+ ISE Persona Deployment 
  <a href="https://www.grandmetric.com/knowledge-base/design_and_configure/cisco-ise-deployment-models/">
      <br/><img src="https://www.grandmetric.com/wp-content/uploads/2017/08/Cisco-ISE-Depolyment-and-NAD-interaction.png" alt="Cisco ISE Deployment models" width="450">
  </a>

