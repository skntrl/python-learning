from main import clean_and_tokenize


def test_clean_and_tokenize():
    # 1. ARRANE: Create some messy data for the input
    messy_input = "Hello., helLo!, wOrlD!"
    expected_output = ["hello", "hello", "world"]

    # 2. ACT: Run my function the messy_data
    actual_output = clean_and_tokenize(messy_input)

    # 3. ASSERT: Demand that the actual output mactches the expected output
    assert actual_output == expected_output, f"Test Failed! We got: {actual_output}"

    print(f"Test Passed! The function is working perfectly.")


if __name__ == "__main__":
    test_clean_and_tokenize()

