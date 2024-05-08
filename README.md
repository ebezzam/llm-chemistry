```
conda create -n chem python=3.11
conda activate chem

pip install llama-index
export OPENAI_API_KEY=XXXXX

# set up example, https://docs.llamaindex.ai/en/stable/getting_started/starter_example/
mkdir data

# download text file to data folder
wget https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt -O data/paul_graham_essay.txt

# example script
python test_llamaindex.py
```
