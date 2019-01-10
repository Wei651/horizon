pipeline {
  agent any
 
  stages {
    stage('package') {
      environment {
        PBR_VERSION = "${env.BRANCH_NAME}"
      }
      steps {
        sh 'python setup.py sdist'
        archiveArtifacts(artifacts: 'dist/*', onlyIfSuccessful: true)
      }
    }
  }
}
