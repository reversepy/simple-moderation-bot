# 🤖 Discord Moderation Bot – Made by Reverse

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![Made by Reverse](https://img.shields.io/badge/Made%20by-Reverse-%23ff69b4)](https://github.com/reversepy)  
[![Discord](https://img.shields.io/discord/1376577777524015105?label=Join%20Discord&logo=discord&color=5865F2)](https://discord.gg/nitrogang)  

A beginner‑friendly Discord moderation bot written in Python using discord.py.  
Auto‑creates moderation roles, provides essential mod commands, and links to your support server.  
Perfect for YouTube tutorials, personal servers, or open‑source projects.

## 🚀 Features

- ✅ Easy .env setup for secure token storage  
- ✅ Auto‑creates roles: `Admin`, `Mod`, `Staff`, `Muted`  
- ✅ Custom `!help` command with emojis  
- ✅ Commands: `!ban`, `!kick`, `!mute`, `!unmute`, `!clear`, `!reverse`  
- ✅ Shows status “Made by Reverse”  

## 📁 File Structure

```
moderation-bot/
├── bot.py              # Main bot script
├── .env.example        # Example environment file
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── LICENSE             # MIT License
```

## 🧪 Setup Instructions

1. Install dependencies:  
   pip install -r requirements.txt

2. Create/update the `.env` file with your bot token:  
   TOKEN=your-bot-token-goes-here

3. Run the bot:  
   python bot.py

## 📜 Commands

Command      | Description
-------------|-----------------------------------------------
!help        | 📘 Shows all available commands  
!ban @user   | 🔨 Bans a user from the server  
!kick @user  | 👢 Kicks a user from the server  
!mute @user  | 🔇 Mutes a user (removes chat perms)  
!unmute @user| 🔊 Unmutes a previously muted user  
!clear 10    | 🧹 Deletes 10 recent messages  
!reverse     | 📞 Sends your support server link  

## 👨‍💻 Made By Reverse

YouTube tutorial coming soon  
Need help? Join the support server: discord.gg/nitrogang

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for full details.

You can:  
- Use, modify, and distribute this bot  
- Use it in commercial or private projects  
- Remix it into something new  

Just keep the credit and don’t sue me if it breaks everything. 🧨
