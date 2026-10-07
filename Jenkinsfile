pipeline {

    agent any

    environment {

        DOCKER_HOST = 'npipe:////./pipe/dockerDesktopLinuxEngine'

        DOCKERHUB_USERNAME = 'anasqdev'

'

        IMAGE_NAME = 'employee-management-api'

    }

    stages {

        stage('Python Tests') {

            steps {

                echo 'Running Python Tests'

                bat '''
                python --version
                python -m pip install -r requirements.txt
                python -m pytest
                '''
            }
        }


        stage('Docker Build') {

            steps {

                echo 'Building Docker Image'

                bat '''
                docker build -t %IMAGE_NAME%:%BUILD_NUMBER% .

                docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest

                docker tag %IMAGE_NAME%:%BUILD_NUMBER% %DOCKERHUB_USERNAME%/%IMAGE_NAME%:%BUILD_NUMBER%

                docker tag %IMAGE_NAME%:%BUILD_NUMBER% %DOCKERHUB_USERNAME%/%IMAGE_NAME%:latest
                '''
            }
        }


        stage('Docker Hub Login') {

            steps {

                echo 'Logging into Docker Hub'

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {

                    bat '''
                    echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin
                    '''
                }
            }
        }


        stage('Docker Push') {

            steps {

                echo 'Pushing Docker Image to Docker Hub'

                bat '''
                docker push %DOCKERHUB_USERNAME%/%IMAGE_NAME%:%BUILD_NUMBER%

                docker push %DOCKERHUB_USERNAME%/%IMAGE_NAME%:latest
                '''
            }
        }
    }


    post {

        success {

            echo '======================================'
            echo 'DOCKER IMAGE SUCCESSFULLY PUSHED'
            echo '======================================'
        }

        failure {

            echo '======================================'
            echo 'PIPELINE FAILED'
            echo '======================================'
        }
    }
}