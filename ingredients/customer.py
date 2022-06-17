
# customer sql table

'''CREATE TABLE "CUSTOMER" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"CU_ID"	TEXT NOT NULL UNIQUE,
	"EMAIL"	TEXT NOT NULL UNIQUE,
	"PASSWORD"	TEXT NOT NULL,
	"BASKET"	TEXT,
	"FAVORIT"	TEXT,
	"INVENTORY_WALLET"	REAL DEFAULT 0,
	"LOCATION"	TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);'''



class customer:
    
    def __init__(self, CU_ID , email : str , password : str , basket : dict , inventory_wallet : int , favorit : list, location :str ) -> None:
        self.__email = email
        self.__CU_ID = CU_ID
        self.__password = password
        self.__basket = basket
        self.__inventory_wallet = inventory_wallet
        self.__favorit = favorit



    def card_to_wallet(self, value):
        pass


    def wallet_to_card(self, value):
        pass

    def changepassword(self, oldpassword, newpassword):
        pass


    def changeemail(self, newewmail, password):
        pass


    def add_to_basket(self,PR_ID, num, SL_ID) :
        pass

    def add_favorites (self, PR_ID):
        pass

    
    def show_history(self):
        pass

    def save_to_db(self):
        pass

    def show_shop_page(self, shop_name):
        pass

    def show_product(self, CU_ID):
        pass
