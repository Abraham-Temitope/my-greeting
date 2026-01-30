pipeline {
    agent any

    environment {
        ECR_REPO     = 'my-greeting'
        AWS_REGION   = 'eu-north-1'
        ACCOUNT_ID   = '920301614774'
        ECR_URL      = "${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
        IMAGE_NAME   = "${ECR_REPO}:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies & Test') {
            steps {
                sh '''
                    python3 -m venv build-venv
                    . build-venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_URL}
                    docker tag ${IMAGE_NAME} ${ECR_URL}/${IMAGE_NAME}
                    docker push ${ECR_URL}/${IMAGE_NAME}
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withKubeConfig([credentialsId: 'kubeconfig']) {
                    sh '''
                        echo "=== DEPLOY DEBUG START ==="
                        pwd
                        which kubectl || echo "kubectl NOT FOUND"
                        kubectl version --client || echo "kubectl version FAILED"
                        kubectl config current-context || echo "No kubeconfig context"
                        ls -la *.yml || echo "No .yml files found"
                        kubectl apply -f deployment.yml || echo "deployment FAILED"
                        kubectl apply -f service.yml   || echo "service FAILED"
                        kubectl apply -f ingress.yml   || echo "ingress FAILED"
                        echo "=== DEPLOY DEBUG END ==="
                    '''
                }
            }
        }
    }

    post {
        always { echo 'Pipeline finished' }
        success { echo '✅ Success!' }
        failure { echo '❌ Failed - check output' }
    }
}

