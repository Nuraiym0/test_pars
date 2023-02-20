# import csv 
# from peewee import *


# db = PostgresqlDatabase(database='parsing', user = 'nuraiym', password='1', host='localhost')


# class Coin(Model):
#     time = CharField()
#     price = CharField()
#     image = TextField()

#     class Meta:
#         database = db


# def main():

#     db.connect()
#     db.create_tables([Coin])

#     with open('parsing.csv') as f:
#         order = ["time", "price",'image',]
#         reader = csv.DictReader(f, fieldnames=order)

#         coins = list(reader)

#         # for row in coins:
#         #     # print (row)
#         #     coin = Coin(time=row['time'], price=row['price'], image=row['image'])
#         #     coin.save()
#         with db.atomic():
#             for index in range(0, len(coins), 100):
#                 Coin.insert_many(coins[index:index+100]).execute( )

















# if __name__ == "__main__":
#     main()

















