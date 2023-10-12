def get_position(N):
    x, y, x_direction, y_direction, step_counter, current_step = 0, 0, 1, 1, 1, 0

    for k in range(1, N + 1):
        x_direction = -x_direction
        for i in range(step_counter):
            x += x_direction
            current_step += 1
            if current_step >= N:
                return (x, y)
        y_direction = -y_direction
        for i in range(step_counter):
            y += y_direction
            current_step += 1
            if current_step >= N:
                return (x, y)

        step_counter += 1
    return (0, 0)

N = int(input())
position = get_position(N)
print(position)
