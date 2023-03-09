# Steps to install Jenkins
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
6. Open terminal and run mongodb image
```
docker run -d -p 27017:27017 --name m1 mongo
```
