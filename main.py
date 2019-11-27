import sys
from statistics import mean

def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")

    # TODO: Fill in the actual logic here!
    with open(input_file_path, "r") as f:
       for line in f:
           line = line.strip("\n")
           to_calc = line.split(",")
           num_list = []
           for n in to_calc:
               num_list.append(float(n))
           av = mean(num_list)
           print(f"{av}")


if __name__ == "__main__":
    main()
