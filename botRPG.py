import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = "!", case_insensitive = True)

@client.event
async def on_ready():
  print('O PAI TA ON')

#######################################################

@client.command()
async def eoq(ctx):
  await ctx.send('fon')

#######################################################

@client.command()
async def comandos(ctx):
  await ctx.send('!eoq')
  await ctx.send('!dado dado, quantidade, variavel')
  await ctx.send('!danos')
  await ctx.send('!(arma)')
  await ctx.send('!iniciativa3')
  await ctx.send('!iniciativa4')
  await ctx.send('!iniciativa5')
  

#######################################################

@client.command()
async def iniciativa3(ctx):
  n1 = str('Player 1')
  n2 = str('Player 2')
  n3 = str('Player 3')
  
  lista = [n1, n2, n3]
  random.shuffle(lista)
  await ctx.send('A ordem será: ')
  await ctx.send(lista)

#######################################################

@client.command()
async def iniciativa4(ctx):
  n1 = str('Player 1')
  n2 = str('Player 2')
  n3 = str('Player 3')
  n4 = str('Player 4')

  lista = [n1, n2, n3, n4]
  random.shuffle(lista)
  await ctx.send('A ordem será: ')
  await ctx.send(lista)

#######################################################

@client.command()
async def iniciativa5(ctx):
  n1 = str('Player 1')
  n2 = str('Player 2')
  n3 = str('Player 3')
  n4 = str('Player 4')
  n5 = str('Player 5')

  lista = [n1, n2, n3, n4, n5]
  random.shuffle(lista)
  await ctx.send('A ordem será: ')
  await ctx.send(lista)

#######################################################

