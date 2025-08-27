# Firka Polls Bot
The source code for the discord bot that automatically logs internal management polls.

## Running the bot
If you would like to run to the bot yourself *(why?)*, follow these steps:

> **1. Clone the project**
> 
> ```bash
> git clone https://github.com/QwIT-Development/poll-bot.git
> ```

> **2. cd into the project folder**
> 
> ```bash
> cd poll-bot
> ```

> **3. Add a dotenv file with your Discord bot token**
> 
> On macOS / Linux:
> ```bash
> echo "DISCORD_TOKEN=your_token_here" >> .env
> ```
> 
> On Windows (cmd):
> ```cmd
> echo DISCORD_TOKEN=your_token_here >> .env
> ```
> 
> PowerShell:
> ```powershell
> 'DISCORD_TOKEN=your_token_here' >> .env
> ```

> **4. Initialize the virtual environment**
> 
> This is easier if you use `uv`. If you're already using `uv`, just run `uv venv`.
> 
> Otherwise, run:
> ```bash
> python3 -m venv .venv
> ```

> **5. Activate the virtual environment**
> 
> ### ⚠ You can exit the virtual environment with the `deactivate` command.️
> 
> On macOS / Linux:
> ```bash
> source .venv/bin/activate
> ```
> 
> On Windows (cmd):
> ```cmd
> .venv\Scripts\activate.bat
> ```
> 
> PowerShell:
> ```powershell
> .venv\Scripts\Activate.ps1
> ```
> 
> If you see an error about execution policy, run this in an administrator PowerShell once:
> 
> ```powershell
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

> **6. Install required packages**
> 
> If you use `uv` like a gigachad:
> ```bash
> uv pip install -r pyproject.toml
> ```
> 
> Otherwise:
> ```bash
> python3 -m pip install -r pyproject.toml
> ```

> **7. Run the bot**
> ```bash
> python3 main.py
> ```

<sub>yippee ur done :D</sub>
<br/>
<sup>stuck in the virtual environment? check step 5</sup>