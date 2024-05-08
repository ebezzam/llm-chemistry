from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# documents = SimpleDirectoryReader("data").load_data()
# index = VectorStoreIndex.from_documents(documents)
# query_engine = index.as_query_engine()
# response = query_engine.query("What did the author do growing up?")
# print(response)

documents = SimpleDirectoryReader("papers").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

questions = [
    "What is the title of the paper?",
    "What peptides are mentioned in the paper?",
]

"""
Question: What is the title of the paper?
Answer: The title of the paper is "CycPeptMPDB: A Comprehensive Database of Membrane Permeability of Cyclic Peptides".

Question: What peptides are mentioned in the paper?
Answer: Circle and Lariat peptides are mentioned in the paper.
"""

for question in questions:
    print("\nQuestion:", question)
    response = query_engine.query(question)
    print("Answer:", response)
