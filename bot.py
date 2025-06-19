import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio
import os
from dotenv import load_dotenv

# Load token from .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Made by Reverse | v.1.0"))

    for guild in bot.guilds:
        await create_roles(guild)

async def create_roles(guild):
    role_names = ["Admin", "Mod", "Staff", "Muted"]
    existing_roles = [role.name for role in guild.roles]

    for name in role_names:
        if name not in existing_roles:
            await guild.create_role(name=name)
            print(f"Created role: {name}")

    muted_role = discord.utils.get(guild.roles, name="Muted")
    for channel in guild.text_channels:
        await channel.set_permissions(muted_role, send_messages=False)

# Custom help command
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="🛠️ Moderation Bot Commands",
        description="Here are the available commands:",
        color=discord.Color.blue()
    )
    embed.add_field(name="!ban @user [reason]", value="🔨 Ban a user", inline=False)
    embed.add_field(name="!kick @user [reason]", value="👢 Kick a user", inline=False)
    embed.add_field(name="!mute @user [reason]", value="🔇 Mute a user", inline=False)
    embed.add_field(name="!unmute @user", value="🔊 Unmute a user", inline=False)
    embed.add_field(name="!clear [amount]", value="🧹 Clear messages", inline=False)
    embed.add_field(name="!reverse", value="📞 Get the support server link", inline=False)

    await ctx.send(embed=embed)

# Reverse command
@bot.command()
async def reverse(ctx):
    await ctx.send("📨 Need help? Join the support server: https://discord.gg/nitrogang")

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason"):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been **banned** 🚫 Reason: {reason}")

@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason"):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been **kicked** 👢 Reason: {reason}")

@bot.command()
@has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason="No reason"):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f"{member.mention} has been **muted** 🔇 Reason: {reason}")

@bot.command()
@has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    await ctx.send(f"{member.mention} has been **unmuted** 🔊")

@bot.command()
@has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"🧹 Deleted {amount} messages.", delete_after=3)

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"⚠️ Error: {str(error)}")

bot.run(TOKEN)
