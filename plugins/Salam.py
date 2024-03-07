
"""
Perintah Tersedia

• `{i}ass`
   Salam 

• `{i}as`
   Assalamu'alaikum

• `{i}ws`
   Jawab Salam
   
• `{i}ks`
   Kenalan 
   
• `{i}jws`
   Istighfar Salam
   
• `{i}3x`
    Bisa 

• `{i}kg`
    Keren lu

• `{i}hm`
    Batuk
"""

from time import sleep
from . import (
    eor,
    ultroid_cmd,
)

@ultroid_cmd(pattern="ass$")
async def _(event):
    await event.eor("**Assalamu'alaikum Warohmatulohi Wabarokatu**")


@ultroid_cmd(pattern="as$")
async def _(event):
    await event.eor("**Assalamu'alaikum**")
    
@ultroid_cmd(pattern="ws$")
async def _(event):
    await event.eor("**Wa'alaikumussalam**")

    
@ultroid_cmd(pattern="ks$")
async def _(event):
    xx = await event.eor("**Hy kaa 🥹**")
    sleep(2)
    await xx.edit("**Assalamualaikum...**")


@ultroid_cmd(pattern="jws$")
async def _(event):
    xx = await event.eor(event, "**Astaghfirullah, Jawab dulu salam dong**")
    sleep(2)
    await xx.edit("**Assalamu'alaikum**")


@ultroid_cmd(pattern="3x$")
async def _(event):
    xx = await event.eor("**Bismillah, 3x**")
    sleep(2)
    await xx.edit("**Assalamu'alaikum Bisa yug Kali**")
    
@ultroid_cmd(pattern="kg$")
async def _(event):
    xx = await event.eor("**Nih Gw Pantun,Buah Apel Buah Kedondong**")
    sleep(2)
    await xx.edit("**Senggol Dong!!!**")

@ultroid_cmd(pattern="hm$")
async def _(event):
    xx = await event.eor("**Batuk dulu g sih**")
    sleep(2)
    await xx.edit("**Biar ludah batuk nya gw ludahin ke wajah lu!**")
