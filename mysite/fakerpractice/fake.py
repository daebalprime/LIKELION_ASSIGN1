from faker import Faker

myfake = Faker()
# Faker('ko_KR')

#Faker의 메소드를 통해 어떤 종류의 가짜 데이터를 뽑아낼 지 결정 가능

#가짜 데이터가 생성될 때 마다 달라지지 않기를 바라는 것)
# Seed 파일. 개념은 잘 알것이라 생각함.

myfake.seed(47)

myfake.name()
myfake.address()
myfake.state()
myfake.text()
myfake.sentence()
myfake.random_number()
