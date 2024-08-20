########################
# This is a smiple app to track initiative in D&D
# It will have a list of characters and their initiative and update the list as the game progresses

import tkinter as tk
from tkinter import ttk

###########################

# dnd specific variables
# proficiency bonus at lvl n
def proficiency(n : int) -> int:
    if n > 20 or n < 1:
        raise ValueError("Level must be between 1 and 20")
    else:
        return 2 + (n-1)//4
    
# primary stat for each class when attacking
primary_ability = {'barbarian': 'strength', 'bard': 'charisma', 'cleric': 'wisdom', 'druid': 'wisdom',
                   'fighter': 'strength', 'monk': 'dexterity', 'paladin': 'strength', 'ranger': 'dexterity',
                   'rogue': 'dexterity', 'sorcerer': 'charisma', 'warlock': 'charisma', 'wizard': 'intelligence'}


# Create a list of characters and their initiative
characters = []

# Create a function to submit stats for a character
def submit_stats():
    name = char_name_var.get()
    str = char_str_var.get()
    dex = char_dex_var.get()
    con = char_con_var.get()
    int = char_int_var.get()
    wis = char_wis_var.get()
    cha = char_cha_var.get()
    hp = char_hp_var.get()
    ac = char_ac_var.get()
    lvl = char_lvl_var.get()
    char_class = char_class_var.get()
    spell_slots1 = char_spell_slots1_var.get()
    spell_slots2 = char_spell_slots2_var.get()
    spell_slots3 = char_spell_slots3_var.get()
    spell_slots4 = char_spell_slots4_var.get()
    spell_slots5 = char_spell_slots5_var.get()
    spell_slots6 = char_spell_slots6_var.get()
    spell_slots7 = char_spell_slots7_var.get()
    spell_slots8 = char_spell_slots8_var.get()
    spell_slots9 = char_spell_slots9_var.get()

    characters.append([name, [str, dex, con, int, wis, cha], hp, ac,                        
                       [spell_slots1, spell_slots2,spell_slots3,
                        spell_slots4,spell_slots5,spell_slots6,
                        spell_slots7,spell_slots8,spell_slots9]
                         , lvl, char_class])
    treev.insert("", 'end', name, 
                 values =(0, name, hp, ac, 
                          [spell_slots1,spell_slots2,spell_slots3,
                           spell_slots4,spell_slots5,spell_slots6,
                           spell_slots7,spell_slots8,spell_slots9], "None"))
    
    


# Create a function to add a character to the list
def add_character():

