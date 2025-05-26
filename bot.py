import discord
from discord.ext import commands
import asyncio

# تنظیمات
TOKEN = "MTM3Mzk0NDg3ODg3ODI5NDEyNg.GHUS-H.FEJEH_pCj2q1QL6hy7QYO1Owf5gJX6X23gdSHc"  # توکن بات را وارد کنید
GUILD_ID = 1342790823598620682  # آیدی سرور (Guild ID)
VC_CHANNEL_ID = 1374657090345500712  # آیدی کانال صوتی (Voice Channel ID)

intents = discord.Intents.default()
intents.members = True  # فعال‌سازی آنتنت‌ها برای دسترسی به اطلاعات اعضا
bot = commands.Bot(command_prefix="!", intents=intents)

# === تغییر وضعیت اکتیویتی ===
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="💢AccsesCM"),
        status=discord.Status.idle  # تنظیم وضعیت Idle
    )

    # اتصال به کانال صوتی (Voice Channel)
    guild = bot.get_guild(GUILD_ID)  # دریافت سرور از آیدی
    vc_channel = guild.get_channel(VC_CHANNEL_ID)  # دریافت کانال صوتی از آیدی

    if vc_channel and isinstance(vc_channel, discord.VoiceChannel):
        # اتصال بات به کانال صوتی
        voice_client = await vc_channel.connect()
        print(f"Joined voice channel: {vc_channel.name}")
    else:
        print("Could not find the voice channel.")

# === دستور برای ترک کانال صوتی ===
@bot.command(name="leave")
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        print("Bot has left the voice channel.")
    else:
        await ctx.send("I'm not in a voice channel.")

# اجرای بات
bot.run(TOKEN)