import subprocess
import os
import time

command = "cls" if os.name == "nt" else "clear"


def clear_console():
    subprocess.run(command, shell=True)

def draw_benin_flag():
    # --- 1. Флаг Бенина ---
    GREEN = "\033[42m"
    YELLOW = "\033[43m"
    RED = "\033[41m"
    RESET = "\033[0m"
    
    for i in range(3):
        print(f"{GREEN}        {YELLOW}            {RESET}")
    for i in range(3):
        print(f"{GREEN}        {RED}            {RESET}")
    print()

def draw_pattern():
    # --- 2. Узор ---
    pattern = [
        "  *    *  ",
        " ***  *** ",
        "**********",
        " ***  *** ",
        "  *    *  "
    ]
    for i in pattern:
        print(i)

def process_sequence():
    # --- 3. Диаграмма по файлу sequence.txt ---

    

            
    num_group1 = 0
    num_group2 = 0
    
    with open("sequence.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                val = float(line)
                if 0 <= val <= 5:
                    num_group1 += 1
                elif -5 <= val < 0:
                    num_group2 += 1
            except ValueError:
                continue
                
    total = num_group1 + num_group2
    if total == 0:
        total = 1
        
    p1 = (num_group1 / total) * 100
    p2 = (num_group2 / total) * 100
    
    print(f"Подходящих чисел всего: {total}")
    print(f"Группа 1 (0 до 5): {num_group1} ({p1:.1f}%)")
    print(f"Группа 2 (0 до -5): {num_group2} ({p2:.1f}%)")
    
    bar_length = 40
    len1 = int(bar_length * (p1 / 100))
    len2 = bar_length - len1
    
    print(f"\nДиаграмма соотношения:")
    print(f"\033[44m{' ' * len1}\033[45m{' ' * len2}\033[0m")
    print(f"\033[34m■\033[0m Группа 1 (0..5)   \033[35m■\033[0m Группа 2 (-5..0)\n")

def draw_function_graph():
    # --- Допзадание ---
    height = 10
    width = 22
    
    grid = [[" " for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        grid[y][0] = "│"
    for x in range(width):
        grid[height-1][x] = "─"
    grid[height-1][0] = "└"
    
    for x_val in range(6):
        y_val = x_val + 1
        x_char = x_val * 3 + 1
        y_char = (height - 1) - y_val
        
        if 0 <= y_char < height and x_char < width:
            grid[y_char][x_char] = "x"
            
    graph_output = ""
    for row in grid:
        graph_output += "".join(row) + "\n"
        
    print(graph_output)

def run_animation():
    frames = [
        ["   O   ", "  /|\\  ", "  / \\  "],
        ["  \\O/  ", "   |   ", "  / \\  "],
        ["   O   ", "  /|/  ", "  / \\  "],
        ["       ", "   O   ", "  /|\\  "]
    ]
    
    print("Запуск анимации...")
    time.sleep(1)
    
    for _ in range(5):
        for frame in frames:
            clear_console()
            print("\n" * 3)
            for line in frame:
                print("   " + line)
            time.sleep(0.35)
            
    clear_console()


draw_benin_flag()
input("нажмите любую клавишу для продолжения")
draw_pattern()
input("нажмите любую клавишу для продолжения")
process_sequence()
input("нажмите любую клавишу для продолжения")
draw_function_graph()

input("Нажмите Enter, чтобы запустить анимацию человечка...")
run_animation()

draw_benin_flag()
draw_pattern()
process_sequence()
draw_function_graph()
print("Работа программы завершена.")