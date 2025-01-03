# Prompt Engineer Agent

## Overview
This project is an **AI-powered Prompt Engineering Tool** designed to automatically enhance and optimize prompts for large language models (LLMs). Using advanced prompt engineering principles and OpenAI's GPT-4, the tool transforms basic prompts into comprehensive, well-structured instructions that yield better results.

## Key Features
- **Automated Prompt Enhancement:** Transforms basic prompts into detailed, optimized versions
- **Multi-step Analysis:** Analyzes input, expands instructions, decomposes tasks, and adds reasoning
- **OpenAI Integration:** Leverages GPT-4o for intelligent prompt engineering
- **Gradio Interface:** Provides an intuitive web interface for easy interaction
- **Evaluation System:** Includes built-in criteria for assessing prompt quality
- **Reference Suggestions:** Recommends relevant sources to enhance prompt effectiveness

## Repo Structure

```
├── .gitignore                # Files and directories to be ignored by Git
├── LICENSE                   # License information for the project
├── README.md                # Project documentation (this file)
├── agent.py                 # Core prompt engineering logic
├── app.py                   # Gradio web interface implementation
└── requirements.txt         # Python dependencies
```

## How It Works

The tool enhances prompts through several steps:
1. **Input Analysis:** Determines key information and requirements
2. **Instruction Expansion:** Adds clarity and detail to basic prompts
3. **Task Decomposition:** Breaks down complex tasks into manageable subtasks
4. **Reasoning Addition:** Incorporates chain-of-thought and self-review instructions
5. **Reference Integration:** Suggests relevant sources and explains their use
6. **Quality Evaluation:** Assesses and adjusts the final prompt based on specific criteria

## Getting Started

### Prerequisites
- Python 3.8+
- OpenAI API key

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/justmalhar/prompt-engineer.git
   cd prompt-engineer-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key in the Gradio UI:
   - Create a .env file in the project root
   - Add your API key: `OPENAI_API_KEY=your-api-key`

### Usage
Run the Gradio interface:
```bash
python app.py
```

The web interface will be available at http://localhost:7860 or generated Gradio.live URL

## Features in Detail

### Prompt Analysis
- Identifies main topics and requirements
- Determines optimal output format
- Suggests enhancement strategies

### Instruction Enhancement
- Adds relevant details and clarifications
- Suggests appropriate AI personas
- Includes guiding examples
- Optimizes output length

### Task Management
- Breaks down complex prompts into subtasks
- Creates specific instructions per subtask
- Defines success criteria

### Quality Control
- Implements self-review mechanisms
- Includes evaluation criteria
- Performs automatic adjustments

## Dependencies
- gradio
- openai
- python-dotenv
- fastapi
- uvicorn
- And more (see requirements.txt)

## Credits
This project is inspired by and adapted from [Advanced-Prompt-Generator](https://github.com/Thunderhead-exe/Advanced-Prompt-Generator) by Thunderhead-exe.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Stay Connected
- **Twitter/X**: [@justmalhar](https://twitter.com/justmalhar) 🛠
- **LinkedIn**: [Malhar Ujawane](https://linkedin.com/in/justmalhar) 💻

Made with ❤️ and AI by [@justmalhar](https://twitter.com/justmalhar)
