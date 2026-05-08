import arcade
import random

width = 800
height = 600
move_speed = 2.5

class Snake(arcade.Window):

    def __init__(self): 
        super().__init__(width, height, "Snake")

        arcade.set_background_color(arcade.color.BLACK)

        self.direction_x = move_speed
        self.direction_y = 0

        self.snake_x = width // 2
        self.snake_y = height // 2

        self.food_x = random.randint(0, width - 20)
        self.food_y = random.randint(0, height - 20)

        self.snake_body = []
        self.snake_length = 1

    def on_draw(self):
        self.clear()

        for segment in self.snake_body:
            arcade.draw_rect_filled(
                arcade.XYWH(
                    segment[0],
                    segment[1],
                    20, 20
                ),
                arcade.color.GREEN
            )

    
        arcade.draw_rect_filled(
            arcade.XYWH(
                self.food_x,
                self.food_y,
                20, 20
            ),
            arcade.color.RED
        )


    def on_update(self, delta_time):
        self.snake_x += self.direction_x
        self.snake_y += self.direction_y

        if (
            abs(self.snake_x - self.food_x) < 20 
            and abs(self.snake_y -self.food_y) < 20
        ): 
            self.food_x = random.randint(0, width - 20)
            self.food_y = random.randint(0, height - 20)

            self.snake_length += 8

        self.snake_body.append((self.snake_x, self.snake_y))
        
        if len(self.snake_body) > self.snake_length:
            self.snake_body.pop(0)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.direction_x = 0
            self.direction_y = move_speed

        elif key == arcade.key.DOWN:
            self.direction_x = 0
            self.direction_y = -move_speed

        elif key == arcade.key.LEFT:
            self.direction_x = -move_speed
            self.direction_y = 0

        elif key == arcade.key.RIGHT:
            self.direction_x = move_speed
            self.direction_y = 0

game = Snake()
arcade.run()