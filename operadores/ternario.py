#!Python3
lockdown = False
grana = 130

status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu'

print(f'o status é :{status}')