import random


def main(times: int, win_numbers: list[int], extra: list[int], prizes: list[int]) -> tuple[int, float]:
    """
    Simple program to simulate `Mark Six` lottery.
    :param times: Number of lottery tickets bought. The numbers on each ticket are generated randomly.
    :param win_numbers: The 6 numbers that rolled out from the `Mark Six` machine.
    :param extra: The extra number that rolled out from the `Mark Six` machine.
    :param prizes: List of prizes with the specified amount.
    :return: Total prizes received, Average prizes per lottery ticket.
    """
    i = 0
    progress, percent_progress = 0, int(times / 1000)
    total_prize_ = 0
    print(f"\rProgress: {progress}%", end="")
    while i < times:
        entry_numbers = random.sample(range(0, 50), k=7)
        entry_number, extra_number = entry_numbers[0: 6], entry_numbers[-1]
        entry_number.sort()
        match_numbers, extra_win = 0, True
        for j in range(6):
            if entry_number[j] == win_numbers[j]:
                match_numbers += 1
        if extra_number == extra:
            extra_win = True
        else:
            extra_win = False
        if match_numbers == 6:
            total_prize_ += prizes[0]
        elif match_numbers == 5 and extra_win:
            total_prize_ += prizes[1]
        elif match_numbers == 5:
            total_prize_ += prizes[2]
        elif match_numbers == 4 and extra_win:
            total_prize_ += prizes[3]
        elif match_numbers == 4:
            total_prize_ += prizes[4]
        elif match_numbers == 3 and extra_win:
            total_prize_ += prizes[5]
        elif match_numbers == 3:
            total_prize_ += prizes[6]
        i += 1
        if i % percent_progress == 0:
            progress += 0.1
            print(f"\rProgress: {progress}%", end="")
    return total_prize_, total_prize_ / times


if __name__ == "__main__":
    times = 1_000_000_000  # Arbitrary integer. Determines the number of tickets bought. Larger number makes the estimation more accurate, but it takes more runtime.
    win_numbers, extra = [1, 2, 3, 4, 5, 6], [7]  # The numbers that is rolled out. Change it but make sure `win_number` and `extra` are sorted.
    prizes = [30_000_000, 600_000, 100_000, 9_600, 640, 320, 40]  # Jackpot, second prize and third prize is assumed
    total_prize, average_return = main(times=times, win_numbers=win_numbers, extra=extra, prizes=prizes)
    print(f"\nTrials: {times:,}, Total prize: {total_prize:,}, Average return: {average_return:,}")
