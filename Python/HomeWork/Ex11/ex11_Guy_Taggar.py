''' Exercise #11. Computational Thinking and Programming.'''


#########################################
# Question 1 - do not delete this comment
#########################################
class Dish:
    def __init__(self, name, price, calories, ingredients):
        if calories <= 0 or price <= 0:
            raise ValueError('Cant have zero calories or price !')
        self.name = name
        self.price = float(price)
        self.calories = int(calories)
        self.ingredients = ingredients[:]

    def __repr__(self):
        return f'{self.name} costs {self.price} NIS and contains: {self.ingredients}\n(Only {self.calories} calories!)'

    def __lt__(self, other):
        if self.price == other.price:
            return len(self.ingredients) < len(other.ingredients)
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price and len(self.ingredients) == len(other.ingredients)

    def __le__(self, other):
        return self < other or self == other

    def add_ingredient(self, ingredient, calories):
        if ingredient in self.ingredients:
            raise ValueError(f'{ingredient} already exists in {self.name}')
        self.ingredients.append(ingredient)
        self.calories += calories
        return None

    def remove_ingredient(self, ingredient, calories):
        if ingredient not in self.ingredients:
            raise ValueError(f'{self.name} doesn\'t have {ingredient}')
        self.ingredients.remove(ingredient)
        self.calories -= calories
        return None


#########################################
# Question 2 - do not delete this comment
#########################################
class Beverage:
    def __init__(self, name, price, is_diet):
        if price <= 0:
            raise ValueError('Cant have zero price !')
        self.name = name
        self.price = float(price)
        self.is_diet = is_diet

    def __repr__(self):
        if self.is_diet:
            return f'{self.name} costs {self.price} NIS (diet)'
        return f'{self.name} costs {self.price} NIS'

    def get_price(self, size='normal'):
        if size not in ['small', 'normal', 'big']:
            raise ValueError('size must be "small", "normal" or "big" ')
        if size == 'small':
            return self.price * 0.8
        elif size == 'big':
            return self.price * 1.2
        return self.price


#########################################
# Question 3 - do not delete this comment
#########################################
class Meal:
    def __init__(self, name, beverage, dishes):
        self.name = name
        self.beverage = beverage
        self.dishes = dishes[:]
        self.is_diet = (beverage.is_diet and sum([dish.calories for dish in dishes]) < 800)

    def __repr__(self):
        if self.is_diet:
            return f'{self.name} meal costs {self.get_price()} NIS (healthy!)'
        return f'{self.name} meal costs {self.get_price()} NIS'

    def get_price(self):
        return self.beverage.get_price('small') + sum(dish.price for dish in self.dishes) - min(
            dish.price for dish in self.dishes)

    # add the bonus method down here (inside Meal class) if you wish
    def __contains__(self, item):
        lst = []
        for dish in self.dishes:
            for ingredient in dish.ingredients:
                lst.append(ingredient)
        return item in lst
