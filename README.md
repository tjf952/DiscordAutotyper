
# Discord AutoTyper [Python]
A python script to auto send commands in Discord or any other program.
<br>
<img alt="Python3" src="https://img.shields.io/badge/-Python3-3776AB?style=flat-square&logo=Python&logoColor=white" />
>DISCLAIMER
**Use at your own risk!** I am not responsible if you get banned for spamming or using autotype. I do not take responsibility for how you use this program nor do I recommend you use it in any way that may infringe on any software / buisness.
This program is not endorsed or affiliated with Discord or any bot for Discord. Usage of this application may also cause a violation of the agreed Terms of Service between you and Discord or a bot.

# Features
- #### Start / Stop via hotkey
- #### Supports sending one time commands via hotkey
- #### Supports individually timed commands
- #### Supports ratelimit for sending messages in Discord
- #### Supports auto stop after certain time
- #### Supports randomly skipping commands to avoid blacklisting and ban


# Installation
Download the repo as a zip and extract it to a folder. Open a command prompt in that folder and and then run the command `pip install -r requirements.txt`  (needs Python3 and pip).

# Usage
- Rename the file `settings-example.json` to `settings.json`.
- Edit the `settings.json` as per your need (read settings.json section below)
- Open a command prompt in the folder and run `python autotyper.py` or simply run the file `run.cmd` (Windows)
  .If you have python3 installed separately run `python3 autotyper.py`
- Now either go to the discord web app or desktop app and click on the textbox
- Finally press the hotkey to start the autotyping



## settings.json
This is the configuration file used by the program.

| Key          | Type    | Value                                                                                                   |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------- |
| hotkey       | string  | The `KeyCode` of the key to start and stop the autotyping. eg. `Key.f5` or `Key.f6`                     |
| exitkey      | string  | The `KeyCode` of the key used to exit the program. eg. `Key.f5` or `Key.f6`                             |
| commandDelay | float   | The delay before sending each command (used for bots which use overall ratelimiting)                    |
| showKeyCode  | boolean | Used as a helper to show the `KeyCode` of the pressed key                                               |
| randomSkip   | float   | A value from 0 to 1 indicating whether to skip a command randomly to prevent ban and blacklisting       |
| randomTime   | integer | The maximum value in seconds to choose the random delay between commands (value is added to `waittime`) |
| stopAfter    | float   | The time in minutes to stop the autotyping after. (set to `-1` for infinite autotype)                   |
| commands     | array   | An array of `command object`                                                                            |
| onetime      | object  | A JS object containing some settings. See `onetime object` below                                        |
| reader       | boolean | Used to decide whether to use below options and enable reading within main script                       |
| authorization| string  | CHANGE_ME: Represents the authorizationd code to conduct web requests from specific channels            |
| channelid    | string  | CHANGE_ME: Represents the channel on Discord to read from                                               |

### CHANGE_ME
If you want to read from specific pages, you'll have to do some extra work

1. Set reader to `true` in the settings.json
2. Change authorization code by retrieving it from Discord
    - Enter Developer Tools [Ctrl+Shift+I]
    - Go to [Network Tab]
    - Refresh page [F5] or [Ctrl+R]
    - Find message that says 'messages?limit=50'
    - Scroll through 'Request Headers' and look for 'authorization' key i.e. 'authorization: KEY'
    - Copy KEY into authorization in the settings.json
3. Change channel_id value by retrieving it from Discord
    - Enter Developer Tools [Ctrl+Shift+I]
    - Go to [Network Tab]
    - Enter a message into the channel you want to read from
    - Find message that says 'messages' (should be the most recent one)
    - It should be in the Request URL i.e. 'https://discord.com/api/v9/channels/CHANNEL_ID/messages'
    - Hint: This should be the same as the last number in the URL in your browser
    - Copy CHANNEL_ID into channelid in the settings.json

***IMPORTANT***: Do not change to a different channel after starting because it will read from the specific channel

### Command Object
Each command is a object with three keys

| Key        | Type    | Value                                                                                                                  |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------- |
| text       | string  | The command you want to send                                                                                           |
| waittime   | integer | The time in seconds to wait before sending the command                                                                 |
| randomtime | boolean | If enabled, a random delay will be added to the `waittime` so as to reduce the chance of getting banned or blacklisted |

### Onetime Object
| Key      | Type    | Value                                                                            |
| -------- | ------- | -------------------------------------------------------------------------------- |
| hotkey   | string  | The `KeyCode` of the key to start the onetime commands. eg. `Key.f7` or `Key.f8` |
| delay    | integer | The time in seconds to wait before sending each of the onetime commands          |
| commands | array   | An array of strings each containing the command text to be sent.                 |

## Examples
##### Single command
You want to send the command `pls beg` after every 45s with a random delay. You want a command to be skipped 10% of the time. The start/stop key is F5 and the exit key is F6. Then the following is the `setttings.json` file:
```json
{
    "hotkey": "Key.f5",
    "exitkey": "Key.f6",
    "showKeyCode": false,
    "commandDelay": 1,
    "showKeyCode": false,
    "randomSkip": 0.2,
    "randomTime": 60,
    "stopAfter": -1,
    "reader": false,
    "authorization": "CHANGE_ME",
    "channelid": "CHANGE_ME",
    "commands": [
        {
            "text": "pls beg",
            "waittime": 45,
            "randomtime": true
        }
    ],
    "onetime": {
        "hotkey": "Key.f8",
        "delay": 3,
        "commands": []
    }
}
```
##### Multiple commands
You want to send the command `pls beg` after every 45s with a random delay, `pls fish` after 40s with no random delay and `pls hunt` after 40s with a random delay. You don't want a command to be skipped randomly. The start/stop key is F9 and the exit key is F10. Then the following will be the `setttings.json` file:
```json
{
    "hotkey": "Key.f9",
    "exitkey": "Key.f10",
    "commandDelay": 1,
    "showKeyCode": false,
    "randomSkip": 0.2,
    "randomTime": 60,
    "stopAfter": -1,
    "reader": false,
    "authorization": "CHANGE_ME",
    "channelid": "CHANGE_ME",
    "commands": [
        {
            "text": "pls beg",
            "waittime": 45,
            "randomtime": true
        },
        {
            "text": "pls fish",
            "waittime": 40,
            "randomtime": false
        },
        {
            "text": "pls hunt",
            "waittime": 40,
            "randomtime": true
        }
    ],
    "onetime": {
        "hotkey": "Key.f8",
        "delay": 3,
        "commands": []
    }
}
```
##### Using onetime commands
You want the commands `pls sell fish all` , `pls sell deer all` and `pls sell bread all` to be sent when the `F7` key is pressed. The delay between each command is 4s.
Then the following will be the `onetime` object:
```json
{
    "key": "Key.f7",
    "delay": 4,
    "commands": [
        "pls sell fish all",
        "pls sell deer all",
        "pls sell bread all"
    ]
}
```
##### Using auto stop after
You want the autotype to automatically stop after `4hrs`. Then the following will be the `settings.json` file:
```json
{
    ...,
    ...,
    "stopAfter": 240,
    ...,
    ...
}
```

## Prevent Bans and Blacklisting
- Make a new server with a few channels and invite the bot you want to use the commands on.
- In `settings.json` make sure to set the `randomSkip` and enable `randomtime` for each command
- Pause the autotyper often and change channels

## Credit
Forked from code written by Delano Lourenco \
Repo: [discord-autotyper-python](https://github.com/3ddelano/discord-autotyper-python) \
Great solution that I wanted to build on!
