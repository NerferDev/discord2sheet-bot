# BSD 3-Clause License
# Copyright (c) 2019, Hugonun(https://github.com/hugonun)
# All rights reserved.

import discord

from gsheet import *

client = discord.Client()
sheet = gsheet()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Command to insert data to excel
    if message.content.startswith('!s '):
        SPREADSHEET_ID = '1rCbJRTM0SGWyX62PyxnS3MGSv4gytVPYLGSB6dOo1hE' # Add ID here
        RANGE_NAME = 'A1'
        FIELDS = 2 # Amount of fields/cells

        # Code
        msg = message.content[3:]
        result = [x.strip() for x in msg.split(',')]
        if len(result) == FIELDS:
            # Add
            print(message.created_at)
            DATA = [message.author.name] + [message.author.id] + [str(message.created_at)] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            await message.channel.send('Your data has been successfully submitted!')
        else:
            # Needs more/less fields
            await message.channel.send('Error: You need to add {0} fields, meaning it can only have {1} comma.'.format(FIELDS,FIELDS-1))
    
    # Whois
    # Please dont remove the copyright and github repo
    elif len(message.mentions) > 0:
        for muser in message.mentions:
            if muser.id == client.user.id:
                if any(word in message.content for word in ['whois','who is','Help','help','info']):
                    await message.channel.send('This bot was made by hugonun(https://github.com/hugonun/).\nSource code: https://github.com/hugonun/discord2sheet-bot')


client.run('NTQwMzIzOTMyNTkxNjIwMTE2.XSuy1w.EQPXfNVpKgDDIXl-FIWMxrnF1EI') # Add bot token here
