from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain_core.output_parsers import JsonOutputParser

llm = ChatGroq(model="qwen/qwen3.8-27b" , temperature=1)

prompt = ChatPromptTemplate.from_template(
"""Generate {count} user records 
"""
)

chain =  prompt | llm | StrOutputParser()
users = chain.invoke({"count": 5})

print(users)

#  """You are a test data generator.
#  Generate {count} realistic user records for an indian commerce app.

#  Rules:
#  -Fields:name, email,phone,city,age
#  -Email must match the persons name.
#  -Phone number a 10 digit indian mobile number.
#  -Inclde 1 invalid recond(e.g bad email or age below 18) and add a field "is_valid": false for it; use true for the others.

#  Return ONLY a JSON list. NO extra text.
# """

#Test Data with Few shot
# "Generate {count} rows of test data for this table as a valid JSON list. "
# "Do not include any markdown formatting, explanations, or backticks. "
# "Output ONLY the raw JSON array.\n\n"
# "Example format:\n"
# "[{{\"id\": 1, \"name\": \"Anita Rao\", \"email\": \"anita.rao@example.com\", \"age\": 29, \"city\": \"pune\"}}]"


#For Schema drive test data generation(json)
#     """Generate {count} rows of test data for this table as json
# CREATE TABLE users( id INT PRIMARY KEY ,name VARCHAR(50) not null ,email VARCHAR(100),age int check(age>=18) ,city varchar(30);
# Rules: unique ids and emails , realistic indian names and cities, include one row that violates a constraint (age < 18)
# """

#For Schema drive test data generation(insert queries)
# """Generate {count} rows of test data for this table as insert queries
#     CREATE TABLE users( id INT PRIMARY KEY ,name VARCHAR(50) not null ,email VARCHAR(100),age int check(age>=18) ,city varchar(30);
#     Rules: unique ids and emails , realistic indian names and cities, include one row that violates a constraint (age < 18)
# """