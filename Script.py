class script(object):
    START_TXT = """๐ง๐ค๐ซ๐ฎ {},
๐ฌ๐ธ ๐ญ๐ ๐ฌ๐ค ๐จ๐ฒ <a href=https://t.me/{}>{}</a>, ๐จ ๐ ๐ฌ ๐ฆ๐ฑ๐ฎ๐ด๐ฏ ๐ฌ๐ ๐ญ๐ ๐ฆ๐ค๐ฑ ๐ก๐ฎ๐ณ ๐ข๐ฑ๐ค๐ ๐ณ๐ค๐ฃ ๐ฅ๐ฎ๐ฑ ๐ฌ๐ ๐ซ๐ซ๐ด ๐ฌ๐ฎ๐ต๐จ๐ค ๐ฒ๐ค๐ ๐ฑ๐ข๐ง , ๐ฎ๐ญ๐จ๐ธ ๐ ๐ด๐ณ๐ง๐ฎ๐ฑ๐จ๐ฒ๐ค๐ฃ ๐ ๐ฃ๐ฌ๐จ๐ญ๐ฒ ๐ข๐ ๐ญ ๐ ๐ข๐ข๐ค๐ฒ๐ฒ

๐ฃ๐ฎ๐ญ ๐ณ ๐ถ๐ ๐ฒ๐ณ๐ค ๐ธ๐ฎ๐ด๐ฑ ๐ณ๐จ๐ฌ๐ค๐"""
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """โฎ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด: {}
โฎ ๐ฒ๐๐ด๐ฐ๐๐พ๐: <a href=https://t.me/BKC0001>๐ฐ๐ฐ๐ณ๐ท๐ธ</a>
โฎ ๐ป๐ธ๐ฑ๐๐ฐ๐๐: ๐ฟ๐๐๐พ๐ถ๐๐ฐ๐ผ
โฎ ๐ป๐ฐ๐ฝ๐ถ๐๐ฐ๐ถ๐ด: ๐ฟ๐๐๐ท๐พ๐ฝ ๐น
โฎ ๐ณ๐ฐ๐๐ฐ ๐ฑ๐ฐ๐๐ด: ๐ผ๐พ๐ฝ๐ถ๐พ ๐ณ๐ฑ
โฎ ๐ฑ๐พ๐ ๐๐ด๐๐๐ด๐: ๐ท๐ด๐๐พ๐บ๐
โฎ ๐ฑ๐๐ธ๐ป๐ณ ๐๐๐ฐ๐๐๐: v1.0.2 [ ๐ฑ๐ด๐๐ฐ ]"""
    SOURCE_TXT = """<b>Donation</b>

โชผ <b>๐๐จ๐ฎ ๐๐๐ง ๐๐จ๐ง๐๐ญ๐ ๐๐ง๐ฒ ๐๐ฆ๐จ๐ฎ๐ง๐ญ ๐๐จ๐ฎ ๐๐๐ฏ๐ ๐ณ. 

<b>โโโโโโโโโแ Payment Methods แโโโโโโโโโ

โฎ ๐๐ผ๐ผ๐ด๐น๐ฒ๐ฃ๐ฎ๐
โฎ ๐ฃ๐ฎ๐๐๐บ
โฎ ๐ฃ๐ต๐ผ๐ป๐ฒ๐ฃ๐ฒ
โฎ ๐ฃ๐ฎ๐๐ฃ๐ฎ๐น

_๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐จ๐ซ ๐๐ง๐จ๐ฐ ๐๐๐จ๐ฎ๐ญ ๐๐ก๐ ๐๐๐ฒ๐ฆ๐๐ง๐ญ ๐๐ง๐๐จ_
โโโโโโโโโโโโแ <a href=https://t.me/Aadhi011><b>๊ช๊ชแฆ๊ซแป</b></a> แโโโโโโโโโโโโ"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>  

- Filter is the feature were users can set automated replies for a particular keyword and แฉแแฉแญ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. แฉแแฉแญ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โพ /filter - <code>add a filter in chat</code>
โพ /filters - <code>list all the filters of a chat</code>
โพ /del - <code>delete a specific filter in chat</code>
โพ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- แฉแแฉแญ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. แฉแแฉแญ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/source00Devil)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โพ /connect  - <code>connect a particular chat to your PM</code>
โพ /disconnect  - <code>disconnect from a chat</code>
โพ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of แฉแแฉแญ

<b>Commands and Usage:</b>
โพ /id - <code>get id of a specifed user.</code>
โพ /info  - <code>get information about a user.</code>
โพ /imdb  - <code>get the film information from IMDb source.</code>
โพ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my OแฏแEแโก

<b>Commands and Usage:</b>
โพ /logs - <code>to get the rescent errors</code>
โพ /stats - <code>to get status of files in db.</code>
โพ /delete - <code>to delete a specific file from db.</code>
โพ /users - <code>to get list of my users and ids.</code>
โพ /chats - <code>to get list of the my chats and ids </code>
โพ /leave  - <code>to leave from a chat.</code>
โพ /disable  -  <code>do disable a chat.</code>
โพ /ban  - <code>to ban a user.</code>
โพ /unban  - <code>to unban a user.</code>
โพ /channel - <code>to get list of total connected channels</code>
โพ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โฎ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โฎ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โฎ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โฎ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โฎ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#๐๐๐ฐ๐๐ซ๐จ๐ฎ๐ฉ
โฎ ๐๐ซ๐จ๐ฎ๐ฉ โบโบ {}(<code>{}</code>)
โฎ ๐๐จ๐ญ๐๐ฅ ๐๐๐ฆ๐๐๐ซ๐ฌ โบโบ <code>{}</code>
โฎ ๐๐๐๐๐ ๐๐ฒ โบโบ {}
"""
    LOG_TEXT_P = """#๐๐๐ฐ๐๐ฌ๐๐ซ
โฎ ๐๐ โบโบ <code>{}</code>
โฎ ๐๐๐ฆ๐ โบโบ {}
"""
