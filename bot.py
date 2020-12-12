import discord
from discord.ext import commands
TOKEN = 'Njk4NTI4OTE2Mjc2NjQxODEy.XpHJvw.p9S3qNTlfw_MST0kiIpu-DS0tmI'
bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def new_ver(ctx, arg):  # создаем асинхронную фунцию бота
    ver = arg.replace(".", "")
    await bot.get_channel(786639220910587975).send(f"Выпущена {arg}!\nandroid: https://github.com/mi6e4ka/phone-firmware-simulator/raw/{arg}/android.apkPC: https://github.com/mi6e4ka/phone-firmware-simulator/raw/{arg}/windows.zip\nЧаво нового: https://github.com/mi6e4ka/phone-firmware-simulator/blob/master/readme.md#{ver}")  # отправляем обратно аргумент

@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def news(ctx, arg):  # создаем асинхронную фунцию бота
    await bot.get_channel(786916184657362984).send("@everyone " + arg)  # отправляем обратно аргумент

@bot.command()  # разрешаем передавать агрументы
async def download(ctx):  # создаем асинхронную фунцию бота
    await ctx.send("Скачать:\nandroid: https://github.com/mi6e4ka/phone-firmware-simulator/raw/master/android.apk\nwindows: https://github.com/mi6e4ka/phone-firmware-simulator/raw/master/windows.zip")  # отправляем обратно аргумент


bot.run(TOKEN)
