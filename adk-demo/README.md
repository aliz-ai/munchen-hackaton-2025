## If you have a computer with a linux terminal and a default python 3.12 env, and poetry installed

1. Install ADK in the python 3.12 env
    ```
    pip install google-adk==1.4.2
    ```
2. Clone the the ADK samples repo to some appropriate location
    ```
    git clone https://github.com/google/adk-samples.git
    cd adk-samples
    git reset --hard 5465f64
    ```

## If you don't have the above installed on your computer

1. Log in to GCP using a web browser.

2. Type “Workbench” in the search field and click on the result.

3. Click **“Create New”**.

4. Name the new instance anything you'd like, for example: *adk-samples*.

5. Uncheck the option **Enable Dataproc Serverless Interactive Sessions**.

6. Make sure the region is set to **us-central1**.

7. Click **Create** to start the Workbench instance.

8. Once the instance starts, click **“Open JupyterLab”** next to its name.

9. Open a new terminal window in JupyterLab.

10. Clone the following repository:
    ```
    ```

11. Source the setup script, this will set up the python environment, install adk and clone the adk-samples repository:
    ```bash
    . munchen-hackathon-2025/adk-demo/setup.sh
    ```

12. At this point you can decide what to do, try to create a new agent, or check out the academic-research sample agent. The following assumes you picked the latter, for creating a new agent, see below. As for the samples the other ones can be tested in a similar fashion, but may not work as they require additional GCP resource setup. The hackaton demo agents should be working though. 

13. Navigate to the selected demo directory:
    ```bash
    cd adk-samples/python/agents/academic-research
    ```

14. Create a `.env` file and add the following content:
    ```env
    GOOGLE_GENAI_USE_VERTEXAI=1
    GOOGLE_CLOUD_PROJECT=<project_name>
    GOOGLE_CLOUD_LOCATION=us-central1
    ```

15. Install the packages with Poetry:
    ```bash
    poetry install
    ```

16. When you run the demo server, it searches through the subdirectories of the current directory, or the directory specified in the command, and parses any agent it can find, and only those it can find in the immediate subdirectories.
To Run the demo server:
    ```bash
    poetry run adk web --host 0.0.0.0
    ```

17. Install `gcloud` on your **local machine**, if not already installed:  
    https://cloud.google.com/sdk/docs/install

18. Authenticate using `gcloud`:
    ```bash
    gcloud auth login
    ```

19. Open an SSH tunnel to the Workbench instance:
    ```bash
    gcloud compute ssh <workbench_name> \
      --project=<gcp_project_name> \
      --zone=<workbench_zone> \
      -- -L 8000:localhost:8000
    ```

20. Open the demo in your local browser at:
    ```
    http://localhost:8000
    ```
    
## Creating a new agent
1. In general it is recommended to create a new python environment for every new project, however in this case for simplicity let's just use the default env.
```
adk create <agent_name> --model gemini-2.5-pro
```
2. For the questions:
- pick Vertex AI
- specify the provided GCP project
- set region as us-central1

3. Check the generated files, you need to edit the agent.py. If your agent needs additional packages make sure you install them.

4. The agent can be tested in a similar fashion as the academic-research assistant above (see 16), except that since we didn't use poetry to create a virtual environment, the default environtment has to be used, so simply run the web UI with
```
adk web --host 0.0.0.0
```

## Links
ADK intro
https://google.github.io/adk-docs/

ADK API doc
https://google.github.io/adk-docs/api-reference/python/google-adk.html
