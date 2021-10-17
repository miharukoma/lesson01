t = float(input("何時ですか"))
if t >= 24:
  t=t-24
  if t >= 24:
    l=t%24
    t=24-l
print("それは",t,"時です。") 