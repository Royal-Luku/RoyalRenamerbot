import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit , usertype,addpre
ADMIN = int(os.environ.get("ADMIN", 5151412494))
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["warn"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("User Notfied Sucessfully")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("User Not Notfied Sucessfully 😔") 


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["active"]))
async def buypremium(bot, message):
	await message.reply_text("Select Plan.........",quote=True,reply_markup=InlineKeyboardMarkup([
                         [       
                                 InlineKeyboardButton("Plan 1", callback_data="vip1")
				   ], [
					InlineKeyboardButton("Plan 2", callback_data="vip2")
				   ], [
					InlineKeyboardButton("Plan 3", callback_data="vip3")
				   ], [
        			InlineKeyboardButton("Plan 4",callback_data = "vip4") ]]))
        			

@Client.on_callback_query(filters.regex('vip1'))
async def vip(bot,update):
	id = update.message.reply_to_message.text.split("/active")
	user_id = id[1].replace(" ", "")
	inlimit  = 10737418240
	uploadlimit(int(user_id),10737418240)
	usertype(int(user_id),"PLAN 1")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Users")
	await bot.send_message(user_id,"Hey, Your Premium Plan Has Been Active Chek Plan /plan")

@Client.on_callback_query(filters.regex('vip2'))
async def vip(bot,update):
	id = update.message.reply_to_message.text.split("/active")
	user_id = id[1].replace(" ", "")
	inlimit  = 21474836480
	uploadlimit(int(user_id),21474836480)
	usertype(int(user_id),"PLAN 2")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Users")
	await bot.send_message(user_id,"Hey, Your Premium Plan Has Been Active Chek Plan /plan")

@Client.on_callback_query(filters.regex('vip3'))
async def vip(bot,update):
	id = update.message.reply_to_message.text.split("/active")
	user_id = id[1].replace(" ", "")
	inlimit  = 53687091200
	uploadlimit(int(user_id),53687091200)
	usertype(int(user_id),"PLAN 3")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Users")
	await bot.send_message(user_id,"Hey, Your Premium Plan Has Been Active Chek Plan /plan")

@Client.on_callback_query(filters.regex('vip4'))
async def vip(bot,update):
	id = update.message.reply_to_message.text.split("/active")
	user_id = id[1].replace(" ", "")
	inlimit  = 107374182400
	uploadlimit(int(user_id),107374182400)
	usertype(int(user_id),"PLAN 4")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Users")
	await bot.send_message(user_id,"Hey, Your Premium Plan Has Been Active Chek Plan /plan")

