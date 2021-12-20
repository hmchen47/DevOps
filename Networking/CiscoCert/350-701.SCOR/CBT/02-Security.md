# 02. Compare Common Security Vulnerabilities

Trainer: Knox Hutchinson


## Introducing Common Attack Vectors

- What to learn
  - how attackers exploit vulnerabilities
  - common attack methods
  - why it's important to handle attacks correctly


## Get to Know OWASP

- OWASP foundation
  - [Open Web Application Security Project](https://owasp.org/) (OWASP)
  - improving the security
  - some important projects
    - [OWASP Top 10](https://owasp.org/www-project-top-ten/): a standard awareness document for developers and web application security
    - [OWASP Cheat Sheet Series](https://owasp.org/www-project-cheat-sheets/): providing a set of simple good pracice guides for appplication developers and defenders to follow
    - [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/): the premier cybersecurity testing resource for web application developers and security professionals
    - [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/): attempting to detect publicly disclosed vulnerabilities contained within a project’s dependencies


## The SQL Injection’; SELECT * FROM table

- 3-tier application architecture
  - tiers: web, app, and db
  - typical data flow: web or mobile apps / Kiosk (frontend) $\rightleftarrow$ application server (backend) $\rightleftarrow$ SQL database
  - frontend: web browser
  - backend: analytics, customer support, shipping, etc.
  - SQL db: storing cell files w/ SQL


- SQL injection
  - code sending code to app server or db directly
  - malicious procedure
    - web input field w/ SQL code to query info, e.g. `SELECT * FROM Table`
    - possible SQL statements: `INSERT`, `DELETE`, `DROP`, etc.
    - retrieve/delete user's sensitive info or insert brough data
  - mitigation: backend validates the SQL statement


- Demo: SQL injection
  - resource: [SQL Injection exercise](https://www.hacksplaining.com/exercises/sql-injection#/start)
  - web input: email = `user@email.com` password = `password` $\to$ Unknown email or password

    ```shell
    Rendering login page.
    Checking supplied authentication details for user@email.com.
    Finding user in database.
    No such user, report this to the user (invalid credentials?).
    Rendering login page.
    ```

  - web input: email = `user@email.com` password = `password'` $\to$ An unexpected error occurred.
    - logs: The logs show a SQL syntax error. This indicates that athe quote characterr messed somthing up in an unexpeccted way.

      ```shell
      Checking supplied authentication details for user@email.com.
      Finding user in database.
      An error occurred: PG::SyntaxError: ERROR: unterminated quoted string at or near "'password'' limit 1" LINE 1: ...ers where email = 'user@email.com' and password = 'password'... ^ : select * from users where email = 'user@email.com' and password = 'password'' limit 1.
      Unable to login this user due to unexpected error.
      Rendering login page.
      ```

    - translated SQL code

      ```sql
      SELECT *
        FROM users
       WHERE email = 'user@email.com'
          AND pass  = 'password'' LIMIT 1
      ```
    
    - repeat the above input and observe the result
    - This behavior indicates that the application might be valuable to SQL INjection

      ```sql
      SELECT *
        FROM users
       WHERE email = 'user@email.com'
         AND pass  = 'password'' LIMIT 1
      ```

  - web input: email = `user@email.com` password = `' or 1=1--`
    - We successfully gained access to the application without having to guess the password using SQL Injection.

    ```sql
    SELECT *
      FROM users
     WHERE email = 'user@email.com'
       AND pass  = '' or 1=1--' LIMIT 1
    ```



## Cross-Site Scripting; var doCode{}

- Cross-site scripting
  - input field of web in 3-tier application w/ JS code, e.g., `<script> alert(); </script>`
  - JS code exected in web browser immediately
  - browser holding Cookie or token $\to$ probably sent to a malicious website
  - other possibilities: JS sending malicious data to server and DB 


- Demo: XSS attack
  - resource:
    - [Test Your XSS Skills Using Vulnerable Sites](https://bit.ly/3Eh9eix)
    - [Google XSS Game](https://xss-game.appspot.com/)
  - level 1:
    - input field: `<script>alert();</script>`
    - fire JS `alert` function 
    - related code snippet: [python code](src/02-l1-level.py)
  - level 2:
    - HTML code handling script text to handle script injection
    - input field: `<img src="" onerror="alert();" />`
    - sending JS code w/o `script` tag
    - related code snippets: [HTML](src/02-l2-index.html), [Python](src/02-l2-level.py), [JS](src/02-l2-post-store.js)



## Password Protection



## Plain-Text Protocols



## The Buffer Overflow



## Summarizing Common Vulnerabilities




