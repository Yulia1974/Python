from Address import Address
from Mailing import Mailing

from_address = Address("789456","Тольятти","Ленинский","21","90")
to_address = Address("123456","Самара","Авроры","119","80")

mailing = Mailing(to_address,from_address,555,'AAA123456')

print(mailing)