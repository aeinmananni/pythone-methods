# یک تاپل به نام coordinates بسازید که شامل مختصات نقطه A در صفحه باشد ( (4, 3) = a). سپس کدی بنویسید که مسافت این نقطه تا مبدا (0, 0) را محاسبه کند.
# برای محاسبه مسافت بین دو نقطه در صفحه مختصات از فرمول مسافت اقلیدسی استفاده کنید:
# distance = √((x₂ - x₁)² + (y₂ - y₁)²)
import math


coordinates =(4,3)
b=(0,0)
distance1 = math.sqrt((b[0] - coordinates[0])** 2 + (b[1] - coordinates[1])**2)
distance2 = math.dist(coordinates, (0, 0))
print(distance1)
print(distance2)