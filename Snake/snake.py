import arcade #type: ignore // added this because it said there was a missing pylance import
import random

grid_size = 20
width = 800
height = 600
move_speed = grid_size

class Snake(arcade.Window):

    def __init__(self): 
        super().__init__(width, height, "Snake")

        arcade.set_background_color(arcade.color.BLACK)

        self.set_update_rate(0.15)

        self.setup()

    def setup(self):

        self.direction_x = move_speed
        self.direction_y = 0

        self.snake_x = width // 2
        self.snake_y = height // 2

        self.food_x = random.randrange(0, width, grid_size)
        self.food_y = random.randrange(0, height, grid_size)

        self.snake_body = []
        self.snake_length = 1

        self.score = 0

        self.game_over = False


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

        arcade.draw_text(
            f"score: {self.score}", 10, height - 30, arcade.color.WHITE, 20
        )

        if self.game_over:

            arcade.draw_text("Press R to restart",
                            width // 2,
                            height // 2 - 20,
                            arcade.color.WHITE,
                            20,
                            anchor_x = "center"
                            )


    def on_update(self, delta_time):
        if self.game_over: return
        self.snake_x += self.direction_x
        self.snake_y += self.direction_y

        if self.snake_x == self.food_x and self.snake_y == self.food_y: 
            self.food_x = random.randrange(0, width, grid_size)
            self.food_y = random.randrange(0, height, grid_size)
            self.score += 1
            self.snake_length += 1

        self.snake_body.append((self.snake_x, self.snake_y))
        
        if len(self.snake_body) > self.snake_length:
            self.snake_body.pop(0)

        for segment in self.snake_body[:-1]:
            if segment == (self.snake_x, self.snake_y):
                self.game_over = True

        if (
            self.snake_x < 0
            or self.snake_x >= width
            or self.snake_y < 0
            or self.snake_y >= height
        ):
            self.game_over = True

    def on_key_press(self, key, modifiers):

        if self.game_over and key == arcade.key.R:
            self.setup()

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