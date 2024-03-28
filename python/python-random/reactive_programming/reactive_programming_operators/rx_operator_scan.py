import rx
from rx import operators as op


def main():
    # Rolling sum
    source = rx.from_([2, 4, 6, 8]).pipe(
        op.scan(lambda sub_total, i: sub_total + i)
    )

    source.subscribe(lambda v: print(v))


if __name__ == "__main__":
    main()
