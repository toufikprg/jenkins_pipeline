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
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                python manage.py check
                python manage.py test
                '''
            }
        }

        stage('Configure ALLOWED_HOSTS') {
            steps {
                sh '''
                . venv/bin/activate
                sed -i "s/^ALLOWED_HOSTS = .*/ALLOWED_HOSTS = ['192.168.116.135', 'localhost', '127.0.0.1']/" gestion_absence/settings.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                . venv/bin/activate
                nohup python manage.py runserver 0.0.0.0:8000 &
                '''
            }
        }
    }
}
