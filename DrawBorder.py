"""
def special_draw_2d(n , m , border , fill):
    print(m * border)
    for i in range(n):
        print(border + ((m-2) * fill) + border)
    print(m * border)
"""
def a(n, m, border, fill):
    fill_line = border + ((m-2) * fill) + border
    border_line = border * m
    for num in range(n):
        if num == 0 or num == n - 1:
            print(border_line)
        else:
            print(fill_line)

            
