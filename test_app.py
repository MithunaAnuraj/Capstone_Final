import streamlit as st
from dotenv import load_dotenv
from doc_processing import get_retrievertools
from tool_list import get_repl
from agent import get_agent, create_agent_chase_way
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

# Initialize tools and agent
session_state = st.session_state
if 'tools' not in session_state:
    session_state.tools = []
if 'agent' not in session_state:
    session_state.agent = None

def initialize_tools():
    if not session_state.tools:
        session_state.tools = get_repl(session_state.tools)

def initialize_agent():
    if not session_state.agent:
        initialize_tools()  # Ensure tools are initialized
        session_state.agent = create_agent_chase_way(session_state.tools)

def main():
    load_dotenv()
    st.set_page_config(page_title="Fin bot", page_icon="🤖")
    st.title("Fin bot")

    st_callback = StreamlitCallbackHandler(st.container())

    if 'files' not in session_state:
        session_state.files = []

    files = st.sidebar.file_uploader(label="Upload your pdfs here", accept_multiple_files=True, type="pdf")

    if files:
        new_files = [file for file in files if file not in session_state.files]
        if new_files:
            session_state.files.extend(new_files)
            new_tools = get_retrievertools(new_files, session_state.tools)
            if new_tools:
                session_state.tools.extend(new_tools)
                initialize_agent()  # Reinitialize agent when tools are updated

    if prompt := st.chat_input():
        st.chat_message("user").write(prompt)
        with st.chat_message("assistant"):
            initialize_agent()
            response = session_state.agent.invoke(
                {"input": prompt}, {"callbacks": [st_callback]}
            )
            st.write(response["output"].replace("$", "/$"))

if __name__ == "__main__":
    main()
