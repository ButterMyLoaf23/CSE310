import arcade

width = 800
height = 600
move_speed = 5

class Snake(arcade.Window):

    def __init__(self): 
        super().__init__(width, height, "Snake")

        arcade.set_background_color(arcade.color.BLACK)

        self.snake_x = width // 2
        self.snake_y = height // 2

    def on_draw(self):
        self.clear()

        arcade.draw_lrbt_rectangle_filled(
            self.snake_x,
            self.snake_x + 20,
            self.snake_y,
            self.snake_y + 20,
            arcade.color.GREEN
        )

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.snake_y += move_speed

        elif key == arcade.key.DOWN:
            self.snake_y -= move_speed

        elif key == arcade.key.LEFT:
            self.snake_x -= move_speed

        elif key == arcade.key.RIGHT:
            self.snake_x += move_speed

game = Snake()
arcade.run()