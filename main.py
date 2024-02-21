import subprocess as s

print(''' 

[1] Hidden Eye                  [2] HeJo-01

''')
i = int(input(""))
if i == 1:
    print("Hidden Eye on [+]")
    # "git clone" komutunu çalıştır
    s.run(["git", "clone", "https://github.com/darkmidus/HiddenEye"])
    s.run(["cd","HiddenEye"])
    s.run(["pip", "install", "-r", "requirements.txt"])
    s.run(["python3", "HiddenEye.py"])
