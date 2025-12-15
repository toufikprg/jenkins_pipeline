pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/toufikprg/jenkins_pipeline.git', branch: 'master'
            }
        }
        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                source venv/bin/activate
                python manage.py check
                python manage.py test
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                source venv/bin/activate
                nohup python manage.py runserver 0.0.0.0:8000 &
                '''
            }
        }
    }
}
