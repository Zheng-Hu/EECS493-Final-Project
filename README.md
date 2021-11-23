# EECS493-Final-Project

## Quick-Start Guide
1. Clone the GitHub repository

2. Open up a new bash terminal with `backend` as the current directory (`cd backend`)

3. Download and install Docker Desktop. To install follow the link and download the installed. Once downloaded follow the system prompts to complete the install process.
   * [Mac](https://docs.docker.com/docker-for-mac/install/)
   * [Windows](https://docs.docker.com/docker-for-windows/install/)
   * [Linux distributions](https://docs.docker.com/engine/install/#server)

4. Run `make local-start` to start the backend

5. Navigate to the frontend directory
  ```
  cd ..
  cd frontend
  ```

6. Install npm ([help](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm))

7. Install the packages for this project (`npm install`)

8. Compile the project (ready for hot-reloads) (`npm run serve`)

9. Navigate to the Local URL, most likely `http://localhost:8081/`

10. Once done, Control-C to stop the frontend, and then navigate to backend directory and stop server:
  ```
  cd ..
  cd backend
  make local-clean
  ```
