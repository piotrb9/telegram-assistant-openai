# Telegram Assistant

Your personal AI assistant acts like a casual Telegram user. It can do tasks like any Telegram member such as:
- joining a channel/group
- leaving a channel/group
- sending a message to a user
- commenting on channel posts
- checking if it is a member of a channel/group
- showing a conversation history with a user/from a group or channel

It also works with a simple database where it saves the data about the joined groups, channels/groups currently following and their messages.
The bot writes the SQL query on its own, so it can do ANY task related to the database (like dropping the table)!

## Preview
![image](https://github.com/piotrb9/telegram-assistant-openai/assets/157641773/4a2c3bba-741a-4a88-b24a-1b89c7a7fe9e)
![image](https://github.com/piotrb9/telegram-assistant-openai/assets/157641773/e5897032-f775-4836-95e7-f3cef13fa7b5)
![image](https://github.com/piotrb9/telegram-assistant-openai/assets/157641773/154c9903-674c-4a31-b1be-d0460f3d5d4d)
![image](https://github.com/piotrb9/telegram-assistant-openai/assets/157641773/6deec25d-4797-4dcc-9d85-7604e4665964)
![image](https://github.com/piotrb9/telegram-assistant-openai/assets/157641773/a41b199c-d314-4d34-83e9-3a628ef83b64)
![comment](https://github.com/piotrb9/telegram-assistant-openai/assets/157641773/52d183f0-2c89-48b4-bf70-b143d57497b1)


## Installation

Install the requirements
```bash
pip install -r requirements.txt
```

Download the repo on your local machine

Run the create_db.py file in the tools dir to initialize the database
```python
python tools/create_db.py
```

Rename the config_template.ini to config.ini and fill it with your data (do not include the [] brackets!)
```
IP = [Proxy IP]
PORT = [Proxy Port]
USERNAME = [Proxy Username]
PASSWORD = [Proxy Password]

Name of the session file, ie. '123456789.session'
SESSION_FILE = [Session Filename]

[Tutorial](https://docs.telethon.dev/en/stable/basic/signing-in.html)
API_ID = [Your Telegram API ID]
API_HASH = [Your Telegram API Hash]

[Tutorial](https://openai.com/blog/openai-api)
OPENAI_API_KEY = [Your OpenAI API Key]

[Get it here](https://platform.openai.com/assistants)
ASSISTANT_ID = [Assistant Identifier]
THREAD_ID = [Thread Identifier]

Username of the group where you will be sending the commands, ie. 'randomtelegramgroup3853'
SERVICE_GROUP = [Service Group]
```

Paste .session file in the /sessions/ directory [What are session files and how to get them](https://docs.telethon.dev/en/stable/concepts/sessions.html).<br />
I advice you to use the phone number as the file name (without the '+' but including the country code, like 123456789.session)

## Usage
Create a service group with the username given in the config file. The bot will join it automatically if its public.

Run the run_bot.py file
```python
python run_bot.py
```

Send commands to the bot and it will automatically respond. Do not exceed OpenAI API rate limits.

If the bot crashes, sometimes you have to restart the OpenAI thread. You can use the /tools/cancel_openai_run.py to do it. It will clean the waiting commands.
```python
python tools/cancel_openai_run.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

Made with the OpenAI API

**DISCLAIMER** For educational purposes only. I do not take responsibility for illegal use of the script, like sending spam or abusing the Telegram TOS!
