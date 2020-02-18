from PIL import Image

def main():
    print("Enter file path:")
    img = Image.open(input().strip(), 'r')
    
    print(dir(img))


if __name__ == "__main__":
    main()