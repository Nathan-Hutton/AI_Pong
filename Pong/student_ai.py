# Define some lists here to store the history data of the game such as the positions of the balls 
position_history = []

def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    """Return "up" or "down", depending on which way the paddle should go to
    align its centre with the centre of the ball
   
    Keyword arguments:
    paddle_frect -- a rectangle representing the coordinates of the paddle
                    paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
                    corner of the rectangle
                    paddle_frect.size[0], paddle_frect.size[1] are the 
                    dimensions of the paddle along the x and y axis, 
                    respectively
   other_paddle_frect --
                    a rectangle representing the opponent paddle. It is 
                    formatted in the same way as paddle_frect
   
   ball_frect --    a rectangle representing the ball. It is formatted in the 
                    same way as paddle_frect
   table_size --    table_size[0], table_size[1] are the dimensions of the table,
                    along the x and the y axis respectively
   
   The coordinates look as follows:
   
            0             x
            |------------->
            |
            |             
            |
        y   v
    """      
    position_history.append((ball_frect.pos[0] + (ball_frect.size[0] / 2), ball_frect.pos[1] + (ball_frect.size[1] / 2)))

    if len(position_history) == 1:
        return "up"

    early_position = position_history[-2]
    late_position = position_history[-1]

    if abs(paddle_frect.pos[0] - late_position[0]) > abs(paddle_frect.pos[0] - early_position[0]):
        # Go to the middle
        if paddle_frect.pos[1] + (paddle_frect.size[1] / 2) < (table_size[1] / 2):
            return "down"
        return "up"

    slope = (late_position[1] - early_position[1]) / (late_position[0] - early_position[0])

    # if slope > 0:
    #     x_top = (0 - paddle_frect.pos[0]) / slope
    #     if x_top < table_size[0]:
    #         slope *= -1
    #         late_position = (x_top, 0)
    # else:
    #     x_top = (table_size[1] - paddle_frect.pos[0]) / slope
    #     if x_top < table_size[0]:
    #         slope *= -1
    #         late_position = (x_top, table_size[1])

    destination_y = slope * ((paddle_frect.pos[0] + (paddle_frect.size[0] / 2) - 5) - late_position[0]) + late_position[1]

    if paddle_frect.pos[1] + (paddle_frect.size[1] / 2) < destination_y:
        return "down"

    return "up"