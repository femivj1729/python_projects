import random
print('RECIPE BOOK')
print("This recipe book is filled with recipes for awesome food.\nIts containing lists of ingredients and directions for making different food dishes.\nYou can possible to add more recipes to your cookbook and view it.")
print()
view_list=['DATE SOUP','FISH FRY','TOMATO RICE','WHITE CAKE']
choose=input('You need to ADD/VIEW/SEARCH the recipe::').upper()

class Search:
        
        def soup():
            print('DATE SOUP')
            print('---------')
            print('INGREDIENTS:\n8-10 nos date,2 nos tomato,1 tbsp lemon juice,1/4 tsp salt,1/2 tsp sugar,\n1/4 tsp black pepper powder,1 tbsp butter,1 tsp corn flour,1 tbsp fresh\ncream,3 cups water ') 
            print('\nDIRECTIONS:')
            print('1.Boil Tomato And Date Separately And Strain It.\n2.Remove The Seeds Of The Dates And Strain It And Add Some Water.\n3.Heat Butter On A Pan Add Corn Flour And Saute For One To Two Mins.\n4.Add Tomato And Dates Juice Add Sugar And Salt And Cook Till Thick.\n5.Add In The Serving Bowl And Pour Lemon Juice And Black Pepper Powder And Mix Well.\n6.Garnish With Fresh Cream,Coriander Leaves And Black Pepper Powder.')    
            print()
        
        def fry():
            print('FISH FRY')
            print('--------')
            print('INGREDIENTS:\n6 nos fish,1 tbsp ginger garlic paste,1 1/2 tbsp chilly powder,1 tsp pepper powder,\n1 tbsp curd,1 tsp coriander powder,1 tsp garam masala powder,1 tbsp salt,1 cups oil.')
            print('\nDIRECTIONS:')
            print('1.Wash the fish and pat dry with kitchen towel. Make slashes in the fish.\n2.In a small bowl take all the ingredients except oil and make a smooth paste.\n3.Rub the paste all over the fish inside the slashes too and keep aside for sometime\n4.Heat oil in a pan. When the oil is hot, reduce the heat and drop the fishes.\n5.Fry in medium heat for till golden and crisp from outside.\n6.Drain and serve with onion rings, green chillies and lemon slice.') 
            print()
        
        def rice():
            print('TOMATO RICE')
            print('-----------')
            print('INGREDIENTS:\n3 nos chopped tomatoes,1 cups cooked rice,10-12 nos curry leaves,2 nos dry red chillies,1 tsp mustard seeds,1/2 tsp jeera seeds,2 tsp ginger garlic paste,1 tsp red chilly powder,1 tbsp sambar powder,1 tsp salt,1 tbsp refined oil/ghee')
            print('\nDIRECTIONS:')
            print('1.Heat a pan, add refined oil. Add the mustard seeds , jeera seeds, dry red chillies and curry leaves.\n2.Once they splutter, add the chopped tomatoes and stir.\n3.Add the ginger garlic paste, salt, red chilly powder and cook on a low flame with lid on.\n4.Once they are mushy, add the Sambar powder and cook till done. Add water if masala tends to get dry.\n5.Mix the cooked rice and serve.')

        def cake():
            print('WHITE CAKE')
            print('----------')
            print('INGREDIENTS:\n1 cup white sugar,½ cup unsalted butter,2 large eggs,2 teaspoons vanilla extract,1 ½ cups all-purpose flour,1 ¾ teaspoons baking powder,½ cup milk')
            print('\nDIRECTIONS:')
            print('1.Preheat the oven and spread oil in the cake pan.\n2.Cream sugar and butter together in a mixing bowl. Add eggs, one at a time, beating briefly after each addition. Mix in vanilla.\n3.Combine flour and baking powder in a separate bowl. Add to the wet ingredients and mix well. Add milk and stir until smooth.\n4.Pour batter into the prepared cake pan.\n5.Bake in the preheated oven until the top springs back when lightly touched, 30 to 40 minutes.\n6.Remove from the oven and cool completely.')

class Addrecipe:
    def create():
        add_num=int(input('How many new recipes to add:'))
        for i in range(1,add_num+1):
            add_name=input('Enter new Recipe name:').upper()
            with open(f'{add_name}.txt','a')as rec:
                rec.write(f'{add_name}\n')
            for j in range(len(add_name)):
                with open(f'{add_name}.txt','a')as rec:
                    rec.write('-') 
            add_ingre=input('Enter Ingredients:')
            with open(f'{add_name}.txt','a')as rec:
                rec.write(f'\nINGREDIANTS:\n{add_ingre}\n\n')
            add_direc=input('How to prepare:')
            with open(f'{add_name}.txt','a')as rec:
                rec.write(f'DIRECTIONS:\n{add_direc}')
        
s=Search
a=Addrecipe

def main():
    if choose=='SEARCH':
        print('Recipes included in the Recipe Book:')
        for n in view_list:
            print(n,end='  ')
        print()
        recipe_name=input('Enter the recipe name to search:').upper()
        
        if recipe_name=='DATE SOUP':
             s.soup()
        elif recipe_name=='FISH FRY':
             s.fry()
        elif recipe_name=='TOMATO RICE':
             s.rice()
        elif recipe_name=='WHITE CAKE':
            s.cake()
        else:
            print('This recipe is not available in this Recipe Book')
             
    if choose=='VIEW':
         print('Views all recipes in the recipe book')
         s.soup()
         s.fry()
         s.rice()
         s.cake()

    if choose=='ADD':
         a.create()
         
main()