# Spotify UI and REST API Test

This project is a client for interacting with the Spotify API and UI.

## Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Spotify Developer Account (to get your `CLIENT_ID` and `CLIENT_SECRET`)

### Installation

1. Clone the repository
2. Create virtual env: `env/scripts/activate`
2. Install the required packages: `pip install -r requirements.txt`
3. Create a .env file in the root directory of the project and add your Spotify API credentials:
  The `.env` file should look like this:

    CLIENT_ID="your client ID"

    CLIENT_SECRET="your client secret"

### Running Test in parallel with allure report generation
  1. To run the test in parallel: `pytest framework/tests/ -k "xdist_group and (UI or API)" -n 1`
  2. Command for report generation: `python -m pytest framework/tests/ --alluredir allure-results`
  3. Generate report : `allure serve allure-results`

### Steps for building a job in jenkins
    1. Select a freestyle project.
    2. Inside the credintials create the credintials for the  
    CLIENT_ID="your client ID"
    CLIENT_SECRET="your client secret"
    3.Set the build Environment - Use secret text(s) or file(s)
    and create tww variables as Secret text.
#### Build Steps
    Execute Execute Windows batch command
`echo "CLIENT_ID=${CLIENT_ID}" >> .env`
`echo "CLIENT_SECRET=${CLIENT_SECRET}" >> .env`

`python -m venv env`

`env\Scripts\activate.bat`

`pip install -r requirements.txt`

`pip install Webdriver-Manager==4.0.1`
`pytest framework/tests/ --alluredir allure-results `

#### Post-build Actions
Generate allure report 

path `/allure-results`

### For creating the job in pipeline use this pipeline script
    pipeline {
    agent any

        environment {
            CLIENT_ID = 'your_ID'
            CLIENT_SECRET = 'your_SECRET'
        }
        
        stages {
            stage('Checkout') {
                steps {
                    // Checkout the code from GitHub
                    git url: 'https://github.com/adnanakanda/Spotify-Test.git', branch: 'main'
                }
            }
        
            stage('Install Dependencies') {
                steps {
                    // Create a virtual environment and install the necessary dependencies
                    bat '''
                        python -m venv venv
                        call venv\\Scripts\\activate
                        pip install --no-cache-dir -r requirements.txt
                        pip install webdriver-manager==4.0.1
                    '''
                }
            }
        
            stage('Run Tests') {
                steps {
                    // Run tests and generate Allure report
                    bat '''
                        call venv\\Scripts\\activate
                        python -m pytest framework/tests/ --alluredir allure-results
                        allure generate allure-results --clean -o allure-report
                        cd allure-report
                        python -m http.server 8080
                    '''
                }
            }
        
            stage('Post Actions') {
                steps {
                    // Archive the Allure report
                    archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
                }
            }
        }
        
        post {
            always {
                // Clean up workspace
                cleanWs()
            }
        }
    }
