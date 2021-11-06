import random
import sys
from game import constants
from game.action import Action
from game.point import Point


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0]
        paddle = cast["paddle"][0]
        bricks = cast["brick"]

        # PADDLE
        for offset in range(len(paddle.get_text())):
            point = Point(paddle.get_position().get_x() + offset, paddle.get_position().get_y())
            if ball.get_position().equals(point):
                reverse = ball.get_velocity().reverse()
                new_direction = Point(random.choice([-1, 1]), reverse.get_y())
                ball.set_velocity(new_direction)
        
        # BRICKS
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                bricks.remove(brick)

                reverse = ball.get_velocity().reverse()
                new_direction = Point(random.choice([-1, 1]), reverse.get_y())
                ball.set_velocity(new_direction)

        # WALLS
        if ball.get_position().equals(Point(ball.get_position().get_x(), 0)):
            reverse = ball.get_velocity().reverse()
            new_direction = Point(random.choice([1, -1]), reverse.get_y())
            ball.set_velocity(new_direction)
        
        if ball.get_position().equals(Point(0, ball.get_position().get_y())) or ball.get_position().equals(Point(constants.MAX_X, ball.get_position().get_y())):
            reverse = ball.get_velocity().reverse()
            new_direction = Point(reverse.get_x(), random.choice([1, -1]))
            ball.set_velocity(new_direction)

        if ball.get_position().equals(Point(ball.get_position().get_x(), constants.MAX_Y)):
            sys.exit()
