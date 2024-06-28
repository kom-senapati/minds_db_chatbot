import mindsdb_sdk
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

server = mindsdb_sdk.connect()

# server.ml_engines.create(
#     "minds_endpoint_engine",
#     "minds_endpoint",
#     connection_data={"minds_endpoint_api_key": os.getenv("API_KEY")},
# )

# project = server.create_project('chat_bot')
project = server.get_project('chat_bot')

# my_model = project.models.create (
#     name = 'minds_endpoint_model',
#     predict = 'answer',
#     engine='minds_endpoint_engine',
#     options={
#         'prompt_template': 'Answer the question : {{question}}',
#         'model_name': 'mistral-7b'
#     }
# )

my_model = project.models.get('minds_endpoint_model')


result_df = pd.DataFrame(my_model.predict({'question': 'What is mindsdb?'}))

print(result_df['answer'][0])
