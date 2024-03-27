import rx


def main():
    source1 = rx.from_list([2, 4, 6, 8])
    source2 = rx.from_list([1, 3, 5, 7, 9])
    source3 = rx.merge(source1, source2).subscribe(lambda v: print(v, end=' '))


if __name__ == "__main__":
    main()
