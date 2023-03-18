# ChatGPT Line Bot

[中文](README.md) | English

[![license](https://img.shields.io/pypi/l/ansicolortags.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/TheExplainthis/ChatGPT-Tinder-Bot)](https://github.com/TheExplainthis/ChatGPT-Tinder-Bot/releases/)


## Update
- 2023/03/03 Model change to chat completion: `gpt-3.5-turbo`


## Introduction
Do you want to integrate ChatGPT into various chat platforms? This repository teaches you how to integrate it with Tinder so that you can automatically reply to messages and make new friends even when you're busy. The provided code structure only infers from past chat records, but engineers who can write code can also use users' background information, or even use image-related models to detect pictures, to enable ChatGPT to respond more appropriately.

![Demo](https://github.com/TheExplainthis/ChatGPT-Tinder-Bot/blob/main/demo/chatgpt-tinder-bot.gif)

## Installation Steps
### Token Retrieval
1. Retrieve the OpenAI API Token:
    1. Register/login to your [OpenAI](https://beta.openai.com/) account.
    2. Click on the avatar on the top right corner and select `View API keys`.
    3. Click on `Create new secret key` in the middle, and the generated token will be `OPENAI_API` (to be used later).
    - Note: Each API has a free quota and restrictions. For details, please refer to [OpenAI Pricing](https://openai.com/api/pricing/).
2. Obtain the Tinder Token:
    1. Log in to [Tinder](https://tinder.com/).
    2. Right-click -> `Inspect` -> `Network` -> Select any Request -> Look for `x-auth-token` in the Request.


### Project Setup
1. Fork the Github project:
    1. Register/login to [GitHub](https://github.com/).
    2. Go to [ChatGPT-Tinder-Bot](https://github.com/TheExplainthis/ChatGPT-Tinder-Bot).
    3. Click `Star` to support the developer.
    4. Click `Fork` to copy all the code to your own repository.
2. Deploy (free space):
    1. Go to [replit](https://replit.com/).
    2. Click `Sign Up` and log in with your `Github` account and authorize it -> click `Skip` to skip the initialization settings.
    3. On the main page in the middle, click `Create` -> a pop-up window will appear, click `Import from Github` on the upper right corner.
    4. If you have not added the Github repository, click the link `Connect GitHub to import your private repos.` -> check `Only select repositories` -> select `ChatGPT-Tinder-Bot`.
    5. Go back to step 4. At this point, the `Github URL` can select the `ChatGPT-Tinder-Bot` project -> click `Import from Github`.

### Project Execution
1. Environment variables setting:
    1. After completing the previous step of `Import`, click on `Tools` at the bottom left of the project management page in `Replit`, then click on `Secrets`.
    2. Click on `Got it` on the right side to add environment variables, which includes:
        1. OpenAI API Token:
            - key: `OPENAI_API`
            - value: `[obtained from step one]`
        2. Desired model:
            - key: `OPENAI_MODEL_ENGINE`
            - value: `gpt-3.5-turbo`
        3. ChatGPT wants the assistant to play the role of a keyword (currently, no further usage instructions have been officially released, and players can test it themselves).
            - key: `SYSTEM_MESSAGE`
            - value: `You are a helpful assistant.`
        4. Tinder Token:
            - key: `TINDER_TOKEN`
            - value: `[obtained from step one]`
2. Start running:
    1. Click on `Run` on the top.
    2. After successful, the right-side screen will display `{"message": "Hello World"}`, and the **URL** on the top of the screen should be copied down.
    - Note: if there is no request within an hour, the program will be interrupted, so the following steps are needed.
3. CronJob scheduled request sending:
    1. Register/Login to [cron-job.org](https://cron-job.org/en/)
    2. In the upper right corner of the panel, select `CREATE CRONJOB`
    3. Enter `ChatGPT-Tinder-Bot` in the Title field, and enter the URL from the previous step, for example: `https://ChatGPT-Tinder-Bot.explainthis.repl.co/`
    4. Send a request every `5 minutes` below
    5. Click on `CREATE`

## Explanation
- When does the bot reply?
    - The bot scans every five minutes and skips if there is no reply from the other party. If there is still no reply after one day, the bot will leave another message.
- How can I customize the settings?
    - In `main.py`, line 27 `scheduled_job` can be adjusted to change how often the bot replies.
    - In `main.py`, line 34 `for` can be adjusted to change how many conversations the bot responds to.
    - In `main.py`, line 47 `if` can be adjusted to change the conditions for when the bot responds to messages.
- How can I add more information?
    - In `/src/dialog.py`, there is a prefix that can be used to add information such as your preferred response style, so the bot can respond in accordance with your style.

## Support Us
Like this free project? Please consider [supporting us](https://www.buymeacoffee.com/explainthis) to keep it running.

[<a href="https://www.buymeacoffee.com/explainthis" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="45px" width="162px" alt="Buy Me A Coffee"></a>](https://www.buymeacoffee.com/explainthis)

## Related Projects
- [auto-tinder](https://github.com/joelbarmettlerUZH/auto-tinder/tree/master)
- [ChatGPT-Discord-Bot](https://github.com/TheExplainthis/ChatGPT-Discord-Bot)
- [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)

## License
[MIT](LICENSE)
