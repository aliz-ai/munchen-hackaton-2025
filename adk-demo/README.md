1. Log in to GCP using a web browser.

2. Type “Workbench” in the search field and click on the result.

3. Click **“Create New”**.

4. Name the new instance anything you'd like, for example: *adk-samples*.

5. Uncheck the option **Enable Dataproc Serverless Interactive Sessions**.

6. Make sure the region is set to **us-central1**.

7. Click **Create** to start the Workbench instance.

8. Once the instance starts, click **“Open JupyterLab”** next to its name.

9. Download the `setup.sh` file from your this repo.

10. Upload `setup.sh` to the starting directory (Jupyter home) in the JupyterLab window.

11. Open a new terminal window in JupyterLab.

12. Source the setup script:
    ```bash
    . setup.sh
    ```

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

16. Run the demo server:
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