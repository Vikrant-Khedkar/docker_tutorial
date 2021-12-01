#This is a news app(Webapp) To host news. It is dockerized and deployed on minikube
Read this : https://amazing-hound-eb9.notion.site/Create-Kubernetes-Deployment-3dab8d09d17843bb958e378f4d0342b0
# Create Kubernetes Deployment

- 1.Create a app
    
    https://github.com/Vikrant-Khedkar/docker_tutorial or any flask app
    
- 2.Create a Docker iamge of it.
    - 2.1. Create a dockerfile.
        
        ```jsx
        FROM python:3.8-slim-buster
        
        WORKDIR /python-docker
        
        COPY requirements.txt requirements.txt
        RUN pip3 install -r requirements.txt
        
        COPY . .
        
        CMD [ "python3", "-m" , "flask", "run","0.0.0.0"]
        ```
        
    - 2.2 Create a docker-compose.yml file
        
        ```yaml
        version: "3.8"
        services:
          app:
            build: .
            command: python app.py
            ports:
              - "5000:5000"
            volumes:
              - .:/python-flask
        ```
        
    - 2.3 Create Docker Image
        
        ```yaml
        docker build -t newsapp_app . 
        #(newsapp is name given to image)
        ```
        
    - 2.4 Run the image to test it
        
        ```yaml
        docker run -p 5000:5000 newsapp_app
        ```
        
    
- 3.Upload Image to DockerHub
    - 3.1. Retag the image created earlier with Dockerhub username
        
        ```c
        docker tag <existing-image> <hub-user>/<repo-name>
        ```
        
    - 3.2 Push the image to DockerHub
        
        ```c
        docker push <hub-user>/<repo-name>
        ```
        
    
- 4.Create a deployment.yaml File
    
    ```c
    apiVersion: v1
    kind: Service
    metadata:
      name: flask-test-service
    spec:
      selector:
        app: flask-test-app
      ports:
      - protocol: "TCP"
        port: 6000
        targetPort: 5000
      type: LoadBalancer
    
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: flask-test-app
    spec:
      selector:
        matchLabels:
          app: flask-test-app
      replicas: 5
      template:
        metadata:
          labels:
            app: flask-test-app
        spec:
          containers:
          - name: flask-test-app
            image: vikrantkhedkar/newsapp_app
            imagePullPolicy: IfNotPresent
            ports:
            - containerPort: 5000
    ```
    
- 5.Create a deployment
    
    ```c
    kubectl 
    apply -f .\deployment.yaml
    ```
    
- 6.Open minikube dashboard
    
    ```c
    minikube dashboard
    ```
    
- 6.Start the service
    
    ```jsx
    minikube service flask-test-service 
    #name of the service
    ```
    

GitHub: https://github.com/Vikrant-Khedkar/docker_tutorial

Requirements:

- python
- flask
- kubectl
- minikube
- docker
- dockerhub
