import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hi {}</b>
<i>I'm a Advanced Auto Forward Bot
I can forward all message from one channel to another channel</i>
**Click help button to know More about me**"""
  HELP_TXT = """<b><u>ð HELP</b></u>

<u>**ð Available commands:**</u>
<b>â£ __/start - check I'm alive__ 
â£ __/forward - forward messages__
â£ __/unequify - delete duplicate messages in channels__
â£ __/settings - configure your settings__
â£ __/reset - reset your settings__</b>

<b><u>ð¢ Features:</b></u>
<b>âº __Forward message from public channel to your channel without admin permission. if the channel is private need admin permission__
âº __Forward message from private channel to your channel by using userbot(user must be member in there)__
âº __custom caption__
âº __custom button__
âº __support restricted chats__
âº __skip duplicate messages__
âº __filter type of messages__
âº __skip messages based on extensions & keywords & size__</b>
"""
  
  HOW_USE_TXT = """<b><u>â ï¸ Before Forwarding:</b></u>
<b>âº __add a bot or userbot__
âº __add atleast one to channel__ `(your bot/userbot must be admin in there)`
âº __You can add chats or bots by using /settings__
âº __if the **From Channel** is private your userbot must be member in there or your bot must need admin permission in there also__
âº __Then use /forward to forward messages__</b>"""
  
  ABOUT_TXT = """
ââââââ° Òá´Êá´¡á´Êá´ Êá´á´ â±âââ±âÛªÛª
ââ­ââââââââââââââââ£
ââ£âª¼ðÊá´á´ : [Fá´Êá´¡á´Êá´ Bá´á´](https://t.me/kr_forward_bot)
ââ£âª¼ð¦CÊá´á´á´á´Ê : [ãððã à½ð«á´á´á´Æ´à½Â°â²ê®ê®Â°ã](https://t.me/tamil_kid)
ââ£âª¼ð¡Há´sá´á´á´ á´É´ : Há´Êá´á´á´
ââ£âª¼ð£ï¸Lá´É´É¢á´á´É¢á´ : PÊá´Êá´É´3
ââ£âª¼ðLÉªÊÊá´ÊÊ : PÊÊá´É¢Êá´á´ AsÊÉ´á´Éªá´ 2.0.0 
ââ£âª¼ðï¸Vá´ÊsÉªá´É´ : 0.0.0
ââ°ââââââââââââââââ£
âââââââââââââââââââââ±âÛªÛª
"""
  STATUS_TXT = """
ââââââ° Êá´á´ sá´á´á´á´s  â±âââ±âÛªÛª
ââ­ââââââââââââââââ£
ââ£âª¼**ð± Tá´á´á´Ê Usá´Ês:** `{}`
ââ
ââ£âª¼**ð¤ Tá´á´á´Ê Bá´á´:** `{}`
ââ
ââ£âª¼**ð Fá´Êá´¡á´Êá´ÉªÉ´É¢s:** `{}`
ââ
ââ°ââââââââââââââââ£
âââââââââââââââââââââ±âÛªÛª
"""
  FROM_MSG = "<b>âª SET SOURCE CHAT â«\n\nForward the last message or last message link of source chat.\n/cancel - cancel this process</b>"
  TO_MSG = "<b>âª CHOOSE TARGET CHAT â«\n\nChoose your target chat from the given buttons.\n/cancel - Cancel this process</b>"
  SKIP_MSG = "<b>âª SET MESSAGE SKIPING NUMBER â«</b>\n\n<b>Skip the message as much as you enter the number and the rest of the message will be forwarded\nDefault Skip Number =</b> <code>0</code>\n<code>eg: You enter 0 = 0 message skiped\n You enter 5 = 5 message skiped</code>\n/cancel <b>- cancel this process</b>"
  CANCEL = "<b>Process Cancelled Succefully !</b>"
  BOT_DETAILS = "<b><u>ð BOT DETAILS</b></u>\n\n<b>â£ NAME:</b> <code>{}</code>\n<b>â£ BOT ID:</b> <code>{}</code>\n<b>â£ USERNAME:</b> @{}"
  USER_DETAILS = "<b><u>ð USERBOT DETAILS</b></u>\n\n<b>â£ NAME:</b> <code>{}</code>\n<b>â£ USER ID:</b> <code>{}</code>\n<b>â£ USERNAME:</b> @{}"  
         
  TEXT = """
ââââââ° Òá´Êá´¡á´Êá´ sá´á´á´á´s  â±âââ±âÛªÛª
ââ­ââââââââââââââââ£
ââ£âª¼<b>ðµ Òá´á´Êá´á´ MsÉ¢ :</b> <code>{}</code>
ââ
ââ£âª¼<b>â sá´á´á´á´Òá´ÊÊÊ Fá´¡á´ :</b> <code>{}</code>
ââ
ââ£âª¼<b>ð¥ á´á´á´ÊÉªá´á´á´á´ MsÉ¢ :</b> <code>{}</code>
ââ
ââ£âª¼<b>ð á´á´Êá´á´á´á´ MsÉ¢ :</b> <code>{}</code>
ââ
ââ£âª¼<b>ðª Sá´Éªá´á´á´á´ MsÉ¢ :</b> <code>{}</code>
ââ
ââ£âª¼<b>ð FÉªÊá´á´Êá´á´ MsÉ¢ :</b> <code>{}</code>
ââ
ââ£âª¼<b>ð Cá´ÊÊá´É´á´ Sá´á´á´á´s:</b> <code>{}</code>
ââ
ââ£âª¼<b>ð¨  Pá´Êá´á´É´á´á´É¢á´:</b> <code>{}</code> %
ââ°ââââââââââââââââ£ 
ââââââ° {} â±ââââ±âÛªÛª
"""
  DUPLICATE_TEXT = """
ââââââ° á´É´á´Ç«á´ÉªÒÊ sá´á´á´á´s â±âââ±âÛªÛª
ââ­ââââââââââââââââ£
ââ£âª¼ <b>Òá´á´á´Êá´á´ ÒÉªÊá´s:</b> <code>{}</code>
ââ
ââ£âª¼ <b>á´á´á´ÊÉªá´á´á´á´ á´á´Êá´á´á´á´:</b> <code>{}</code> 
ââ°ââââââââââââââââ£
ââââââ° {} â±ââââ±âÛªÛª
"""
  DOUBLE_CHECK = """<b><u>DOUBLE CHECKING â ï¸</b></u>
<code>Before forwarding the messages Click the Yes button only after checking the following</code>

<b>â YOUR BOT:</b> [{botname}](t.me/{botuname})
<b>â FROM CHANNEL:</b> `{from_chat}`
<b>â TO CHANNEL:</b> `{to_chat}`
<b>â SKIP MESSAGES:</b> `{skip}`

<i>Â° [{botname}](t.me/{botuname}) must be admin in **TARGET CHAT**</i> (`{to_chat}`)
<i>Â° If the **SOURCE CHAT** is private your userbot must be member or your bot must be admin in there also</b></i>

<b>If the above is checked then the yes button can be clicked</b>"""
