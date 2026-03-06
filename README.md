# VJ Join Request Acceptor Bot

**A Advance Join Request Accept Bot Which Can Accept Both All Pending Join Request And New Join Request With Login Feature.**

**For New Join Request Use This Repo [Click Here](https://github.com/VJBots/VJ-Auto-Approval-Bot)**

## How To Deploy [Video Tutorial](https://youtu.be/2Unf-cLbJLY)

#### Environment Variables

- <b>`API_ID` : Get From [my.telegram.org](https://my.telegram.org)
- `API_HASH` : Get From [my.telegram.org](https://my.telegram.org)
- `BOT_TOKEN` : Get From [BotFather](https://telegram.me/BotFather)
- `DB_URI` : Mongodb Database Url [Tutorial Watch Here](https://youtu.be/DAHRmFdw99o)
- `ADMINS` : It mean Admin/Owner Id For Broadcasting Message.
- `LOG_CHANNEL` : Log channel id start with -100xxxxxx</b>

#### Commands To Use Bot
- <b>`/start` : check bot is alive or not, know about bot
- `/accept` : accept all pending request form channel or group.
- `/login` : login your telegram account for string session
- `/logout` : logout your telegram account 
- `/broadcast` : reply this command to your broadcast message in bot.</b>

## Update Channel [VJ Botz](https://telegram.me/vj_botz)

## Support Group [VJ Support](https://telegram.me/vj_bot_disscussion)

## Credit - [Tech VJ](https://youtube.com/@Tech_VJ)


## Deploy on Render

1. Push this repository to GitHub.
2. In Render, create a new **Web Service** from the repo.
3. Render will auto-detect `render.yaml` (or set manually):
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app & python3 bot.py`
4. Add required environment variables in Render:
   - `API_ID`
   - `API_HASH`
   - `BOT_TOKEN`
   - `DB_URI`
   - `ADMINS`
   - `LOG_CHANNEL`
   - Optional: `DB_NAME`, `NEW_REQ_MODE`

