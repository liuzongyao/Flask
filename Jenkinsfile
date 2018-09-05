pipeline {
    agent { docker { image 'python:2.7.5' } }
    stages {
        stage('build') {
            steps {
                sh 'python helloworld.py'
            }
        }
    }
}
