from langchain.chat_models import AzureChatOpenAI
from langchain.schema import SystemMessage
from langchain.schema import HumanMessage
from langchain.callbacks import get_openai_callback

BASE_URL = "https://servicemax-aig-project.openai.azure.com"
API_KEY = "ee8c4e7057e944c0a6773c4a04df3736"
DEPLOYMENT_NAME = "ServiceMax-AIG-Project"
model = AzureChatOpenAI(
    openai_api_base=BASE_URL,
    openai_api_version="2023-05-15",
    deployment_name=DEPLOYMENT_NAME,
    openai_api_key=API_KEY,
    openai_api_type="azure",
)

with get_openai_callback() as cb:
    model(
        [
            SystemMessage(
                content="You are a helpful assistant"
            ),
            HumanMessage(
                content="When was PTC founded ?"
            )
        ]
    )

print(f"Output: {cb}")
print(f"Total Cost (USD): ${format(cb.total_cost, '.6f')}")

