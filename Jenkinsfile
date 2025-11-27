    pipeline {
    agent any

    environment {
       environment {
    PROJECT_NAME   = "pipeline-test"
    SONARQUBE_URL  = "http://sonarqube:9000"
    SONARQUBE_TOKEN = "sqa_1c832b7d13f4adc047f10ac114a7f93c04402903"
    TARGET_URL      = "http://172.26.245.185:5000"
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
