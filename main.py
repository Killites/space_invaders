import turtle
import random

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# ---------------- PLAYER ----------------
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.setheading(90)
player.goto(0, -250)

def move_left():
    x = player.xcor()
    if x > -280:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 280:
        player.setx(x + 20)

# ---------------- BULLET ----------------
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.penup()
bullet.shapesize(stretch_wid=0.2, stretch_len=0.8)
bullet.hideturtle()

bullet_state = "ready"

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

def move_bullet():
    global bullet_state
    if bullet_state == "fire":
        bullet.sety(bullet.ycor() + 20)
        if bullet.ycor() > 300:
            bullet.hideturtle()
            bullet_state = "ready"

# ---------------- ENEMIES ----------------
enemies = []

for _ in range(5):
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.goto(random.randint(-200, 200), random.randint(100, 250))
    enemies.append(enemy)

def move_enemies():
    for enemy in enemies:
        enemy.sety(enemy.ycor() - 2)

# ---------------- COLLISION ----------------
def is_collision(t1, t2):
    return t1.distance(t2) < 20

# ---------------- GAME OVER TEXT ----------------
game_over_text = turtle.Turtle()
game_over_text.hideturtle()
game_over_text.color("white")
game_over_text.penup()

# ---------------- CONTROLS ----------------
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(fire_bullet, "space")

# ---------------- GAME LOOP ----------------
game_on = True

def game_loop():
    global game_on, bullet_state

    if game_on:
        move_bullet()
        move_enemies()

        for enemy in enemies:

            # Bullet hits enemy
            if is_collision(bullet, enemy):
                enemy.goto(random.randint(-200, 200), random.randint(100, 250))
                bullet.hideturtle()
                bullet_state = "ready"

            # Enemy hits player
            if is_collision(enemy, player):
                game_over_text.goto(0, 0)
                game_over_text.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
                game_on = False

        screen.update()
        screen.ontimer(game_loop, 20)

game_loop()
screen.mainloop()