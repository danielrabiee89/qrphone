from peewee import SqliteDatabase, IntegerField, Model


db = SqliteDatabase("phone.db")


class Phone(Model):
    Phone_number = IntegerField()

    class Meta:
        database = db
        db_database = "QRphone"

db.connect()
db.create_tables([Phone])
db.close()
