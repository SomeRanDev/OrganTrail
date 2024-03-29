#Shash
from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over
from scenes.main_game.scene_stomach import Scene_Stomach
from scenes.main_game.scene_fever import Scene_Fever

class Scene_Antibodies(Scene_Base):
    def setup(self):
        '''
        #Note: This block is for testing only. Use if you are skipping straight to this scene
        self.set_value("vaxx", False)
        self.set_value("entry", 0)
        self.set_value("pathogen", 1) #change as needed
        self.set_value("player_frames", ["images/rashCrash_0", "images/rashCrash_1"]) #change as needed
		#temp value for player animation, will set later in enter scene
        self.set_value("player_animation", 0)
        '''
        GAME_WIDTH = self.window.game_width
        GAME_HEIGHT = self.window.game_height
        self.set_value("player_animation", self.show_picture(self.get_value("player_frames"), GAME_WIDTH/2, 30, 20))
        self.play_song("audio/testmusic2.mp3")
        self.set_background("images/bloodstream.png")

        self.add_dialog("Circulation, circulation. What a fun ride.")
        self.add_dialog("The circulatory system is how things get around.")
        self.add_dialog("Red blood cells in particular carry oxygen to different parts of the body.")
        self.add_dialog("They go from the heart to large arteries, and then to smaller capillaries near different organs.")
        self.add_dialog("Once they deliver the oxygen, they exit and travel back to the heart through veins.")
        self.add_dialog("You can probably make your way to your goal this way.")
        self.add_dialog("Just ride this out and you'll find yourself there in no time.")
        self.add_dialog("Wait...what's this??")

        antibodies = self.show_picture("images/antibodies.png", -200, 100, 30)
        self.move_picture(antibodies, 300, 100, 30)
        self.add_dialog("A white blood cell just shot you with antibodies! If they stick to you, that means your cover is blown.")
        self.add_dialog("Oh no, here it comes...")
        self.move_picture(antibodies, 1500, 100, 30)

        self.set_background("images/boxing.png")

        self.set_value("wbc", self.show_picture(["images/wbc_0", "images/wbc_1", "images/wbc_2", "images/wbc_3"], -100, 0))
        self.move_picture(self.get_value("wbc"), GAME_WIDTH/32, 0, 20)
        self.play_sound("audio/danger_jingle.wav")
        self.play_song("audio/combatmusic.mp3")
		
		#player character bounce animation
        self.move_picture(self.get_value("player_animation") ,  GAME_WIDTH/2, -20, 15)
        self.move_picture(self.get_value("player_animation") ,  GAME_WIDTH/2, 30, 15)
		
        self.add_dialog("A White Blood Cell arrived!")
        
        #chance of vaccination
        if self.get_value("vaxx"):
            self.add_dialog("The victim is vaccinated, so you only have a 20% chance of beating the cell.")
            self.add_button(x = 400,
						y = 400, 
						w = 300,
						h = 40,
						name = "Attack!",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 18, -1, False],
						action = self.fight)
        else:
            self.add_dialog("This victim is unvaccinated, so you have an 80% chance of beating the cell!")
            self.add_button(x = 400,
						y = 400, 
						w = 300,
						h = 40,
						name = "Attack!",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 18, -1, False],
						action = self.fight)

        self.wait_for_button_press()

    def fight(self):
	
        GAME_WIDTH = self.window.game_width
        GAME_HEIGHT = self.window.game_height

        if self.get_value("vaxx"):
            if self.generate_random_chance(20):
				#animation to attack
                self.move_picture(self.get_value("player_animation") ,  GAME_WIDTH/32, 30, 15)
                self.move_picture(self.get_value("player_animation") ,  GAME_WIDTH/2, 30, 15)
				
				#animation of WBC death
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/32, -20, 20)
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/32, 600, 30)
                self.remove_all_buttons()
                self.add_dialog("Hit! Show 'em who's boss!")
                self.add_dialog("Better get going before more show up...")
				
                if self.get_value("pathogen") == 1:
                    self.goto_scene(Scene_Stomach)
                else:
                    self.goto_scene(Scene_Fever)
            else:
                self.remove_all_buttons()
				
				#wbc animation to attack
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 30, 20)
				
				#wbc chowing down motion
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 35, 10)
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 25, 10)
				
                self.add_dialog("Your will was strong, but the blood cell was stronger...")
                
                self.goto_scene(Scene_Game_Over)
        else:
            if self.generate_random_chance(80):
                self.remove_all_buttons()
                
				#animation to attack
                self.move_picture(self.get_value("player_animation") ,  GAME_WIDTH/32, 30, 15)
                self.move_picture(self.get_value("player_animation") ,  GAME_WIDTH/2, 30, 15)
                self.add_dialog("Hit! Show 'em who's boss!")
				
				#animation of WBC death
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/32, -20, 20)
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/32, 600, 30)
                self.add_dialog("Better get going before more show up...")
				
                if self.get_value("pathogen") == 1:
                    self.goto_scene(Scene_Stomach)
                else:
                    self.goto_scene(Scene_Fever)

            else:
                self.remove_all_buttons()
				
				#wbc animation to attack
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 30, 20)
				
				#wbc chowing down  motion
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 40, 30)
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 20, 30)
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 40, 30)
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 20, 30)
				
                self.add_dialog("Your will was strong, but the blood cell was stronger...")
                self.goto_scene(Scene_Game_Over)

        

    