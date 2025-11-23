#This is  a normal candy crash game in python---

import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
screen_width = 400
screen_height = 400
grid_size = 8
tile_size = screen_width // grid_size
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Candy Crush Clone")

# Define a tile
class Tile:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.selected = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x * tile_size, self.y * tile_size, tile_size, tile_size))
        if self.selected:
            pygame.draw.rect(surface, (255, 255, 255), (self.x * tile_size, self.y * tile_size, tile_size, tile_size), 3)

# Create the grid
def create_grid():
    grid = []
    for y in range(grid_size):
        row = []
        for x in range(grid_size):
            row.append(Tile(x, y, random.choice(colors)))
        grid.append(row)
    return grid

# Draw the grid
def draw_grid(grid):
    for row in grid:
        for tile in row:
            tile.draw(screen)

# Check for matches in rows or columns
def check_matches(grid):
    matched = []
    
    # Check rows
    for y in range(grid_size):
        for x in range(grid_size - 2):
            if grid[y][x].color == grid[y][x+1].color == grid[y][x+2].color:
                matched.extend([grid[y][x], grid[y][x+1], grid[y][x+2]])

    # Check columns
    for x in range(grid_size):
        for y in range(grid_size - 2):
            if grid[y][x].color == grid[y+1][x].color == grid[y+2][x].color:
                matched.extend([grid[y][x], grid[y+1][x], grid[y+2][x]])

    return matched

# Remove matched tiles and fill the grid with new tiles
def remove_matches(grid, matched):
    for tile in matched:
        tile.color = random.choice(colors)

# Main game loop
def game_loop():
    grid = create_grid()
    selected_tile = None
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x //= tile_size
                y //= tile_size

                if selected_tile is None:
                    selected_tile = grid[y][x]
                    selected_tile.selected = True
                else:
                    selected_tile.selected = False
                    if abs(selected_tile.x - x) + abs(selected_tile.y - y) == 1:
                        # Swap the tiles
                        grid[y][x], grid[selected_tile.y][selected_tile.x] = grid[selected_tile.y][selected_tile.x], grid[y][x]
                        
                        # Check for matches
                        matched = check_matches(grid)
                        if matched:
                            remove_matches(grid, matched)
                        else:
                            # Swap back if no match
                            grid[y][x], grid[selected_tile.y][selected_tile.x] = grid[selected_tile.y][selected_tile.x], grid[y][x]

                    selected_tile = None

        # Draw the grid
        draw_grid(grid)
        pygame.display.update()

        # Limit the frame rate
        clock.tick(30)

    pygame.quit()

# Start the game
game_loop()
