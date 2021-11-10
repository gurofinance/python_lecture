foods = {"떡볶이":"오뎅",
         "짜장면":"단무지",
         "라면":"김치",
         "피자":"피클",
         "맥주":"땅콩",
         "치킨":"치킨무",
         "삼겹살":"상추",
        };
food_list = zip((list(foods.keys()), list(foods.values())))
print(food_list)s
for i , data in food_list:
    print(i)