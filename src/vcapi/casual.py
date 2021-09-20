import vcapi.data as data
from argparse import ArgumentParser
from time import sleep


def main():
    parser = ArgumentParser(description="casual-query")
    parser.add_argument("output", default="./servers.json")
    parser.set_defaults(output="./servers.json")

    args = parser.parse_args()
    output_file = args.output

    while True:
        with open(output_file, 'w') as output_fp:
            print("Generating Listing")
            data.dump_listing_to_file(output_fp)
            print("Done")
        sleep(60)


if __name__ == "__main__":
    main()