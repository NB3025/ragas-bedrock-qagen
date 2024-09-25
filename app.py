import nest_asyncio
import boto3
from langchain_community.document_loaders import PDFMinerLoader
from ragas.testset.generator import TestsetGenerator
from ragas.testset.evolutions import simple, reasoning, multi_context
from langchain_aws import ChatBedrock, BedrockEmbeddings
from config import config

# Apply nest_asyncio to avoid runtime errors
nest_asyncio.apply()

# Load PDF document
FILE_PATH = "./test.pdf"
loader = PDFMinerLoader(FILE_PATH)
documents = loader.load()

# Function to get Bedrock client
def get_bedrock_client(profile, region):
    session = boto3.Session(profile_name=profile, region_name=region)
    return session.client("bedrock-runtime")

# Initialize Bedrock client
bedrock_client = get_bedrock_client(config["profile"], config["region"])

# Set up generator and critic LLMs
generator_llm = ChatBedrock(
    model_id=config["bedrock_model_id"], 
    client=bedrock_client,
    model_kwargs={'temperature': 0}
)

critic_llm = ChatBedrock(
    model_id=config["bedrock_model_id"], 
    client=bedrock_client,
    model_kwargs={'temperature': 0}
)

# Set up embeddings
embeddings = BedrockEmbeddings(
    client=bedrock_client,
    model_id=config["bedrock_embedding_model_id"]
)

# Initialize TestsetGenerator
generator = TestsetGenerator.from_langchain(
    generator_llm,
    critic_llm,
    embeddings
)

# Define distribution of question types
distributions = {
    simple: 0.5,
    multi_context: 0.25,
    reasoning: 0.25
}

# Generate test set
testset = generator.generate_with_langchain_docs(
    documents=documents, 
    test_size=10, 
    distributions=distributions
)

# Convert test set to pandas DataFrame
test_df = testset.to_pandas()

# Print the first 5 rows of the DataFrame
print(test_df.head())

# Save DataFrame to CSV
test_df.to_csv("ragas_synthetic_dataset.csv", index=False)