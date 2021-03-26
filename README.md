# hello-edison-python
This is a Python program for building a microservice in Kubernetes and Docker. <br />

<b> Repository structure: </b> <br />
The main files in this repository are: <br />
Dockerfile: Specifies how the application is built and packaged. <br />
deployment files/edison-python-deployment.yaml: Contains a templated Kubernetes deployment file. <br />
deployment files/edison-python-service.yaml: Contains values that will be instantiated into the Kubernetes. <br />
service/src/app.py: The core Python/Flask application. <br />

<b> Dependencies: </b> <br /> 
Flask and Redis.
