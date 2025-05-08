import file
import matrix
import sys

def main():
    
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <caminho_do_arquivo>")
        sys.exit(1)

    file_path = sys.argv[1]
    file.readFile(file_path)
    # file.print_()

    matrix.generate_combinations()
    matrix.resolver_sistemas()
    print("\n")

if __name__ == "__main__":
    main()
