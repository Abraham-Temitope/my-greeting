Hey everyone, I just wrapped up a fun little project called "my-greeting" – it's a simple Flask app that serves up a "Hello World" message with a personal touch. I built it as a way to dive into Python web development, Docker, and deploying to AWS with CI/CD. The app runs on port 5000 and can be containerized for easy deployment.To get it running locally:

    Clone the repo: git clone https://github.com/Abraham-Temitope/my-greeting.git
    Set up a virtual environment: python3 -m venv myenv and source myenv/bin/activate
    Install dependencies: pip install -r requirements.txt
    Run the app: python app.py
    Visit http://localhost:5000 to see the greeting.

For the full CI/CD setup, I used Jenkins to automate testing, building the Docker image, pushing to ECR, and deploying to EKS. It's a basic but solid pipeline for beginners like me getting into DevOps. Check out the Jenkinsfile for the details.If you're interested in how I set it up or want to collaborate, drop a comment or message me. Always looking to learn more!