@client.command()
async def dado(ctx, dado, quantidade, variavel):
  
  i=0
  for i in range(int(quantidade)):
    dadoRandom = random.randint(1,int(dado))
    await ctx.send(f'\n> Dado d{dado} = {dadoRandom}')
    if (int(dado) == 20):
      embed = discord.Embed()
      if(int(dadoRandom) == 1):
        embed.set_thumbnail (url = "https://i.pinimg.com/564x/0b/eb/27/0beb275e2e3ede956317405d887b538b.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 2):
        embed.set_thumbnail (url = "https://i.pinimg.com/564x/da/e2/87/dae28725a1ca2286a6a3cc6ed09a8c71.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 3):
        embed.set_thumbnail (url = "https://i.pinimg.com/564x/75/ad/91/75ad917844cd374e28b0c9dbd0f408db.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 4):
        embed.set_thumbnail (url = "https://i.pinimg.com/564x/50/31/58/5031586f1299b77f0a1ed7ee4afe6705.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 5):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/66/31/a6/6631a62fded1198516fece15ebd21f78.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 6):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/00/a8/5e/00a85e6fd9a057ad1921555da06c4733.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 7):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/22/7c/71/227c7199462a95d799e4b112d5a92ccc.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 8):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/c5/a4/c8/c5a4c88f1c6fdfbd8b935f7a418c69d7.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 9):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/85/51/e8/8551e8ed26c2b3b81d487960957d995b.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 10):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/3e/7b/79/3e7b799e344485e076f4a92df844b6e3.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 11):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/b1/2d/b4/b12db407d0a84ef74dacdbbaf36f5858.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 12):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/9c/2f/82/9c2f82762a5707177ce9798778a5d3fc.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 13):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/08/cf/b5/08cfb575d7650bc73d634c12f994214a.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 14):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/62/12/56/6212567a61fae31591ce6c90c817a19c.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 15):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/08/28/4f/08284fb3690d43e6227c368a860a8a14.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 16):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/a6/b2/51/a6b25130bff1b7692e36ea6d0fe05aca.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 17):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/16/fe/7b/16fe7bd06c2415c77ed95c84ac9074be.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 18):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/60/86/76/60867640045fd6f354e215bb3d7fbc82.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 19):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/46/ac/64/46ac6480cdeb98fcbd20cd3825cb1706.jpg")
        await ctx.send(embed = embed)

      elif(int(dadoRandom) == 20):
        embed.set_thumbnail (url = "https://i.pinimg.com/236x/21/61/e2/2161e2cd9d12ea21faed8c8c7cfb33c5.jpg")
        await ctx.send(embed = embed)

      if(int(variavel) == 1):
        if (int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif (int(dadoRandom) < 20):
          await ctx.send('\n\n>> FRACASSO\n');
        else:
          await ctx.send('\n\n>> NORMAL\n');

      elif(int(variavel) == 2):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) < 19):
          await ctx.send('\n\n>> FRACASSO\n');
        else:
          await ctx.send('\n\n>> NORMAL\n');

      elif(int(variavel) == 3):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) < 18):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) > 17 and int(dadoRandom) < 20):
          await ctx.send('\n\n>> NORMAL\n');
        else:
          await ctx.send('\n\n>> BOM\n');

      elif(int(variavel) == 4):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) < 17):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) > 16 and int(dadoRandom) < 20):
          await ctx.send('\n\n>> NORMAL\n');
        else:
          await ctx.send('\n\n>> BOM\n');

      elif(int(variavel) == 5):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) < 16):
          await ctx.sendf('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) > 15 and int(dadoRandom) < 19):
          await ctx.send('\n\n>> NORMAL\n');
        else:
          await ctx.send('\n\n>> BOM\n');

      elif(int(variavel) == 6):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 14):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 15 and int(dadoRandom) <= 18):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 19 and int(dadoRandom) <= 19):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n')

      elif(int(variavel) == 7):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 13):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 14 and int(dadoRandom) <= 17):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 18 and int(dadoRandom) <= 19):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>>EXTREMO\n');

      elif(int(variavel) == 8):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 12):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 13 and int(dadoRandom) <= 17):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 18 and int(dadoRandom) <= 19):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n');

      elif(int(variavel) == 9):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 11):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 12 and int(dadoRandom) <= 16):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 17 and int(dadoRandom) <= 19):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n');

      elif(int(variavel) == 10):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 10):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 11 and int(dadoRandom) <= 16):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 17 and int(dadoRandom) <= 19):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n');

      elif(int(variavel) == 11):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 9):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 10 and int(dadoRandom) <= 15):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 16 and int(dadoRandom) <= 18):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n');

      elif(int(variavel) == 12):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 8):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 9 and int(dadoRandom) <= 15):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 16 and int(dadoRandom) <= 18):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n');

      elif(int(variavel) == 13):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 7):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 8 and int(dadoRandom) <= 14):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 15 and int(dadoRandom) <= 18):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n');

      elif(int(variavel) == 14):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 6):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 7 and int(dadoRandom) <= 14):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 15 and int(dadoRandom) <= 18):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n');

      elif(int(variavel) == 15):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 5):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 6 and int(dadoRandom) <= 13):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 14 and int(dadoRandom) <= 18):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n');

      elif(int(variavel) == 16):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 4):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 5 and int(dadoRandom) <= 13):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 14 and int(dadoRandom) <= 17):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n');

      elif(int(variavel) == 17):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 3):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 4 and int(dadoRandom) <= 12):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 13 and int(dadoRandom) <= 17):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n');

      elif(int(variavel) == 18):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 2):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 3 and int(dadoRandom) <= 12):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 13 and int(dadoRandom) <= 17):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n');

      elif(int(variavel) == 19):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 1):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 2 and int(dadoRandom) <= 11):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 12 and int(dadoRandom) <= 17):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n');

      elif(int(variavel) == 20):
        if(int(dadoRandom) == 1):
          await ctx.send('\n\n>> DESASTRE\n');
        elif(int(dadoRandom) <= 1):
          await ctx.send('\n\n>> FRACASSO\n');
        elif(int(dadoRandom) >= 2 and int(dadoRandom) <= 10):
          await ctx.send('\n\n>> NORMAL\n');
        elif(int(dadoRandom) >= 11 and int(dadoRandom) <= 17):
          await ctx.send('\n\n>> BOM\n');
        else:
          await ctx.send('\n\n>> EXTREMO\n');

    elif(int(dado) == 100):  
      if(int(dadoRandom) < int(variavel)):
        await ctx.send('\n\n>> FRACASSO\n')
      else:
        await ctx.send('\n\n>> SUCESSO\n')

#######################################################################

@client.command()
async def danos(ctx):
  await ctx.send('>PRIMARIA')
  await ctx.send('M4     			               2d8	       20 balas 	   2 PENTES')
  await ctx.send('DOZE	      		          3d6/4	     2 balas	 	2 PENTES')
  await ctx.send('BERETTA 	    	        2d4	        15 balas	     4 PENTES')
  await ctx.send('DESERT EAGLE 		 2d6 	        7 balas		   5 PENTES')
  await ctx.send('GLOCK			             1d4+1d3	  17 balas	   4 PENTES')
  await ctx.send('REVOLVER		          2d4	          6 balas		  4 CILINDROS')
  await ctx.send('SINALIZADOR		   2d3+Q	     2 balas(?)	 2 RESERVAS')
  await ctx.send('ARCO			               1d6	          flechas	    20 FLECHAS')
  await ctx.send('KATANA			         1d12')
  await ctx.send('-')
  await ctx.send('>SECUNDARIA')
  await ctx.send('SHURIKEN		     1d6	  		20 SHURIKEN')
  await ctx.send('ADAGA			      1d6')
  await ctx.send('FACA			          2d3')
  await ctx.send('MAOS			         1d3')
  await ctx.send('-')
  await ctx.send('>OBJETOS')
  await ctx.send('TACOS, CADEIRAS		1d3')
  await ctx.send('MACHADO			          1d4')
  await ctx.send('MARTELO			             1d4')
  await ctx.send('TRIDENTE		                 1d6')
  await ctx.send('FOICE			                    2d3')

  #################################################################

