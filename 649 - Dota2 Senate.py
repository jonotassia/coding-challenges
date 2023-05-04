from collections import Counter, deque


def predictPartyVictory(senate: str) -> str:
    # Queue approach
    r_queue: deque = deque()
    d_queue: deque = deque()

    # Fill the two queues based on the letters in the senate string
    for i, senator in enumerate(senate):
        if senator == "R":
            r_queue.append(i)
        else:
            d_queue.append(i)

    # Dequeue from the queue until one of the queues is empty
    while r_queue and d_queue:
        r_memb, d_memb = r_queue.popleft(), d_queue.popleft()

        # If r_memb has a smaller value than d_memb (ie are an earlier position in the committee), add a new
        # member back to the end of the list to preserve its length
        if r_memb < d_memb:
            r_queue.append(r_memb + len(senate))
        else:
            d_queue.append(d_memb + len(senate))

    return "Radiant" if r_queue else "Dire"

    # Naive approach (counter and lists)
    # r_bans: int = 0
    # d_bans: int = 0
    #
    # active_list: list[bool] = [True] * len(senate)
    #
    # member_count = Counter(senate)
    #
    # while member_count["R"] and member_count["D"]:
    #     for i, senator in enumerate(senate):
    #         if not active_list[i]:
    #             continue
    #
    #         # Simulate Radiant party voting
    #         if senator == "R":
    #             # If there is a ban available, ban this member
    #             if r_bans:
    #                 active_list[i] = False
    #                 r_bans -= 1
    #                 member_count["R"] -= 1
    #             else:
    #                 d_bans += 1
    #
    #         # Simulate Dire party voting
    #         else:
    #             if d_bans:
    #                 active_list[i] = False
    #                 d_bans -= 1
    #                 member_count["D"] -= 1
    #             else:
    #                 r_bans += 1
    #
    # return "Radiant" if member_count["R"] else "Dire"

predictPartyVictory("RDD")