# Create a new window to add a character
    new_char_window = tk.Toplevel(window)
    new_char_window.title('Add Character')
    new_char_window.geometry('650x350')
    submit_button = tk.Button(new_char_window, text = 'Submit', command = submit_stats)
    submit_button.place(x=300, y=300)

    # Create a label to prompt the user to enter the character's name
    tk.Label(new_char_window, text = 'Enter Character Name:').place(x=260 , y = 0)


    # Create an entry box for the user to enter the character's name
    name_entry = tk.Entry(new_char_window, textvariable = char_name_var)
    name_entry.place(x=260, y = 20)

    # Create a label to prompt the user to enter the character's stats
    tk.Label(new_char_window, text = 'Enter Modifiers:').place(x=250, y = 60)

    # Create an entry boxes for the user to enter the stats
    str_entry = tk.Entry(new_char_window, textvariable = char_str_var)
    str_entry.place(x=0, y = 80)
    
    dex_entry = tk.Entry(new_char_window, textvariable = char_dex_var)
    dex_entry.place(x=100, y=80)

    con_entry = tk.Entry(new_char_window, textvariable = char_con_var)
    con_entry.place(x=200, y=80)

    int_entry = tk.Entry(new_char_window, textvariable = char_int_var)
    int_entry.place(x=300, y=80)

    wis_entry = tk.Entry(new_char_window, textvariable = char_wis_var)
    wis_entry.place(x=400, y=80)

    cha_entry = tk.Entry(new_char_window, textvariable = char_cha_var)
    cha_entry.place(x=500, y=80)     

    # Create labels for the user to enter the character's stats
    tk.Label(new_char_window, 
              justify=tk.CENTER,
              padx = 10, 
              text="Strength").place(x=0, y=100)
    tk.Label(new_char_window, 
              justify=tk.CENTER,
              padx = 10, 
              text="Dexterity").place(x=100, y=100)
    tk.Label(new_char_window, 
              justify=tk.CENTER,
              padx = 10, 
              text="Constitution").place(x=200, y=100)
    tk.Label(new_char_window, 
              justify=tk.CENTER,
              padx = 10, 
              text="Intelligence").place(x=300, y=100)
    tk.Label(new_char_window, 
              justify=tk.CENTER,
              padx = 10, 
              text="Wisdom").place(x=400, y=100)
    tk.Label(new_char_window, 
              justify=tk.CENTER,
              padx = 10, 
              text="Charisma").place(x=500, y=100)
    
    # Create a entry boxes for level, class, hp and ac
    lvl_entry = tk.Entry(new_char_window, textvariable = char_lvl_var)
    class_entry = tk.Entry(new_char_window, textvariable = char_class_var)
    hp_entry = tk.Entry(new_char_window, textvariable = char_hp_var)
    ac_entry = tk.Entry(new_char_window, textvariable = char_ac_var)
    
    
    # create labels for hp, ac, class, and proficiency
    lvl_label = tk.Label(new_char_window,justify=tk.CENTER,
              padx = 10, text="Level")
    class_label = tk.Label(new_char_window,justify=tk.CENTER,
              padx = 10, text="Class")
    hp_label = tk.Label(new_char_window,justify=tk.CENTER,
                padx = 10, text="HP")
    ac_label = tk.Label(new_char_window,justify=tk.CENTER,
                padx = 10, text="AC")
    
    # place the labels and entry boxes
    class_label.place(x=50, y=140)
    class_entry.place(x=50, y=160)

    lvl_label.place(x=200, y=140) 
    lvl_entry.place(x=200, y=160)    

    hp_label.place(x=300, y=140)
    hp_entry.place(x=300, y=160)

    ac_label.place(x=400, y=140)
    ac_entry.place(x=400, y=160)

    # Create a label to prompt the user to enter the character's spell slots
    tk.Label(new_char_window, text = 'Enter Character Spell Slots:').place(x=250, y = 200)

    # Create an entry boxes for the user to enter the spell slots
    spell_slots1_entry = tk.Entry(new_char_window, textvariable = char_spell_slots1_var)
    spell_slots2_entry = tk.Entry(new_char_window, textvariable = char_spell_slots2_var)
    spell_slots3_entry = tk.Entry(new_char_window, textvariable = char_spell_slots3_var)
    spell_slots4_entry = tk.Entry(new_char_window, textvariable = char_spell_slots4_var)
    spell_slots5_entry = tk.Entry(new_char_window, textvariable = char_spell_slots5_var)
    spell_slots6_entry = tk.Entry(new_char_window, textvariable = char_spell_slots6_var)
    spell_slots7_entry = tk.Entry(new_char_window, textvariable = char_spell_slots7_var)
    spell_slots8_entry = tk.Entry(new_char_window, textvariable = char_spell_slots8_var)
    spell_slots9_entry = tk.Entry(new_char_window, textvariable = char_spell_slots9_var)

    # Create labels for the user to enter the character's spell slots
    spell_slots1_label = tk.Label(new_char_window,
                                    justify=tk.CENTER,
                                    padx = 0,
                                    text="1st Level")
    spell_slots2_label = tk.Label(new_char_window,
                                    justify=tk.CENTER,
                                    padx = 0,
                                    text="2nd Level")
    spell_slots3_label = tk.Label(new_char_window,
                                    justify=tk.CENTER,
                                    padx = 0,
                                    text="3rd Level")
    spell_slots4_label = tk.Label(new_char_window,
                                    justify=tk.CENTER,
                                    padx = 0,
                                    text="4th Level")
    spell_slots5_label = tk.Label(new_char_window,
                                    justify=tk.CENTER,
                                    padx = 0,
                                    text="5th Level")
    spell_slots6_label = tk.Label(new_char_window,
                                    justify=tk.CENTER,
                                    padx = 0,
                                    text="6th Level")
    spell_slots7_label = tk.Label(new_char_window,
                                    justify=tk.CENTER,
                                    padx = 0,
                                    text="7th Level")
    spell_slots8_label = tk.Label(new_char_window,
                                    justify=tk.CENTER,
                                    padx = 0,
                                    text="8th Level")
    spell_slots9_label = tk.Label(new_char_window,
                                    justify=tk.CENTER,
                                    padx = 0,
                                    text="9th Level")
    
    # place the labels and entry boxes
    spell_slots1_label.place(x=0, y=220)
    spell_slots1_entry.place(x=0, y=240)

    spell_slots2_label.place(x=70, y=220)
    spell_slots2_entry.place(x=70, y=240)

    spell_slots3_label.place(x=140, y=220)
    spell_slots3_entry.place(x=140, y=240)

    spell_slots4_label.place(x=210, y=220)
    spell_slots4_entry.place(x=210, y=240)

    spell_slots5_label.place(x=280, y=220)
    spell_slots5_entry.place(x=280, y=240)
    
    spell_slots6_label.place(x=350, y=220)
    spell_slots6_entry.place(x=350, y=240)

    spell_slots7_label.place(x=420, y=220)
    spell_slots7_entry.place(x=420, y=240)

    spell_slots8_label.place(x=490, y=220)
    spell_slots8_entry.place(x=490, y=240)

    spell_slots9_label.place(x=560, y=220)
    spell_slots9_entry.place(x=560, y=240)

    


    
