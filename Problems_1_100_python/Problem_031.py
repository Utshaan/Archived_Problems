import time

t = time.time()
l = [[0, 0, 0, 0, 0, 0, 0, 1]]
for g in range(3):
    for f in range(1 + (200 - g * 100) // 50):
        for e in range(1 + (200 - g * 100 - f * 50) // 20):
            for d in range(1 + (200 - g * 100 - f * 50 - e * 20) // 10):
                for c in range(1 + (200 - 100 * g - 50 * f - 20 * e - 10 * d) // 5):
                    for b in range(
                        1 + (200 - 100 * g - 50 * f - 20 * e - 10 * d - 5 * c) // 2
                    ):
                        for a in range(
                            1
                            + (200 - 100 * g - 50 * f - 20 * e - 10 * d - 5 * c - 2 * b)
                        ):
                            if (
                                a + b * 2 + c * 5 + d * 10 + e * 20 + f * 50 + g * 100
                            ) == 200:
                                l.append([a, b, c, d, e, f, g, 0])
print(f"{len(l)} , time taken - {time.time() - t}")
