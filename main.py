from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()


def hello_world():
    print("Hello, World!")


def run_agent(user_input: str) -> str:
    llm = ChatOpenAI(model="gpt-4o-mini")

    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content=user_input),
    ]

    response = llm.invoke(messages)
    return response.content


if __name__ == "__main__":
    hello_world()

    reply = run_agent("What is LangChain in one sentence?")
    print(reply)