@client.command()
async def m4(ctx, quantidade):
  i=0; j=0; aux=0;
  for i in range(int(quantidade)):
    for j in range(2):
      dadoRandom = random.randint(1,8)
      aux = dadoRandom + aux
      await ctx.send(f'\n> Dano = {dadoRandom}')
  await ctx.send(f'\n>Total Dano = {aux}')

@client.command()
async def doze(ctx, dist, quantidade):
  i=0; j=0; aux=0;
  for i in range(int(quantidade)):
    if(int(dist) == 10):
      for j in range(3):
        dadoRandom = random.randint(1,6)
        aux = dadoRandom + aux
        await ctx.send(f'\n> Dano = {dadoRandom}')
    elif(int(dist) == 20):
      for j in range(3):
        dadoRandom = random.randint(1,4)
        aux = dadoRandom + aux
        await ctx.send(f'\n> Dano = {dadoRandom}')
  await ctx.send(f'\n>Total Dano = {aux}')

@client.command()
async def beretta(ctx, quantidade):
  i=0; j=0; aux=0;
  for i in range(int(quantidade)):
    for j in range(2):
      dadoRandom = random.randint(1,4)
      aux = dadoRandom + aux
      await ctx.send(f'\n> Dano = {dadoRandom}')
  await ctx.send(f'\n>Total Dano = {aux}')

@client.command()
async def eagle(ctx, quantidade):
  i=0; j=0; aux=0;
  for i in range(int(quantidade)):
    for j in range(2):
      dadoRandom = random.randint(1,6)
      aux = dadoRandom + aux
      await ctx.send(f'\n> Dano = {dadoRandom}')
  await ctx.send(f'\n>Total Dano = {aux}')

@client.command()
async def glock(ctx, quantidade):
  i=0; aux=0;
  for i in range(int(quantidade)):
      dadoRandom = random.randint(1,4)
      aux = dadoRandom + aux
      await ctx.send(f'\n> Dano = {dadoRandom}')
      dadoRandom = random.randint(1,3)
      aux = dadoRandom + aux
      await ctx.send(f'\n> Dano = {dadoRandom}')
  await ctx.send(f'\n>Total Dano = {aux}')

@client.command()
async def revolver(ctx, quantidade):
  i=0; j=0; aux=0;
  for i in range(int(quantidade)):
    for j in range(2):
      dadoRandom = random.randint(1,4)
      aux = dadoRandom + aux
      await ctx.send(f'\n> Dano = {dadoRandom}')
  await ctx.send(f'\n>Total Dano = {aux}')

@client.command()
async def sinalizador(ctx, quantidade):
  i=0; j=0; aux=0;
  for i in range(int(quantidade)):
    for j in range(2):
      dadoRandom = random.randint(1,3)
      aux = dadoRandom + aux
      await ctx.send(f'\n> Dano = {dadoRandom}')
  await ctx.send(f'\n>Total Dano = {aux}')

@client.command()
async def arco(ctx, quantidade):
  i=0; j=0; aux=0;
  for i in range(int(quantidade)):
    for j in range(1):
      dadoRandom = random.randint(1,6)
      aux = dadoRandom + aux
      await ctx.send(f'\n> Dano = {dadoRandom}')
  await ctx.send(f'\n>Total Dano = {aux}')

@client.command()
async def katana(ctx, quantidade):
  i=0; j=0; aux=0;
  for i in range(int(quantidade)):
    for j in range(1):
      dadoRandom = random.randint(1,12)
      aux = dadoRandom + aux
      await ctx.send(f'\n> Dano = {dadoRandom}')
  await ctx.send(f'\n>Total Dano = {aux}')

@client.command()
async def adaga(ctx, quantidade):
  i=0; j=0; aux=0;
  for i in range(int(quantidade)):
    for j in range(1):
      dadoRandom = random.randint(1,6)
      aux = dadoRandom + aux
      await ctx.send(f'\n> Dano = {dadoRandom}')
  await ctx.send(f'\n>Total Dano = {aux}')

@client.command()
async def faca(ctx, quantidade):
  i=0; j=0; aux=0;
  for i in range(int(quantidade)):
    for j in range(2):
      dadoRandom = random.randint(1,3)
      aux = dadoRandom + aux
      await ctx.send(f'\n> Dano = {dadoRandom}')
  await ctx.send(f'\n>Total Dano = {aux}')

@client.command()
async def maos(ctx, quantidade):
  i=0; j=0; aux=0;
  for i in range(int(quantidade)):
    for j in range(1):
      dadoRandom = random.randint(1,3)
      aux = dadoRandom + aux
      await ctx.send(f'\n> Dano = {dadoRandom}')
  await ctx.send(f'\n>Total Dano = {aux}')


client.run('') # Colocar o token do bot do discord entre as aspas.