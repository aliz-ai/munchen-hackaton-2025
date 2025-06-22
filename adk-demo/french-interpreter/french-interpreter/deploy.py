import vertexai
import os
from dotenv import load_dotenv
from vertexai import agent_engines

from agent import root_agent

load_dotenv()

GOOGLE_CLOUD_PROJECT = os.getenv('GOOGLE_CLOUD_PROJECT',)
GOOGLE_CLOUD_LOCATION = os.getenv('GOOGLE_CLOUD_LOCATION')
GOOGLE_CLOUD_STORAGE_BUCKET = os.getenv('GOOGLE_CLOUD_STORAGE_BUCKET')

vertexai.init(
    project=GOOGLE_CLOUD_PROJECT,
    location=GOOGLE_CLOUD_LOCATION,
    staging_bucket=GOOGLE_CLOUD_STORAGE_BUCKET,
)

remote_app = agent_engines.create(
    agent_engine=root_agent,
    requirements=[
        "google-cloud-aiplatform[adk,agent_engines]"   
    ]
)

print("Remote app:", remote_app.resource_name)
print("testing remote app...")
remote_session = remote_app.create_session(user_id="u_456")

message = "Hello!"
print(f"User message: {message}")
for event in remote_app.stream_query(
    user_id="u_456",
    session_id=remote_session["id"],
    message=message,
):
    print(event)
