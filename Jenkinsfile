pipeline {
    agent {label "docker"}
    stages {
        stage('build') {
            steps {
                sh 'python get-pip.py --user'
            }
        }
        stage('install') {
            steps {
            	sh 'sleep 1000'
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
