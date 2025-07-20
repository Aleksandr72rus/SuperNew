# 1 var
st = "I am learning Python. hello, WORLD!"
tmp = st[st.find('h'):st.rfind('h')]
result = st[:st.find('h')] + tmp[::-1] + st[st.rfind('h') + 1:]
print("Строчка: ", st)
print("Результат:", result)

# 2 var
# st = input("Введите строку: ")
# tmp = st[st.find('h'):st.rfind('h')]
# result = st[:st.find('h')] + tmp[::-1] + st[st.rfind('h') + 1:]
# print("Строчка: ", st)
# print("Результат:", result)


