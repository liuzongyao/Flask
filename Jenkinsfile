pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python get-pip.py'
            }
        }
        stage('test') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('test') {
            steps {
                sh 'python jenkins_redwood.py'
            }
        }
    }
}
