from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.output_parsers import OutputFixingParser
from typing import Optional
from pydantic import Field,BaseModel
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
base_url=os.getenv("BASE_URL")
model=os.getenv("MODEL")

class Contact(BaseModel):
    name: str = Field(description="The name of the person")
    phno: int = Field(description="The Phone Number of the person")
    age: Optional[int] = Field(description="A person's age", default=None)
    address: Optional[str]= Field(description="A person's address", default=None)
    hobbies: Optional[list[str]]= Field(description="The person's hobbies or what they do as leisure activities.", default=None)

pydanticparser=PydanticOutputParser(pydantic_object=Contact)
while True:
    print("Enter all your details please, ensure you enter Phone number.")
    i=input()
    prompt=ChatPromptTemplate([('user',"""Extract the requisite details from the prompt {i}\n
                                {format_instructions}""")],partial_variables={'format_instructions':pydanticparser.get_format_instructions()},input_variables=[i])
    llm=ChatOpenAI(base_url=base_url,
                   model=model,
                   api_key=api_key)
    fixer=OutputFixingParser.from_llm(parser=pydanticparser,llm=llm)
    chain=prompt|llm|fixer
    output=chain.invoke({'i':i})
    print("The type of the file is:",type(output))
    print("The name is:",output.name)
    print("The phone number is:",output.phno)
    print("The age is:",output.age)
    print("The address is:",output.address)
    print("The hobbies are:",output.hobbies)
    
