pipeline {
  environment {
    registry = "stash1001/stash1001/alpr-api"
    registryCredential = '22f8c8c3-9914-4222-9b9c-9f44267a05f3'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git credentialsId: 'a75d2253-13b4-4d48-9dcd-69b4218bb550', url: 'git@github.com:stash1001/stash1001/alpr-api.git'
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Clean up docker') {
      steps{
        sh label: '', script: ' docker rm -f alpr_alpr-api_pipeline$BUILD_NUMBER'
      }
    }
  }
}