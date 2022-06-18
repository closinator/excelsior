import discord
import os
import random
from keep_alive import keep_alive
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionEventType
from discord.ext.commands import Bot
from discord.ext import *

intents = discord.Intents().all()

bot = commands.Bot(command_prefix = "e? ", intents = intents)
client2 = commands.Bot(command_prefix = "e? ", intents = intents)


@bot.event
async def on_ready():
  print("Ready! {0.user}".format(bot))

@bot.command(name = "ban")
@commands.has_permissions(administrator = True)
async def ban(ctx, member: discord.Member, reasons = "No reason"):
  await member.ban(reason = reasons)
  await ctx.send(f"Banned the user {member}")

@bot.command(name = "unban")
@commands.has_permissions(administrator = True)
async def unban(ctx, reasons = "No reason"):
  banned_users = await ctx.guild.bans()
  mess = ctx.message.content.split(" ")

  if len(mess) == 2:
    embed = discord.Embed(title = "Invalid Syntax!", description = "The format for the `e? unban` command is this: ", color = 0xff0000)
    embed.add_field(name = "`e? unban (user to unban)`", value = "I can't just unban no one!")
    await ctx.send(embed = embed)
  
  # member_name, member_discriminator = member.split("#")
  else:
    to_unban = mess[2].split("#")
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (to_unban[0], to_unban[1]):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

        
  
@bot.command(name = "commands")
async def help(ctx):
  embed = discord.Embed(title = "Commands", description = "Excelsior is a powerful bot you can use to gamify and manage your server. ", color = 0x66ccff)
  embed.add_field(name = "Commands:", value = "`e? help` \n `e? roll` \n `e? copy` \n `e? work` \n `e? ban` \n `e? unban`")
  await ctx.send(embed = embed)

@bot.command(name = "roll")
async def roll(ctx):
  embed = discord.Embed(title = "Roll a die :game_die:", description = "This command rolls a die and gives you a random number between 1 and 6.", color = 0xff000)
  embed.add_field(name = "Your number:", value = random.randint(1, 6))
  await ctx.send(embed = embed)

@bot.command(name = "copy")
async def copy(ctx):
  list_of_words = ctx.message.content.split(" ")
  if len(list_of_words) == 2:
    embed = discord.Embed(title = "Invalid Syntax!", description = "The format for the `e? copy` is this: ", color = 0xff0000)
    embed.add_field(name = "`e? copy (what you want me to say)`", value = "I need something to copy!")
    await ctx.send(embed = embed)
  else: 
    string = ""
    for item in list_of_words[2:len(list_of_words)]:
      string += item
      string += " "
    message_sent = "\""+string+"\""
    await ctx.send(message_sent)

@bot.command(name = "work")
async def work(ctx):
  if os.path.exists(ctx.message.guild.name+".txt") == False:
    f = open(ctx.message.guild.name+".txt", "x")
    for user in ctx.guild.members:
      f.write(user.name+"#"+user.discriminator+"\t"+str(0)+"\t"+"\n")
    f.close()
    user = ctx.message.author
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    sum = num1 + num2
  
    embed = discord.Embed(title = "Work to earn coins", description = "Solve the addition problem below to earn coins! ", color = 0x0000FF)
    embed.add_field(name = str(num1)+"+"+str(num2), value = "You'll get 10 coins if you solve it. Enter your answer in the chat now! ")
    await ctx.send(embed = embed)
    def check(m):
      return m.content == m.content and m.channel == ctx.channel and m.author == user
  
    msg = await bot.wait_for("message", check = check)
    if (int(msg.content) == sum):
      f = open(ctx.message.guild.name+".txt", "r")
      tot_file = []
      for line in f:
        line_split = line.split("\t")
        if line_split[0] == str(user):
          line_split[1] = str(int(line_split[1]) + 10)
        tot_file.append(line_split)
      f.close()
      t = open(ctx.message.guild.name+".txt", "w")
      for line in tot_file:
        for i in range(len(line) - 1):
          t.write(line[i]+"\t")
          
        t.write("\n")
      await ctx.send("Good Job! The answer was {0}! You get 10 coins! ".format(sum))
    elif (int(msg.content) != sum):
      await ctx.send("You didn't get the right answer. The answer was {0}. Be better. ".format(sum))
  else:
    user = ctx.message.author
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    sum = num1 + num2
  
    embed = discord.Embed(title = "Work to earn coins", description = "Solve the addition problem below to earn coins! ", color = 0x0000FF)
    embed.add_field(name = str(num1)+"+"+str(num2), value = "You'll get 10 coins if you solve it. Enter your answer in the chat now! ")
    await ctx.send(embed = embed)
    def check(m):
      return m.content == m.content and m.channel == ctx.channel and m.author == user
  
    msg = await bot.wait_for("message", check = check)
    if (int(msg.content) == sum):
      f = open(ctx.message.guild.name+".txt", "r")
      tot_file = []
      for line in f:
        line_split = line.split("\t")
        if line_split[0] == str(user):
          line_split[1] = str(int(line_split[1]) + 10)
        tot_file.append(line_split)
      f.close()
      t = open(ctx.message.guild.name+".txt", "w")
      for line in tot_file:
        for i in range(len(line) - 1):
          t.write(line[i]+"\t")
          
        t.write("\n")
      await ctx.send("Good Job! The answer was {0}! You get 10 coins! ".format(sum))
    elif (int(msg.content) != sum):
      await ctx.send("You didn't get the right answer. The answer was {0}. Be better. ".format(sum))

@bot.command(name = "kick")
@commands.has_permissions(administrator = True)
async def kick(ctx, member: discord.Member, reason = "No reason"):
  try:
    await bot.kick(member)
    await ctx.send(f"Kicked{member}")
  except Exception:
    await ctx.send("Something went wrong")

@bot.command(name = "rich")
async def rich(ctx):
  f = open(ctx.message.guild.name+".txt", "r")
  leaderboard = {}
  for line in f:
    l = line.split("\t")
    leaderboard[l[0]] = l[1]

  leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse = True)

  value = ""
  for user in leaderboard:
    value += str(user[0]+"\t"+user[1])+" "+":dollar:"+"\n"

  embed = discord.Embed(title = "Leaderboard", description = "This is the leaderboard of users in terms of how many coins they have!  ", color = 0x00FF00)
  embed.add_field(name = "Users:", value = value)
  await ctx.send(embed = embed)


keep_alive()
bot.run(os.getenv("TOKEN"))
