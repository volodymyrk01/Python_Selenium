# Steps to deploy
1. Install [Homebrew](https://brew.sh/)
2. Install [Jenkins](https://www.jenkins.io/download/lts/macos/) using the Homebrew package manager.
```
brew install jenkins-lts
```
3. Start the Jenkins service:
```
brew services start jenkins-lts
```
4. Browse to http://localhost:8080/ and follow the instructions to complete the installation.
5. Install and run [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/)
6. Open terminal pull and run mongodb image
```
docker pull mongo
docker run -d -p 27017:27017 --name m1 mongo
```
7. Go to http://localhost:8080/ and create "build-and-push-image" pipeline. Click new item -> Enter an item name, select pipeline -> Click on the "GitHub project" checkbox and paste this Project URL "https://github.com/volodymyrk01/Python_Selenium/" -> In the Build Triggers tab click on the "GitHub hook trigger for GITScm polling" checkbox -> Paste this fragment to Groovy Sandbox
```
pipeline {
    agent any
    environment {
    password = credentials('dockerhub')
    }
    stages {
        stage('Building image'){
            steps{
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/volodymyrk01/Python_Selenium']])
                script{
                    sh 'docker build -t myimage .'
                }
            }
        }
        stage('Checking the integrity of framework') {
            steps {
                script{
                        sh 'docker run -v "Path to the directory on the host machine e.g. - /Users/Desktop/docker":/html/ --network host myimage pytest --html=/html/pytest_report.html /app/tests/html_report_generation.py && docker run -v "Your Path":/html/ --network host myimage pytest /app/tests/framework_tests.py'
                }
            }
        }
        stage('Pushing image to hub'){
            steps{
                script{
                    sh 'pip3 install pymongo docker'
                    sh 'python3 utils/mongodb_tests.py "Your repo name and tag name e.g. - user/myimage:version1.2"'
                }
            }
        }
        stage('Running image from test-pipeline'){
            steps{
                build 'test-pipeline'
            }
        }
    }
}
```
9.
