import mindsdb_sdk
import pandas as pd

server = mindsdb_sdk.connect()
project = server.get_project("essay_craft")

essay_analyser = project.models.get("essay_analyser")
essay_helper = project.models.get("essay_helper")

def analyse(essay):
    result_df = pd.DataFrame(essay_analyser.predict({"essay": essay}))
    return (result_df["result"][0])

def generate_roadmap(topic):
    result_df = pd.DataFrame(essay_helper.predict({"topic": topic}))
    return (result_df["result"][0])
