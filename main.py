import requests

API = '4AE6oBdDqv65cxz9ldC7bw==0MlnMRH3aGvPOv05'

name_file = "4_Mezhevych.txt"

class AnalyzeFood:
    def __init__(self, product_name):
        self.product_name = product_name
        url = "https://api.calorieninjas.com/v1/nutrition?query=" + product_name
        headers = {'X-Api-Key': API}

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == requests.codes.ok:
                data_json = response.json()
                if len(data_json['items']) > 0:
                    self.data = data_json['items'][0]
                else:
                    self.data = None
                    print("We did not find this product :(")
            else:
                self.data = None
                print("Problem of loading")
        except Exception as problem:
            self.data = None
            print(f"Critical problem {problem}")

    def get_calories(self):
        if self.data is None:
            return 0

        calories = self.data['calories']

        return calories

    def get_fat(self):
        if self.data is None:
            return "Not enough information"

        amount_fat = self.data['fat_total_g']

        if 0 <= amount_fat <= 20:
            return "It is not fat food"
        elif 20 <= amount_fat <= 50:
            return "Do not eat this food at night. It is so unhealthy!"
        else:
            return "Throw away this product! It is a fat bomb"


    def get_sugar(self):
        if self.data is None:
            return "Not enough information"

        amount_sugar = self.data['sugar_g']

        if 0 <= amount_sugar <= 10:
            return "Amount of sugar is low"
        else:
            return "It has so many sugar. Throw away this product!"


    def get_protein(self):
        if self.data is None:
            return "Not enough information"

        amount_protein = self.data['protein_g']

        if amount_protein > 15:
            return "It is so good for pump your muscles!"
        else:
            return "Amount of protein is low"


    def get_carbo(self):
        if self.data is None:
            return "Not enough information"

        amount_carbo = self.data['carbohydrates_total_g']

        if amount_carbo > 50:
            return "Do not eat this product at night, because you will have swelling in the morning"
        else:
            return "Level of amount of carbo is ok"


    def get_product(self):
        return self.product_name


    def get_text(self):
        return str(self.data)

    def show(self):
        if self.data is None:
            return "Not clear information"

        name = self.get_product()
        energy = self.get_calories()
        sugar = self.data['sugar_g']
        fat = self.data['fat_total_g']
        protein = self.data['protein_g']
        carbo = self.data['carbohydrates_total_g']

        text = (f'Today you ate {name}, there are {energy} calories and {sugar} grams of sugar.\n'
                f'{self.get_sugar()}\n'
                f'PFC of product:\n'
                f'-{fat} grams of fat. {self.get_fat()}\n'
                f'-{protein} grams of protein. {self.get_protein()}\n'
                f'-{carbo} grams of carbo. {self.get_carbo()}')

        return text

    def get_data(self):
        return self.data


def ai(data):
    if data is None:
        return "not normal name of product = not advise"

    if data['sugar_g'] > 20:
        return "this can make acne worse!"
    elif data['fat_total_g'] > 30 or data['calories'] > 1500:
        return "this can cause a double chin to develop, hehe"
    else:
        return "no advise :)"

if __name__ == '__main__':
    while True:
        ask_name = input("Enter a name of product: ")
        tool = AnalyzeFood(ask_name)
        results = tool.show()
        advise = ai(tool.get_data())

        print(results)
        print(f"Your AI advise: {advise}")

        try:
            with open("4_Mezhevych.txt", "a") as file:
                file.write("------------------------------\n")
                file.write(f"Name of product: {ask_name}\n")
                file.write(f"Main information: {results}\n")
                file.write(f"AI advise: {advise}\n")
        except:
                print("Write error")