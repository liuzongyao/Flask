pipeline {
    agent python
    stages {
        stage('build') {
            steps {
                /*sh 'python get-pip.py --user'*/
                sh 'echo build'
            }
        }
        stage('install') {
            steps {
            	/*sh 'sleep 1000'*/
                sh 'pip install -r requirements.txt --user'
            }
        }
        stage('test') {
            steps {
                sh 'python jenkins_redwood.py'
                sh 'echo finished'
                sh 'sleep 3000'            
            }
        }
    }
}
