from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from tools.aws_tools import list_ec2_instance, list_asg
from langchain.agents import AgentType

# Step 1: Wrap boto3 functions as LangChain tools
tools = [
    Tool(
        name="ListEC2Instances",
        func=list_ec2_instance,
        description="Use this to list all EC2 instances with their ID, type, and state."
    ),
    Tool(
        name="ListAutoScalingGroups",
        func=list_asg,
        description="Use this to list all Auto Scaling groups with desired, min, and max capacity."
    ),
]

# Step 2: Create ChatGPT agent (requires OPENAI_API_KEY env var)
llm = ChatOpenAI(temperature=0)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True
)

# Step 3: Ask your question
if __name__ == "__main__":
# Accept user input
    user_input = input("What would you like to do? (e.g., check EC2, list ASG): ")

    # Run the agent with both input and chat_history
    result = agent.invoke({
        "input": user_input,
        "chat_history": []  # required by conversational agent
    })

    print(result)
