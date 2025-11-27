pipeline {
    agent any

    environment {
        PROJECT_NAME    = "pipeline-test"
        SONARQUBE_URL   = "http://sonarqube:9000"
        SONARQUBE_TOKEN = "sqa_1c832b7d13f4adc047f10ac114a7f93c04402903"
        TARGET_URL      = "http://172.26.245.185:5000"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/fernaaandaaaa/proyecto-devsecops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                // OJO: el nombre debe ser el del servidor SonarQube que configuraste en Jenkins
                // si allá se llama distinto (por ejemplo "SonarQubeScanner" o "Sonarqube"),
                // cambia ese texto.
                withSonarQubeEnv('Sonarqube') {
                    sh '''
                        . venv/bin/activate
                        sonar-scanner \
                          -Dsonar.projectKey=pipeline-test \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=${SONARQUBE_URL} \
                          -Dsonar.login=${SONARQUBE_TOKEN}
                    '''
                }
            }
        }

        stage('Dependency Check') {
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
                    . venv/bin/activate
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
