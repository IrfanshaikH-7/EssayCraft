import mindsdb_sdk
import os
from dotenv import load_dotenv

load_dotenv()

server = mindsdb_sdk.connect()

server.ml_engines.create(
    "minds_endpoint_engine",
    "minds_endpoint",
    connection_data={"minds_endpoint_api_key": os.getenv("API_KEY")},
)

project = server.create_project("essay_craft")
project = server.get_project("essay_craft")

project.models.create(
    name="essay_analyser",
    predict="result",
    engine="minds_endpoint_engine",
    options={
        "prompt_template": "Study the given essay. Give it a score out of 10. And tell in what areas it can be improved. Give good motivating feedback. Essay - {{essay}}. Give output as formatted html inside a div tag.",
        "model_name": "mistral-7b",
        "max_tokens": 800
    },
)

project.models.create(
    name="essay_helper",
    predict="result",
    engine="minds_endpoint_engine",
    options={
        "prompt_template": "Generate a roadmap of the essay (sub topics on which we need to write) topic is {{topic}}. Give output as formatted html inside a div tag.",
        "model_name": "mistral-7b",
        "max_tokens": 800
    },
)
