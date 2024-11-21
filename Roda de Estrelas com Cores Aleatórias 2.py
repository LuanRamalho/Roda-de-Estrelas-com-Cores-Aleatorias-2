import tkinter as tk
import random
import math

# Função para gerar uma estrela
def draw_star(canvas, x, y, size, color):
    points = []
    for i in range(10):  # Alternar entre os vértices maiores e menores
        angle = math.radians(i * 36)  # Cada ponto está a 36 graus
        length = size if i % 2 == 0 else size / 2
        px = x + length * math.cos(angle)
        py = y - length * math.sin(angle)
        points.append((px, py))
    # Converter os pontos em uma lista de coordenadas para o tkinter
    flat_points = [coord for point in points for coord in point]
    canvas.create_polygon(flat_points, fill=color, outline="black")

# Função para gerar uma roda de estrelas
def draw_star_wheel(canvas, center_x, center_y, radius, star_size, num_stars):
    for i in range(num_stars):
        angle = math.radians(i * (360 / num_stars))
        x = center_x + radius * math.cos(angle)
        y = center_y - radius * math.sin(angle)
        color = random_color()
        draw_star(canvas, x, y, star_size, color)

# Função para gerar uma cor aleatória
def random_color():
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

# Configuração principal do programa
def main():
    root = tk.Tk()
    root.title("Roda de Estrelas")
    
    canvas_width = 800
    canvas_height = 800
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()
    
    center_x, center_y = canvas_width // 2, canvas_height // 2
    radius = 250
    star_size = 50
    num_stars = 12  # Número de estrelas na roda

    draw_star_wheel(canvas, center_x, center_y, radius, star_size, num_stars)
    
    root.mainloop()

if __name__ == "__main__":
    main()
