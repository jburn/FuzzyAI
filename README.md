# FuzzyAI Fuzzer
<div style="text-align: center;">

**This repository is an archive of a modified version of FuzzyAI implemented for a diploma thesis** 

**The raw result data can be found in the results folder**

The FuzzyAI Fuzzer is a powerful tool for automated LLM fuzzing. It is designed to help developers and security researchers identify jailbreaks and mitigate potential security vulnerabilities in their LLM APIs. 

![FZAI](resources/fuzz.gif)

## Getting Started

1. Clone the repository:
   ```bash
   git clone git@github.com:cyberark/FuzzyAI.git
   ```

2. Install dependencies using [Poetry](https://python-poetry.org/) or [PIP](https://pypi.org/project/pip/) and [Python venv](https://docs.python.org/3/library/venv.html):
   ```bash
   poetry install
   poetry shell  # Activate virtual environment
   ```
  or
  ```
   python -m venv venv
   ./venv/Scripts/activate
   pip install -r ./requirements.txt
   ```

3. Run the fuzzer:
   ```bash
   python run.py -h
   ```
4. Optional: Install [ollama](https://ollama.com/download/), and download a model for local usage:
   ``` # Running the command will download and install (if not) llama3.1, which is about 4.7 GB in size and is an 8B parameters model. Llama3.1 hat can be substituted with any other open-source model that is supported by ollama.
   ollama pull llama3.1
   ollama show llama3.1 # verify model installation
   ```
