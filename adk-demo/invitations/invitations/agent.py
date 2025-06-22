from pydantic import BaseModel, Field
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools.agent_tool import AgentTool

class Event(BaseModel):
    name: str = Field(description="The name of the event")
    date: str = Field(description="The date of the event")
    time: str = Field(description="The time of the event")
    location: str = Field(description="The location of the event")

class Invitation(BaseModel):
    invitation_raw: str = Field(description="The raw text of the invitation")
    invitation_score: int = Field(description="The score of the invitation from 0 to 10")

parser = Agent(
    model='gemini-2.5-pro',
    name='parser_agent',
    description='A helpful assistant for parsing user messages about events.',
    output_schema=Event,
    instruction='You are text parser agent. More specifically you receive a user message about an event, and you task is to parse it and fetch the name, date, time, location of the event.',
)

composer = Agent(
    model='gemini-2.5-pro',
    name='composer_agent',
    description='A helpful assistant for composing invitation to events.',
    input_schema=Event,
    output_key='invitation_raw',
    instruction='You are a text composer agent. More specifically you receive an event and you task is to compose an invitation to the event with the appropriate wording.',
)

checker = Agent(
    model='gemini-2.5-pro',
    name='checker_agent',
    description='A helpful assistant for checking the invitation.',
    instruction='You are a text checker agent. More specifically you receive an invitation raw text and you task is to score it from 0 to 10 based on the quality of the invitation. The score should be based on the wording, clarity, and overall quality of the invitation.',
    output_schema=Invitation,
    output_key='invitation'
)

invitations_agent = SequentialAgent(
    name='invitations_agent',
    description='An agent for parsing user messages about events, composing invitations, and checking the quality of the invitations.',
    sub_agents=[parser, composer, checker],
)

root_agent = Agent(
    model='gemini-2.5-pro',
    name='invitations_root_agent',
    description='A root agent for handling invitations.',
    instruction='You are a root agent for composing event invitations. you will greet the user, explain your purpose, and ask for the event details such as name, time, place. AFter the event details are provided use the workflow_agent to compose an invitation and score it. If the event details were already provided, don\'t ask for them again instead just proceed with the workflow_agent. If there are no event details provided, ask the user for them repeatedly. Once the workflow has been executed, return the invitation and its score to the user.',
    tools=[AgentTool(agent=invitations_agent)],
)