import mindsdb_sdk
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

server = mindsdb_sdk.connect()
project = server.get_project("chat_bot")

my_model = project.models.get("minds_endpoint_model")

while 1:
    question = input("Prompt (Type 'quit' to quit) >> ")

    if question.lower() == "quit":
        break

    result_df = pd.DataFrame(my_model.predict({"question": question}))
    print(result_df["answer"][0])
