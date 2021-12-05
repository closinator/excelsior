import discord
import os
import random
from keep_alive import keep_alive
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionEventType

client = discord.Client()

@client.event
async def on_ready():
  print("Ready! {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    pass
  
  elif message.content.startswith("e? help"): 
    embed = discord.Embed(title = "Commands", description = "Excelsior is a powerful bot you can use to gamify and manage your server. ", color = 0x66ccff)
    embed.add_field(name = "Commands:", value = "`e? help` \n `e? roll` \n `e? copy` \n `e? work`")
    await message.channel.send(embed = embed)
  
  elif message.content.startswith("e? roll"):
    embed = discord.Embed(title = "Roll a die :game_die:", description = "This command rolls a die and gives you a random number between 1 and 6.", color = 0xff000)
    embed.add_field(name = "Your number:", value = random.randint(1, 6))
    await message.channel.send(embed = embed)
  
  elif message.content.startswith("e? copy"):
    list_of_words = message.content.split(" ")
    if len(list_of_words) == 2:
      embed = discord.Embed(title = "Invalid Syntax!", description = "The format for the `e? copy` is this: ", color = 0xff0000)
      embed.add_field(name = "`e? copy (what you want me to say)`", value = "I need something to copy!")
      await message.channel.send(embed = embed)
    else: 
      string = ""
      for item in list_of_words[2:len(list_of_words)]:
        string += item
        string += " "
      message_sent = "\""+string+"\""
      await message.channel.send(message_sent)
  
  elif message.content.startswith("e? work"):
    num1 = random.randint(1, 10)
    op = ["*", "/", "+", "-"]
    num2 = random.randint(1, 10)
    equation = str(num1) + random.choice(op) + str(num2)
    corr = random.randint(1, 4)
    button = []
    for i in range(4):
      if corr == i:
        button.append(Button(label = int(eval(equation))))
      else:
        button.append(Button(label = random.randint(1, int(eval(equation) - 1))))
    mess = str(equation) + "\n" + "Click one of the buttons below. _Choose the wrong answer and you lose money!_ :sob:"
    embed = discord.Embed(title = "What is the correct answer to the problem below?", description = mess, color = 0x0000ff)
    await message.channel.send(embed = embed, components = button)
    """@client.event
    async def on_button_click(interaction):
      if interaction.component.label.startswith("ha"):
        await interaction.respond(type = InteractionEventType.ChannelMessageWithSource, content = 'clicked')
      else:
        await interaction.respond(type = InteractionEventType.ChannelMessageWithSource, content = "clicked2")"""
keep_alive()
client.run(os.getenv("TOKEN"))
