def bulbSwitch(n: int) -> int:
    # One-liner
    return int(sqrt(n))

    # Naive approach
    # bulb_dict: dict = {n+1: 0 for n in range(n)}
    # on_count: int = 0
    #
    # step: int = 1
    #
    # while step <= n:
    #     for i in range(step, n+1, step):
    #         if not bulb_dict[i]:
    #             bulb_dict[i] = 1
    #             on_count += 1
    #         else:
    #             bulb_dict[i] = 0
    #             on_count -= 1
    #     step += 1
    #
    # return on_count

bulbSwitch(9999999)