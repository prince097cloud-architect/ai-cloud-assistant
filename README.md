# 🤖 AI Cloud Assistant — LangChain + OpenAI + AWS

A conversational AI assistant that lets you **query your AWS resources** (EC2, Auto Scaling Groups) using natural language — powered by **LangChain**, **OpenAI**, and **Boto3**.

---

## 🚀 Features

- 🔍 Ask: “Check EC2” — and get a real-time list of running instances.
- 📊 Query ASGs with simple commands like: “List all ASG”
- 💬 Built with LangChain Agent + OpenAI Chat Model
- 🔧 Uses Python’s `boto3` to fetch live AWS data

---

## 🛠️ Tech Stack

- LangChain (Agent + Tool)
- OpenAI (GPT-4 API)
- Python 3.10+
- Boto3 for AWS
- Terminal-based input

---

## 🧪 Sample Prompts

| Prompt                        | Result                         |
|------------------------------|--------------------------------|
| `check ec2`                  | Lists all running EC2s         |
| `list asg`                   | Shows Auto Scaling Groups      |
| `check ec2 and asg`          | ❌ Only one tool executes      |
| `how many ec2 are running?` | ✅ Responds with EC2 count     |

---

## ⚠️ Known Issues

- ❌ No multi-tool execution (e.g., EC2 and ASG together)
- ❌ No memory — each session is stateless
- ⚠️ OpenAI API rate limit (Fix: Add $5 credit to your OpenAI account)

---

## ✅ Next Steps

- 🧠 Add persistent memory (Redis or file-based)
- 🛠️ Support multiple tool invocation
- 🗂️ Store outputs to a file or DB
- ☁️ Expand support: RDS, Lambda, Cost Explorer, IAM

---


---

## 📄 License

MIT License
