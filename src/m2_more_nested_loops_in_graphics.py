"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Mashengjun Li.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    ori_x = rectangle.corner_1.x
    ori_y = rectangle.corner_1.y
    ori_x1 = rectangle.corner_2.x
    ori_y1 = rectangle.corner_2.y
    x = ori_x
    y = ori_y
    x1 = ori_x1
    y1 = ori_y1
    change_x_by = x1 - x
    change_y_by = y1 - y
    for j in range(n):
        for k in range(j+1):
            new_rec_corner1 = rg.Point(x, y)
            new_rec_corner2 = rg.Point(x1, y1)
            new_rec = rg.Rectangle(new_rec_corner1, new_rec_corner2)
            new_rec.attach_to(window)
            window.render()
            x = x + change_x_by
            x1 = x1 + change_x_by
        y = y + change_y_by
        y1 = y1 + change_y_by
        x = ori_x - ((k + 1) * 0.5) * change_x_by
        x1 = ori_x1 - ((k + 1) * 0.5) * change_x_by


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
