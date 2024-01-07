# import numb as ng
# comp_num  = ng.generate_random_number(0,1000)
# # wanna_play_again='y'
# score =0
# # while wanna_play_again=='y'
# dt = ng.give_random_range(5)
# ng.show_on_screen(comp_num,dt)
import numb as ng

comp_num = ng.generate_random_number(0,1000)
score = 0
dt = ng.give_random_range(20)
ng.show_on_screen(comp_num,dt)

user_num = ng.take_user_input() 
ng.check_if_same(comp_num,user_num)