# Create a function to set initiative for a character
def set_initiative():
    for character in characters:
        # get the initiative value from the entry box and add dex modifier
        init = globals()[f'{character[0]}_init_var'].get() + character[1][1]

        # set the initiative value for the character
        character[-1] = init
        treev.set(character[0], 'Initiative', init)

    # update the initiative order in the characters list
    characters.sort(key = lambda x: x[-1], reverse = True)
    for i in range(len(characters)):
        treev.move(characters[i][0], '', i)





# Create a function to roll for initiative
def roll_initiative()-> None:
    # Create a new window to prompt character to roll for initiative
    new_window = tk.Toplevel(window)
    new_window.title('Roll for Initiative!')
    new_window.geometry('800x200')

    # Create a label to prompt the character to roll for initiative
    tk.Label(new_window, text = "Roll a D20!").pack()

    # Create an entry box for each character to enter their initiative roll
    i = 0
    for character in characters:
        globals()[f'{character[0]}_init_var'] = tk.IntVar()
        tk.Entry(new_window, textvariable = 
             globals()[f'{character[0]}_init_var']).place(x=i, y=100)
        tk.Label(new_window, text = character[0]).place(x=i, y=120)
        i = i + 800/len(characters)

    

    # Create a button to roll for initiative
    roll_button = tk.Button(new_window, text = 'Submit', command = lambda: set_initiative())
    roll_button.pack()



# create a function to track combat
def track_combat() -> None:
    # Create a new window to prompt the user to track combat
    combat_window = tk.Toplevel(window)
    combat_window.title('Fight!')
    combat_window.geometry('800x400')

    # organize the players in their initiative order 
    ordered_chars = treev.get_children()

    # select the first character to go
    globals()['turn_counter'] : int = 0
    num_players = len(ordered_chars)
    treev.selection_set(ordered_chars[globals()['turn_counter']])

    # if an attack hits, open a window to prompt for damage
    def attack_hits() -> None:
        hit_window = tk.Toplevel(combat_window)
        hit_window.title('That\'s a Hit!')
        hit_window.geometry('400x200')
        # create a label to prompt the user to enter the damage
        damage_entry = tk.Entry(hit_window, textvariable=damage_roll_var)
        damage_prompt = tk.Label(hit_window, text = 'Enter the damage:')
        damage_entry.pack()
        damage_prompt.pack()

        #create function do deal the damage and update tree
        def deal_damage() ->  None:
            # get the damage and target from the entry boxes
            damage = damage_entry.get()
            target = target_select.get()
            
            #####BUG CHECK######
            print(f"{damage = }")
            print(f"{target = }")

            # subtract the damage from the target's HP
            current_hp = treev.item(target)['values'][2]
            treev.set(target, 'HP', int(current_hp) - int(damage))
            # after the attack is resolved, move to the next character
            globals()['turn_counter'] += 1
            treev.selection_set(ordered_chars[globals()['turn_counter'] % num_players] )
            current_turn_label.config(text = f"It's {ordered_chars[globals()['turn_counter']]}'s turn!")           
            hit_window.destroy()
        # create buttons to submit/cancel the damage
        
        submit_button = tk.Button(hit_window, text = 'Deal Damage', command = lambda: deal_damage())
        cancel_button = tk.Button(hit_window, text = 'Cancel', command = lambda: hit_window.destroy())

        
        # create an entry box for the user to enter the damage
        
        # place the buttons
        submit_button.pack()
        cancel_button.pack()

    # if an attack misses, open a window to confirm or cancel the miss
    def attack_misses() -> None:
        miss_window = tk.Toplevel(combat_window)
        miss_window.title('That\'s a Miss!')
        miss_window.geometry('400x200')

        def miss_damage() -> None:
            # after the attack is resolved, move to the next character
            globals()['turn_counter'] += 1
            treev.selection_set(ordered_chars[globals()['turn_counter'] % num_players] )
            current_turn_label.config(text = f"It's {ordered_chars[globals()['turn_counter']]}'s turn!")
            miss_window.destroy()

        # create buttons to confirm/cancel the miss
        confirm_button = tk.Button(miss_window, text = 'Bummer!', command = lambda: miss_damage())
        cancel_button = tk.Button(miss_window, text = 'Cancel', command = lambda: miss_window.destroy())

        # place the buttons
        confirm_button.pack()
        cancel_button.pack()

    # create function which makes current player attack
    def attack(roll : int, target : str) -> None:
        # determine if the attack hits
        print(treev.item(target))
        print(int(treev.item(target)['values'][3]))
        if int(roll) >= int(treev.item(target)['values'][3]):
            attack_hits()
        else:
            attack_misses()
        


    


    

    # Tell the user who's turn it is
    current_turn_label = tk.Label(combat_window, text = f"It's {ordered_chars[globals()['turn_counter']]}'s turn!")
    current_turn_label.pack()

    damage_roll = tk.Entry(combat_window)
    target_select = ttk.Combobox(combat_window, values = ordered_chars)
    attack_button = tk.Button(combat_window, text = 'Roll to hit', command= lambda: attack(damage_roll.get(), target_select.get()))
    
    damage_roll.pack()
    attack_button.pack()
    target_select.pack()

