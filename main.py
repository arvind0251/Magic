import asyncio
from pyrogram import Client, filters
from config import BOT_TOKEN  # Assuming your token is stored in the config.py file

app = Client("bot", bot_token=BOT_TOKEN)

# Maximum repetition limit
MAX_REPEAT_LIMIT = 500

@app.on_message(filters.command("hang"))
async def hang(client, message):
    if message.chat.type != "private":
        if message.sender_id in SUDO_USERS or message.sender_id == "admin":
            try:
                # Extracting the command arguments
                args = message.text.split(" ")

                if len(args) < 2:
                    await message.reply(f"❖ **Usage ➥** /hang <number> [emoji] [delay]")
                    return

                # Number of repetitions
                counter = int(args[1])
                if counter > MAX_REPEAT_LIMIT:
                    await message.reply(f"❖ **Max repetitions allowed is {MAX_REPEAT_LIMIT}.**")
                    return
                
                # Emoji (default is "😈")
                emoji = args[2] if len(args) > 2 else "😈"

                # Delay (default is 0.2 seconds)
                delay = float(args[3]) if len(args) > 3 else 0.2

                if delay < 0.1 or delay > 5:
                    await message.reply("❖ **Delay must be between 0.1 and 5 seconds.**")
                    return

                # Sending the repeated messages
                await message.reply(f"Starting to send {counter} {emoji} with {delay}s delay...")

                for _ in range(counter):
                    await message.reply(emoji * 50)  # Adjust the repetition of the emoji
                    await asyncio.sleep(delay)  # Custom delay
                await message.reply(f"Completed {counter} repetitions of {emoji}.")

            except (IndexError, ValueError):
                await message.reply(f"❖ **Usage ➥** /hang <number> [emoji] [delay]")
            except Exception as e:
                print(e)
                await message.reply("❖ **An error occurred while processing the command.**")
        else:
            await message.reply("You are not authorized to use this command.")
    else:
        await message.reply("This command can't be used in private messages.")

# Run the bot
app.run()
