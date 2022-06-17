
# seller sql table
'''CREATE TABLE "SELLER" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"SL_ID"	TEXT NOT NULL UNIQUE,
	"EMAIL"	INTEGER NOT NULL UNIQUE,
	"PASSWORD"	TEXT NOT NULL,
	"INVENTORY_WALLET"	REAL DEFAULT 0,
	"PRODUCTS"	TEXT,
	"STATUS"	TEXT,
	"SCORE"	INTEGER,
	PRIMARY KEY("ID" AUTOINCREMENT)
);'''


class seller:
    def __init__(self, SL_ID , email : str , password : str, inventory_wallet : int, history : dict , products : dict, location : str, score) -> None:
        pass


    def add_to_db(self):
        pass


    def changepassword(self, oldpassword, newpassword):
        pass


    def changeemail(self, newewmail, password):
        pass


    def rate(self, flag):
        pass


    def order_reports(self):
        pass

    def PR_id_generator(self):
        pass


# product sql table
'''CREATE TABLE "PRODUCT" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"PR_ID"	TEXT NOT NULL UNIQUE,
	"NAME"	TEXT NOT NULL UNIQUE,
	"NUMBER"	INTEGER NOT NULL,
	"PRICE"	INTEGER NOT NULL,
	"SELLER_SL_ID"	TEXT,
	"STATUS"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("SELLER_SL_ID") REFERENCES "SELLER"
);'''

class products:
    def __init__(self, name,  PR_ID, seller, number, price):
        self.__name = name 
        self.__PR_ID = PR_ID
        self.__seller = seller
        self.__number = number 
        self.__price = price


    def add_product(self, name ):
        pass

    def remove_product(self):
        pass

    def add_comment(self, CU_ID, comment):
        pass

    def show_comments(self):
        pass


