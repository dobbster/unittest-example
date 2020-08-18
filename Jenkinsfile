// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any

    stages {
		stage('Clean-up') {
			steps {
			    echo 'Cleaning up...'
				// Delete existing jenkins workspace
				step([$class: 'WsCleanup'])

				// Delete existing remote deployment if any exists
				sshagent(credentials : ['harsh-q-ec2']) {
					sh 'ssh -t -t ec2-user@ec2-23-20-82-169.compute-1.amazonaws.com -o StrictHostKeyChecking=no "rm -rf test/ verify/ main.py setup.sh || true"'
                }
				
			}
		}
        stage('Checkout SCM') {
            steps {
                echo 'Github Checkout..'
				// git clone
			    git credentialsId: 'cc0499d4-450b-4723-9c92-6bd734254373', url: 'https://github.com/dobbster/unittest-example.git'
            }
        }
		stage('Build') {
            steps {
                echo 'Building..'
				// build
				sshagent(credentials : ['harsh-q-ec2']) {
		            sh 'ssh -o StrictHostKeyChecking=no ec2-user@ec2-23-20-82-169.compute-1.amazonaws.com uptime'
		            sh 'ssh -v ec2-user@ec2-23-20-82-169.compute-1.amazonaws.com'
					//Copy files to ec2 code server
		            sh 'scp -r $WORKSPACE/test ec2-user@ec2-23-20-82-169.compute-1.amazonaws.com:~'
		            sh 'scp -r $WORKSPACE/verify ec2-user@ec2-23-20-82-169.compute-1.amazonaws.com:~'
					sh 'scp $WORKSPACE/main.py ec2-user@ec2-23-20-82-169.compute-1.amazonaws.com:~'
					sh 'scp $WORKSPACE/setup.sh ec2-user@ec2-23-20-82-169.compute-1.amazonaws.com:~'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
				// Run unittests
				sshagent(credentials : ['harsh-q-ec2']) {
					// Creates virtual env and runs unittest
 					sh 'ssh -t -t ec2-user@ec2-23-20-82-169.compute-1.amazonaws.com -o StrictHostKeyChecking=no "bash setup.sh"'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Deploy
				sshagent(credentials : ['harsh-q-ec2']) {
					// Executes python app
 					sh 'ssh -t -t ec2-user@ec2-23-20-82-169.compute-1.amazonaws.com -o StrictHostKeyChecking=no "python verify/verify.py"'
				}
            }
        }
    }
}
