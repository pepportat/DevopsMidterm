# DevOps Midterm Project

## Project Description

This project involves setting up
a small web application and
automating its deployment 
and environment configuration.
The main goal is to simulate a real
devops work on a local machine.

## Tools and Tech used:
- **Web Application**: Flask (Python-based)
- **Version Control**: GitHub
- **CI/CD**: GitHub Actions
- **Infrastructure as Code (IaC)**: Ansible
- **Deployment Strategy**: Blue-Green Deployment



### CI/CD explanation
The pipeline is triggered automatically when changes are pushed to any branch
Pull requests to the main branch trigger test execution
All unit tests are run automatically to verify application functionality




### IaC (Ansible) Explanation
The ansible playbook instaalls the dependencies and sets up the environment
it also handles deployment.
Uses blue-green deployment strategy to ensure zero downtime.
Health checks verify the new deployment before switching traffic


# Running the Project Locally

- Clone the repository
- Install Ansible: sudo apt install ansible (will need WSL)
- Navigate to the destination folder
- Run the setup playbook: ansible-playbook setup.yml --ask-become-pass (last part needed if you have a password set)
- Access the application at http://localhost:5000 or run the code the same way as it is done in the screenshots


**Note**: Screenshots, steps and some other parts are included in the PDF file.
