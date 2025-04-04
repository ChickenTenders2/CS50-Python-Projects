def convert(response):
    new_response = response.replace(":)", "🙂").replace(":(", "🙁")
    return new_response

def main():
    response = input()
    new_response = convert(response)
    print(new_response)

main()
