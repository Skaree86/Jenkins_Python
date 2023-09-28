pipeline {
  agent any
  stages {
    stage('version') {
      agent {Monthy}
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 script.py'
      }
    }
  }
}
