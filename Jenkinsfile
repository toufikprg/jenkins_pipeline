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

stage('Deploy') {
    steps {
        sh '''
        . venv/bin/activate
        nohup python manage.py runserver 0.0.0.0:8000 &
        '''
    }
}
