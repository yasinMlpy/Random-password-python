import random

password = "asdpuhasdpoiuahdaoihdai0sdh nN><XNCOUIN#OIR+)(#_)llp_``$($(*)@*&$)$-*/d5+4f321df3s20f.f0s5f1sd+f84f87fsd-+/f7s"
random_password = ""
for i in range(8):
    random_password += random.choice(password)
print("Your new password:", random_password)