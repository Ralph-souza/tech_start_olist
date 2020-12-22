class Product:
    __sku: str
    __name: str
    __price: float
    __weight: float
    __height: float
    __length: float
    __width: float
    __description: float
    __categories: list

    def set_categories(self, category: str) -> None:
        self.__categories.append(category)

    def get_categories(self) -> list:
        return self.__categories

    def set_sku(self, sku: str) -> None:
        self.__sku = sku

    def get_sku(self) -> str:
        return self.__sku  

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_price(self, price: float) -> None:
        self.__price = price
    
    def get_price(self) -> str:
        return self.__price

    def set_weight(self, weight: float) -> None:
        self.__weight = weight

    def get_weight(self) -> float:
        return self.__weight

    def set_height(self, height: float) -> None:
        self.__height = height

    def get_height(self) -> float:
        return self.__height

    def set_length(self, length: float) -> None:
        self.__length = length

    def get_length(self) -> float:
        return self.__length

    def set_width(self, width: float) -> None:
        self.__width = width

    def get_width(self) -> float:
        return self.__width

    def set_description(self, description: str) -> None:
        if len(description) >= 20:
            self.__description = description
        else:
            print("Description must be bigger than 20 char")

    def get_description(self) -> str:
        return self.__description

    
    def __str__(self):
        return f"""
                    - SKU: {self.get_sku()}
                    - Name: {self.get_name()}
                    - Price: {self.get_price()}
                    - Weight: {self.get_weight()}
                    - Height: {self.get_height()}
                    - Length: {self.get_length()}
                    - Width: {self.get_width()}
                    - Description: {self.get_description()}
                 """