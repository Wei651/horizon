pipeline {
  agent any
 
  environment {
    PBR_VERSION = env.BRANCH_NAME
  }

  stages {
    stage('package') {
      steps {
        sh 'python setup.py sdist'
        archiveArtifacts(artifacts: 'dist/*', onlyIfSuccessful: true)
      }
    }
  }
}
