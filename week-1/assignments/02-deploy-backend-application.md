# Assignment 2: Deploy a Simple Spring Boot App on Compute Engine



## Objective

Deploy a basic Spring Boot REST API on a Google Compute Engine VM that supports CRUD operations:

- GET

- POST

- PUT

- DELETE



---



## Prerequisites

- GCP account set up (Assignment 1 completed)

- Basic Java + Spring Boot familiarity



---



# 1. Create a Compute Engine VM



Go to Compute Engine → VM Instances → Create Instance



Configuration:

- Name: springboot-vm

- Machine type: E2-small

- OS: Ubuntu

- Enable HTTP traffic

- Enable HTTPS traffic



Click Create



---



# 2. Connect to VM



Click SSH on your instance.



---



# 3. Install Dependencies



sudo apt update

sudo apt install -y openjdk-17-jdk maven git



Check versions:



java -version

mvn -version



---



# 4. Create Spring Boot App



Using the (Spring Initializer)\[start.spring.io] build a simple app. The example endpoints uses items but track whatever you like



Create REST endpoints:

- GET /items

- GET /items/{id}

- POST /items

- PUT /items/{id}

- DELETE /items/{id}



Use in-memory storage (List or Map).



---



# 5. Run Application



mvn spring-boot:run



App runs on:

http://localhost:8080



---



# 6. Push application to github in your repository



Add the simple project you've written to github in your personal repo in the organization. Use git clone to pull your project into the Compute Engine instance and start it up using the previous instructions



# 7. Expose to Internet



Create firewall rule:

- allow-8080

- source: 0.0.0.0/0

- allow all ports



Get external IP:

Compute Engine → VM Instances



Open:

http://<EXTERNAL\_IP>:8080



---



# 8. Test API



GET /items

POST /items

PUT /items/{id}

DELETE /items/{id}



Example POST:

{

   "name": "Test Item",

   "description": "Sample item"

}



---



# Bonus: Add Database instead of in-memory storage



This can be done by spinning up a database directly within your instance or creating a Cloud SQL instance you can connect to. Give this a shot and try your best!



---



# Deliverables

- VM screenshot

- App running screenshot
- 
- Share link in a text file so we can access your application



---



\# Notes

\- Stop VM when not used