# Create the main window
window = tk.Tk()
window.title('Initiative Tracker')
window.resizable(width = 20, height = 10)


# Use treeview to display the list of characters
treev = ttk.Treeview(window)

# Configuring treeview
treev.pack(side = 'right')
verscrlbar = ttk.Scrollbar(window, orient ="vertical", command = treev.yview)
verscrlbar.pack(side ='right', fill ='x')

# Defining number of columns
treev["columns"] = ("Initiative", "Name", "HP" , "AC", "Spell Slots", "Effects")

# Defining heading
treev['show'] = 'headings'

# Assigning the width and anchor to  the respective columns
treev.column("Initiative", width = 60, anchor ='center')
treev.column("Name", width = 150, anchor ='center')
treev.column("HP", width = 80, anchor ='center')
treev.column("AC", width = 80, anchor ='center')
treev.column("Spell Slots", width = 150, anchor ='center')
treev.column("Effects", width = 150, anchor ='center')


# Assigning the heading names to the respective columns
treev.heading("Initiative", text ="Init")
treev.heading("Name", text ="Name")
treev.heading("HP", text ="HP")
treev.heading("AC", text ="AC")
treev.heading("Spell Slots", text ="Spell Slots")
treev.heading("Effects", text ="Active Effects")

# Create variables
char_init_var = tk.IntVar(); char_name_var = tk.StringVar();
char_str_var = tk.IntVar();char_dex_var = tk.IntVar()
char_con_var = tk.IntVar();char_int_var = tk.IntVar()
char_wis_var = tk.IntVar();char_cha_var = tk.IntVar()
char_hp_var = tk.IntVar();char_ac_var = tk.IntVar()
char_lvl_var = tk.IntVar();char_class_var = tk.StringVar()
char_spell_slots1_var = tk.IntVar();char_spell_slots2_var = tk.IntVar()
char_spell_slots3_var = tk.IntVar();char_spell_slots4_var = tk.IntVar()
char_spell_slots5_var = tk.IntVar();char_spell_slots6_var = tk.IntVar()
char_spell_slots7_var = tk.IntVar();char_spell_slots8_var = tk.IntVar()
char_spell_slots9_var = tk.IntVar()

damage_roll_var = tk.IntVar()

# Create a button to add a character
add_button = tk.Button(window, text = 'Add Character', command = add_character).pack()

# Create a button to roll for initiative
roll_button = tk.Button(window, text = 'Roll for Initiative', command = lambda: roll_initiative()).pack()

# create a button to start combat
fight_button = tk.Button(window, text = 'Start Combat', command=lambda:track_combat()).pack()



window.mainloop()