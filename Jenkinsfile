pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python get-pip.py --user'
                sh 'export PATH=/var/jenkins_home/.local/bin:$PATH'
            }
        }
        stage('install') {
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
