import curses
import random
import time

# Initial settings for the game
def initialize_game(screen):
    curses.curs_set(0)  # Hide the cursor
    screen.timeout(100)  # Set the delay between screen updates
    screen.keypad(1)  # Enable keypad mode
    height, width = screen.getmaxyx()  # Get the size of the terminal window
    
    # Initialize snake
    snake = [(height // 2, width // 2 + i) for i in range(3)]  # Initial snake length of 3 units
    direction = curses.KEY_RIGHT  # Initial direction of the snake
    
    # Generate obstacles
    num_obstacles = int((height * width) * 0.05) // 5  # Obstacles take up 5% of the screen
    obstacles = []
    for _ in range(num_obstacles):
        is_vertical = random.choice([True, False])
        if is_vertical:
            start_y = random.randint(1, height - 6)
            start_x = random.randint(1, width - 2)
            for i in range(5):
                obstacles.append((start_y + i, start_x))
        else:
            start_y = random.randint(1, height - 2)
            start_x = random.randint(1, width - 6)
            for i in range(5):
                obstacles.append((start_y, start_x + i))

    # Generate initial food
    food = generate_food(snake, obstacles, height, width)
    special_food = generate_food(snake, obstacles, height, width, special=True)

    return snake, direction, food, special_food, obstacles, 0, 0  # Normal food count, Special food count

def generate_food(snake, obstacles, height, width, special=False):
    while True:
        food = (random.randint(1, height - 2), random.randint(1, width - 2))
        if food not in snake and food not in obstacles:
            return food if not special else ('X', food)

def main(screen):
    snake, direction, food, special_food, obstacles, normal_count, special_count = initialize_game(screen)
    paused = False

    while True:
        next_key = screen.getch()

        if next_key == ord(' '):  # Pause and resume the game
            paused = not paused
            screen.timeout(100 if not paused else -1)
            continue
        
        if not paused:
            if next_key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
                direction = next_key  # Change direction based on user input

            head = snake[0]
            if direction == curses.KEY_RIGHT:
                new_head = (head[0], head[1] + 1)
            elif direction == curses.KEY_LEFT:
                new_head = (head[0], head[1] - 1)
            elif direction == curses.KEY_UP:
                new_head = (head[0] - 1, head[1])
            elif direction == curses.KEY_DOWN:
                new_head = (head[0] + 1, head[1])
            
            # Wrap around the screen boundaries
            new_head = ((new_head[0] + height) % height, (new_head[1] + width) % width)
            
            # Check for collision with itself or obstacles
            if new_head in snake or new_head in obstacles:
                reason = "obstacles" if new_head in obstacles else "itself"
                game_over(screen, normal_count, special_count, reason)
                break

            snake.insert(0, new_head)
            
            if new_head == food:
                normal_count += 1
                food = generate_food(snake, obstacles, height, width)
            elif new_head == special_food[1]:
                special_count += 1
                if len(snake) > 1:
                    snake.pop()
                special_food = generate_food(snake, obstacles, height, width, special=True)
            else:
                snake.pop()
            
            screen.clear()
            screen.addch(food[0], food[1], 'π')
            screen.addch(special_food[1][0], special_food[1][1], 'X')
            for y, x in snake:
                screen.addch(y, x, 'O')
            for y, x in obstacles:
                screen.addch(y, x, '#')
            screen.refresh()

        time.sleep(0.1)  # Slow down the game loop

def game_over(screen, normal_count, special_count, reason):
    screen.clear()
    message = f"Game over. The snake collided with {reason}. You ate {normal_count} normal food and {special_count} special food."
    screen.addstr(0, 0, message)
    screen.refresh()
    time.sleep(3)

curses.wrapper(main)

#Hello TAs <3!Here are my prompt for ChatGPT. I rearranged the requirements in the pdf file!

#Hi, I want to design and implement a console-based text version of the Snake game in Python. Firstly, the snake is moving toward the right, but it can be controlled by the arrow keys by the user, and it can wrap around the screen boundaries. The snake will grow when it eats normal food. The game ends if the snake collides with itself or any obstacles. 
#The instructions are below.

#Initial setting of the game
#(1)The game screen should be initialized according to the size of the terminal window. 
#(2) Obstacles, represented by inverted color cells, should take up 5% of the game screen. Each obstacle should consist of at least 5 consecutive cells, arranged either horizontally or vertically. 
#These obstacles should be generated at random positions at the start of the game.
#(3)The initial snake is three units long.
#(4)The player should be able to pause and resume the game by pressing the whitespace.

#About food for the snake
#(1)Normal food: represented by π. When eating normal food, snake grows by 1 unit.
#(2)Special food: represented by X. When eating special food, snake shrinks by 1 unit. However, the snake cannot shrink if its length is less than or equal to 1.
#(3)Both types of food should be generated at random positions on the game screen. When a food is eaten, another one should be generated immediately.

#Movement of the snake
#(1)Initial snake moves towards the right.
#(2)When moving the snake by the arrow keys, the movement would accelerate a little bit each time the user trying to change its moving direction.
#(3)The snake’s movement is allowed to wrap around the screen boundaries. That said, when the snake hits the bottom/up boundary, it can move out from the up/bottom boundary. When the snake hits the left/right boundary, it can move out from the right/left boundary. 
#Its path is wrapping around a rectangle, to be short.

#Ending the game
#At the end of the game, the program should display:
#a. the number of normal and special foods eaten
#b. the reason why the game ended:by hitting the walls or hitting the obstacles.
#Message example:"Game over. You collided by hitting the wall. You ate 3 normal food and 1 special food."
#"Game over. You collided by hitting the obstacles. You ate 3 normal food and 1 special food."
