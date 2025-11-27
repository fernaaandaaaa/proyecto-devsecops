pipeline {
    agent any

    environment {
        // Nombre del scanner que configuraste en Jenkins
        SONAR_SCANNER = 'SonarQubeScanner'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/fernaaandaaaa/proyecto-devsecops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeScanner') {
                    sh '''
                        source venv/bin/activate
                        sonar-scanner \
                        -Dsonar.projectKey=proyecto-devsecops \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://localhost:9000
                    '''
                }
            }
        }

        stage("Dependency Check") {
            steps {
                sh '''
                    dependency-check.sh \
                    --scan . \
                    --out dependency-check-report \
                    --format HTML
                '''
            }
        }

        stage('Run Python App') {
            steps {
                sh '''
                    source venv/bin/activate
                    python3 vulnerable_server.py &
                    sleep 5
                '''
            }
        }

    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
