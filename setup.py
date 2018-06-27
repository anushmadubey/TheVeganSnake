import cx_Freeze

executables = [cx_Freeze.Executable("Snake_game.py")]

cx_Freeze.setup(
    name="Snake Game",
    options={"build_exe":{"packages":["pygame"],"include_files":["SnakeHead.png","apple.png"]}},
    description = "Snake Game",
    executables = executables
     
    )
