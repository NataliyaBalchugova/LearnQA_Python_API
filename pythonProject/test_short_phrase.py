def test_short_phrase():
    print("Enter a phrase shorter than 15 characters")
    phrase = input("Set a phrase: ")
    assert len(phrase) == 15
    if len(phrase) == 15:
        print("Success")