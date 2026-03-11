# Cloud Native Microservice Monitoring

## Project Overview

This project demonstrates the implementation of a cloud-native application using containerization, monitoring, and CI/CD automation. The system includes a microservice that shares the GPS location of a classroom, containerized using Docker, monitored using Prometheus, and automated with a CI/CD pipeline using GitHub Actions.

The goal of this project is to understand how modern DevOps tools work together to build, deploy, monitor, and automate applications in a cloud environment.

---

## Technologies Used

* Docker
* Python (Flask Microservice)
* Prometheus
* cAdvisor
* Git
* GitHub
* GitHub Actions (CI/CD)

---

## Project Structure

```
cloud-native-microservice-monitoring
│
├── task1-microservice
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── deployment.yaml
│   └── service.yaml
│
├── task2-prometheus
│   └── prometheus.yml
│
└── task3-cicd
    └── .github
        └── workflows
            └── docker-image.yml
```

---

# Task 1: GPS Microservice using Docker

A lightweight microservice was created using Python Flask to provide the GPS location of the classroom. The service returns location information in JSON format and runs inside a Docker container.

### Features

* Simple REST API endpoint
* JSON response containing classroom location
* Containerized using Docker for portability

### Example Output

```
{
  "classroom": "Cloud Lab",
  "latitude": 17.3850,
  "longitude": 78.4867
}
```

### Run the Microservice

Build the Docker image:

```
docker build -t gps-service .
```

Run the container:

```
docker run -p 5000:5000 gps-service
```

Access the service:

```
http://localhost:5000
```

---

# Task 2: Container Monitoring using Prometheus

Prometheus was used to monitor container performance. cAdvisor collects metrics from running Docker containers, and Prometheus scrapes these metrics periodically.

### Monitoring Components

* **cAdvisor** – collects container performance metrics
* **Prometheus** – stores and visualizes monitoring data

### Metrics Collected

* CPU usage
* Memory usage
* Network usage
* Container statistics

Prometheus dashboard can be accessed at:

```
http://localhost:9090
```

---

# Task 3: CI/CD Pipeline using GitHub Actions

A CI/CD pipeline was implemented using GitHub Actions to automate the build process of the Docker container.

### Workflow Process

```
Developer Push Code
        ↓
GitHub Repository
        ↓
GitHub Actions Trigger
        ↓
Build Docker Image
```

Whenever code is pushed to the repository, GitHub Actions automatically triggers the workflow and builds the Docker image.

---

# Architecture Overview

```
Microservice (Flask)
        ↓
Docker Container
        ↓
Prometheus Monitoring
        ↓
GitHub Actions CI/CD
```

---

# Learning Outcomes

* Understanding microservice architecture
* Containerizing applications using Docker
* Monitoring container performance using Prometheus
* Implementing CI/CD automation with GitHub Actions
* Integrating DevOps tools into a cloud-native workflow

---

# Conclusion

This project successfully demonstrates the integration of microservices, containerization, monitoring, and CI/CD automation. Docker enables efficient packaging and deployment of applications, Prometheus provides real-time monitoring of container performance, and GitHub Actions automates the build process. Together, these technologies form a robust DevOps pipeline for developing and managing modern cloud-native applications.
