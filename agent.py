from langchain.globals import set_debug,set_verbose
from langchain.agents import AgentType, initialize_agent
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor




def agent_init(reper,query):

    

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

    agent = initialize_agent(
        agent=AgentType.OPENAI_FUNCTIONS,
        tools=reper,
        llm=llm,
        verbose=True,
)
    set_debug(True)
    set_verbose(True)
    #query = st.text_input(label="Enter query here")
    return (agent({"input":query}))

def get_agent(tools):
    

    llm = ChatOpenAI(temperature=0, streaming = True, model="gpt-3.5-turbo-0613")

    agent = initialize_agent(
        agent=AgentType.OPENAI_FUNCTIONS,
        tools=tools,
        llm=llm,
        verbose=True)
    # set_debug(True)
    # set_verbose(True)
    #query = st.text_input(label="Enter query here")
    return agent

    #agent({"input": "what is cost of revenue?"})

def create_agent_chase_way(tools):
    prompt = hub.pull("hwchase17/openai-functions-agent")
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, return_intermediate_steps=True)
    return agent_executor
