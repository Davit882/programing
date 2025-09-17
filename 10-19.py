from collections import Counter  # Բացակայող ներմուծում

def amenashat_nish_bare(sentence):
    words = sentence.split()
    max_word = max(words, key=len)
    return max_word

sentence = "Ծիրանենիի ծաղկունքը հրաշալ"
print(amenashat_nish_bare(sentence))


def amenashat_ogtagorcvox_tar(nakhad):
    only_letters = [char.lower() for char in nakhad if char.isalpha()]
    if not only_letters:
        return None
    count = Counter(only_letters)
    most_common = count.most_common(1)[0]
    return most_common

nakhad = "Ծիրանենի ծաղկունքը հրաշալի տեսարան է"
result = amenashat_ogtagorcvox_tar(nakhad)

if result:
    tar, qanak = result
    print("Ամենաշատ օգտագործված տառն է՝ '{}', որը հանդիպել է {} անգամ։".format(tar, qanak))
else:
    print("Տառեր չեն գտնվել։")


def erkar_bari_amenashat_tar(nakhad):
    words = nakhad.split()
    if not words:
        return None

    longest_word = max(words, key=len)
    cleaned_word = ''.join([ch.lower() for ch in longest_word if ch.isalpha()])

    if not cleaned_word:
        return None

    count = Counter(cleaned_word)
    most_common = count.most_common(1)[0]
    return most_common[0]

sentence = "Ծիրանենի ծաղկունքը հրաշալի տեսարան է"
result = erkar_bari_amenashat_tar(sentence)

print("Ամենաշատ օգտագործված տառը ամենաերկար բառում՝", result)


def edge_elements(s: str, n: int):
    if n <= 0 or n > len(s):
        return None
    return s[n - 1], s[-n]

print(edge_elements("HelloWorld", 1))  # ('H', 'd')
print(edge_elements("HelloWorld", 3))  # ('l', 'r')


def is_palindrome(num: int) -> bool:
    s = str(num)
    return s == s[::-1]

print(is_palindrome(121))    # True
print(is_palindrome(12321))  # True
print(is_palindrome(123))    # False


def is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]

def nearest_palindrome(num: int) -> int:
    if is_palindrome(num):
        return num

    lower = num - 1
    upper = num + 1

    while True:
        if lower >= 0 and is_palindrome(lower):
            return lower
        if is_palindrome(upper):
            return upper
        lower -= 1
        upper += 1

print(nearest_palindrome(121))   # 121
print(nearest_palindrome(123))   # 121
print(nearest_palindrome(99))    # 99
print(nearest_palindrome(10))    # 9
print(nearest_palindrome(88))    # 88


def product_first_last(num: int) -> int:
    s = str(abs(num))
    if len(s) == 1:
        d = int(s[0])
        return d * d
    first = int(s[0])
    last = int(s[-1])
    return first * last

print(product_first_last(1234))   # 4
print(product_first_last(5069))   # 45
print(product_first_last(7))      # 49
print(product_first_last(-987))   # 63


def count_strings(lst: list) -> int:
    return sum(1 for item in lst if isinstance(item, str))

print(count_strings([1, "hello", 3, "world", True]))   # 2
print(count_strings(["a", "b", "c"]))                  # 3
print(count_strings([10, 20, 30]))                     # 0


from typing import Union

def max_number(lst: list) -> Union[int, float, None]:
    if not lst:
        return None
    return max(lst)

numbers = [3, 5.7, 2, 9, 4.2]
result = max_number(numbers)
print("Max number is:", result)

