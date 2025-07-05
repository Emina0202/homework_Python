from address import Address
from mailing import Mailing

to_addr = Address(
    index='123456',
    city='Каспийск',
    street='Ленина',
    house='20',
    apartment='5'
    )
from_addr = Address(
    index='654321',
    city='Махачкала',
    street='Петра1',
    house='20',
    apartment='10'
    )

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=200, track='ABCD1234'
    )

print(
    f'Отправление {mailing.track} '
    f'из {mailing.from_address.index}, {mailing.from_address.city}, '
    f'{mailing.from_address.street}, {mailing.from_address.house}-'
    f'{mailing.from_address.apartment} '
    f'в {mailing.to_address.index}, {mailing.to_address.city}, '
    f'{mailing.to_address.street}, {mailing.to_address.house}-'
    f'{mailing.to_address.apartment}. '
    f'Стоимость {mailing.cost} рублей.'
)
