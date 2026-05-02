import turtle


def koch_curve(t: turtle.Turtle, order: int, size: float) -> None:
    if order == 0:
        t.forward(size)
    else:
        # Кожен відрізок замінюємо чотирма меншими частинами кривої Коха.
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order: int, size: float = 300) -> None:
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Koch Snowflake")

    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Сніжинка складається з трьох кривих Коха, повернутих на 120 градусів.
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


def main() -> None:
    try:
        order = int(input("Введіть рівень рекурсії: "))

        if order < 0:
            print("Рівень рекурсії має бути невідʼємним числом.")
            return

        draw_koch_snowflake(order)

    except ValueError:
        print("Потрібно ввести ціле число.")


if __name__ == "__main__":
    main()