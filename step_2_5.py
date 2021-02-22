m_list = [9,7,5,4,3]
print(m_list)
a = int(input('введите число:  '))
for el in m_list:
    if el < a:
        n = m_list.index(el)
        print(n)
        m_list.insert(n, a)
        break
if a < el:
    m_list.append(a)
print(m_list)