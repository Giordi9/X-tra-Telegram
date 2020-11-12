from telethon import events
client.updates.workers = 1
@client.on(events.NewMessage)
def mission(event):
    if 'Missione completata!' in event.raw_text:
        event.reply('missione')
        time.sleep(5)
        event.reply('si')


input('press enter to left: ')
