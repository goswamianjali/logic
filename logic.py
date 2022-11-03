def discount() -> str:
  sentence = input('\n Enter the words:')
  #print(sentence)
  discount = float(input('\n Discount value:'))
  s = sentence.split()
  for x in range(len(s)):

            if s[x][0] =='$' and s[x][1:].isnumeric():
              price = float(s[x][1:])
              new_price = ''
              new_price+=s[x][0]
              dis = (price*discount) / 100
              apply = price - dis
              s[x] = "${:.2f}".format(apply)
              #s[x] = new_price+apply
              #print("converted values into decimal after applying discount are:")
              print(s[x], end = ' ')

            elif s[x][0] !='$' or not s[x][1:].isdigit():
                #print("Not converted values into decimal after applying discount are:")


              print(s[x], end = ' ')
            else:
              return s
  ans = []
  return ' '.join(ans)
print(discount())

