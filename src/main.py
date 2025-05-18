import file as file
import matrix as matrix
import sys

def main():
    
    if len(sys.argv) < 2:
        print("\nO comando deve ser: python3 main.py <caminho_do_arquivo>\n")
        sys.exit(1)

    file_path = sys.argv[1]
    file.readFile(file_path)
    # file.print_()

    matrix.gerar_combinacoes()
    matrix.resolver_sistemas()
    print("\n")

if __name__ == "__main__":
    main()
