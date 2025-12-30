pipeline {
    agent any

    stages {
        // Stage 1: Clone the Repo
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
                git 'https://github.com/azan04/Final.git'
            }
        }

        // Stage 2: Run Unit Tests
        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                // Install requirements (ensure python/pip is installed on the agent)
                sh 'pip install -r requirements.txt' 
                // Run tests (adjust based on your test framework, e.g., pytest)
                sh 'python -m unittest discover' 
            }
        }

        // Stage 3: Build the App
        stage('Build') {
            steps {
                echo 'Building Docker Image...'
                [cite_start]// Builds the image using the Dockerfile in the current directory [cite: 14]
                sh 'docker build -t my-flask-app .' 
            }
        }

        // Stage 4: Deploy the App
        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
                [cite_start]// Stop and remove any existing container with the same name to avoid conflicts [cite: 17]
                sh 'docker stop flask-container || true'
                sh 'docker rm flask-container || true'
                
                [cite_start]// Run the new container, mapping port 5000 [cite: 17]
                sh 'docker run -d -p 5000:5000 --name flask-container my-flask-app'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
