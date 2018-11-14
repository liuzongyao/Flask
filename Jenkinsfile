pipeline {
    agent  {label  "python"}
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
                /*sh 'pip install -r requirements.txt --user'*/
                sh 'echo install'
            }
        }
        stage('test') {
            steps {
                sh 'python helloworld.py'
                sh 'echo finished'
                sh 'sleep 60'            
            }
        }
    }
}
