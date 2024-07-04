def convert(user_input):
    output = user_input.replace(":)", "🙂").replace(":(","🙁")
    return output
def main():

    user_input = input("please enter some input:")
    output = convert(user_input)
    print(output)



main()
