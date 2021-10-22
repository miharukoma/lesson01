coin=float(input("金額を打ち込んでください")) ##coinを定義

kazu=coin//100                                ##kazuを定義、100円の枚数表記に使用
coin % 100                                    ##余数切捨
print("100円は",kazu,"枚です")
## kazu = coin - kazu*100
## coin2 = coin - kazu*100

coin2=coin-kazu*100

kazu2=coin2//10
coin2 % 10
print("10円は",kazu2,"枚です")
## coin3 = coin2 - kazu2*10

coin3=coin2-kazu2*10

kazu3=coin3//1
coin3 % 1
print("1円は",kazu3,"枚です")

## kingaku = float(input("金額入力"))
## suji100 = kingaku // 100
## suji100 % 100
## kingaku2 = kingaku - suji100*100
## suji10 = kingaku2 // 10
## suji10 % 10
## kingaku3 = kingaku2 - suji10*10
## print("100円は"suji100”枚、10円は”suji10”枚、1円は”kingaku3”枚です”)