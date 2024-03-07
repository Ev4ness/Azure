
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
    dante_cmd,
)

@dante_cmd(pattern="ass$")
async def _(event):
    await event.eor("**Assalamu'alaikum Warohmatulohi Wabarokatu**")


@dante_cmd(pattern="as$")
async def _(event):
    await event.eor("**Assalamu'alaikum**")
    
@dante_cmd(pattern="ws$")
async def _(event):
    await event.eor("**Wa'alaikumussalam**")

    
@dante_cmd(pattern="ks$")
async def _(event):
    xx = await event.eor("**Hy kaa 🥹**")
    sleep(2)
    await xx.edit("**Assalamualaikum...**")


@dante_cmd(pattern="jws$")
async def _(event):
    xx = await event.eor(event, "**Astaghfirullah, Jawab dulu salam dong**")
    sleep(2)
    await xx.edit("**Assalamu'alaikum**")


@dante_cmd(pattern="3x$")
async def _(event):
    xx = await event.eor("**Bismillah, 3x**")
    sleep(2)
    await xx.edit("**Assalamu'alaikum Bisa yug Kali**")
    
@dante_cmd(pattern="kg$")
async def _(event):
    xx = await event.eor("**Nih Gw Pantun,Buah Apel Buah Kedondong**")
    sleep(2)
    await xx.edit("**Senggol Dong!!!**")

@dante_cmd(pattern="hm$")
async def _(event):
    xx = await event.eor("**Batuk dulu g sih**")
    sleep(2)
    await xx.edit("**Biar ludah batuk nya gw ludahin ke wajah lu!**")
