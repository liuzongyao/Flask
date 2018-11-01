pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python get-pip.py --user'
            }
        }
        stage('install') {
            steps {
                sh 'pip install -r requirements.txt --user'
            }
        }
        stage('test') {
            steps {
                sh 'python helloworld.py'
            }
        }
    }
}
