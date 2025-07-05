from smartphone import Smartphone  # Импортируем класс Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14 Pro Max", "+79876543210"),
    Smartphone("Samsung", "Galaxy S23 Ultra", "+79123456789"),
    Smartphone("Xiaomi", "Redmi Note 11S", "+79012345678"),
    Smartphone("Huawei", "P50 Pro", "+79234567890"),
    Smartphone("Google", "Pixel 7 Pro", "+79345678901")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
