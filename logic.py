sentence = "\n there are $1 $2 and 5$ candies in the shop"
print(sentence)
discount = int(input('\n Discount value:'))
s = sentence.split()
#len(s)
for x in range(len(s)):
            if s[x][0] =='$':
              price = int(s[x][1:])
              new_price = ''
              new_price+=s[x][0]
              dis = (price*discount) / 100
              apply = price - dis
              apply = "{:.2f}".format(apply)
              s[x] = new_price+apply
              #print("converted values into decimal after applying discount are:")
              print(s[x])

            elif s[x][0] !='$':
                #print("Not converted values into decimal after applying discount are:")
                print(s[x])
            else:
              continue