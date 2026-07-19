pipeline {
    agent any
    
    parameters {
        choice(
            name: 'BROWSER',
            choices: ['chrome', 'firefox'],
            description: 'Browser for UI tests'
        )
    }

    environment {
        API_URL = credentials('api-url')
        UI_URL  = credentials('ui-url')
    }
 
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
 
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    . venv/bin/activate
                    ruff check .
                '''
            }
        }
 
        stage('Run API tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest api/tests --alluredir=allure-results
                '''
            }
        }
 
        // тесты могут выполняться долго при загрузке automationexercise.com без VPN
        stage('Run UI tests') {
            steps {
                script {
                    withEnv(["BROWSER=${params.BROWSER}"]) {
                        sh '''
                            . venv/bin/activate
                            pytest ui/tests \
                            --browser $BROWSER \
                            --alluredir=allure-results
                        '''
                    }
                }
            }
        }
    }
 
    post {
        always {
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'allure-results']]
        }
    }
}