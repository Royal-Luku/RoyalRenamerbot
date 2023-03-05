"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	No 4gb Support
	
	**Plan 1 📝** -: __Daily Upload Limited 10GB
40rs Per Month With 4GB Support__

	**Plan 2 📝** -: __Daily Upload Limited 20GB
100rs Per Month With 4GB Support__

       **Plan 3 📝** -: __Daily Upload Limited 50GB
160rs Per Month With 4GB Support__

       **Plan 4 📝** -: __Daily Upload Limited Unlimited
250rs Per Month With 4GB Support__
	
	Pay Using Upi Id ```adityakar052@paytm```
	
	After Payment Done Send Screenshots To Admin!"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Admin",url = "https://t.me/royaldwip")], 
        			[InlineKeyboardButton("Chek Plan",callback_data = "plan")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	No 4gb Support
	
	**Plan 1 📝** -: __Daily Upload Limited 10GB
40rs Per Month With 4GB Support__

	**Plan 2 📝** -: __Daily Upload Limited 20GB
100rs Per Month With 4GB Support__

       **Plan 3 📝** -: __Daily Upload Limited 50GB
160rs Per Month With 4GB Support__

       **Plan 4 📝** -: __Daily Upload Limited Unlimited
250rs Per Month With 4GB Support__
	
	Pay Using Upi Id ```adityakar052@paytm```
	
	After Payment Done Send Screenshots To Admin!"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN",url = "https://t.me/OTT_Zone_Admin")],
        			[InlineKeyboardButton("chek Plan",callback_data = "plan")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
