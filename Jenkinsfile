pipeline {
  agent any
 
  options {
    copyArtifactPermission(projectNames: 'horizon-container')
  }

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

  post {
    success {
      build job: 'horizon-container', parameters: [string(name: 'BRANCH_NAME', value: "${env.BRANCH_NAME}")]
    }
  }
}
