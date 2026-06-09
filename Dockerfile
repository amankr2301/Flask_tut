# 1. Base Image: Downloads a tiny Linux environment with Python 3.10 pre-installed
FROM python:3.10

# 2. Port Slot: Tells Docker to open up port 5000 on the container's wall for traffic
EXPOSE 5000

# 3. Workbench: Creates a folder named /app inside the container and moves inside it
WORKDIR /app

# 4. Build Step: Installs Flask directly inside the container's isolated Python environment
RUN pip install flask 

# 5. File Copier: Copies all files from your current local directory into the container's /app folder
COPY . .  

# 6. Ignition Switch: Runs ONLY when the container boots up. 
# "--host 0.0.0.0" forces Flask to listen to incoming requests from outside the container box
CMD ["flask" , "run" , "--host" , "0.0.0.0"]