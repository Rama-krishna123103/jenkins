pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ramakrishna123456'
        KUBERNETES_NAMESPACE = 'default'
        DEPLOYMENT_NAME = 'iris-model-deployment'
        SERVICE_NAME = 'iris-model-service'
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    // Explicitly check out the desired branch or commit
                    git branch: 'main', url: 'https://github.com/Rama-krishna123103/jenkins.git/'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        docker.image(DOCKER_IMAGE).push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Apply Kubernetes deployment and service configurations
                    sh 'kubectl apply -f k8s/deployment.yaml'
                    sh 'kubectl apply -f k8s/service.yaml'
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
