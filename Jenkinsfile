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
      build(
        job: 'service-containers/master', 
        parameters: [
          string(name: 'JOB_NAME', value: "${env.JOB_NAME}")
        ]
      )
    }
  }
}
