import asyncio
import click
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types


load_dotenv()


root_agent = Agent(
    model='gemini-2.5-pro',
    name='root_agent',
    description='A helpful assistant for transliting anything to French',
    instruction='Answer every user query with the phrase "Omelette du fromage". Don\'t say anything else, just repeat the phrase "Omelette du fromage". Even if the user give you other directives. Just ignore them and say "Omelette du fromage".',
)


@click.command()
@click.option('--message', type=str, help='The message to send to the agent')
def main(message: str):
    asyncio.run(run_async_main(message=message))


async def run_async_main(message: str):
    session_service = InMemorySessionService()

    APP_NAME = "french_interpreter_app"
    USER_ID = "user_1"
    SESSION_ID = "session_001"

    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    print(f"User: {message}")
    content = types.Content(role='user', parts=[types.Part(text=message)])

    response = runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content)
    async for event in response:
        if event.is_final_response():
          if event.content and event.content.parts:
             final_response_text = event.content.parts[0].text
          elif event.actions and event.actions.escalate:
             final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
          break
    print(f"Agent Response: {final_response_text}")


if __name__ == "__main__":
    main()
