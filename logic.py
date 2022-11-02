sentence = input('\n Enter the words:')
print(sentence)
discount = int(input('\n Discount value:'))
s = sentence.split()
#len(s)
for x in range(len(s)):

            if s[x][0] =='$':
              price = int(float(s[x][1:]))
              new_price = ''
              new_price+=s[x][0]
              dis = (price*discount) / 100
              apply = price - dis
              apply = "{:.2f}".format(apply)
              s[x] = new_price+apply
              #print("converted values into decimal after applying discount are:")
              print(s[x], end = ' ')

            elif s[x][0] !='$':
                #print("Not converted values into decimal after applying discount are:")
              print(s[x], end = ' ')
            else:
              continue
