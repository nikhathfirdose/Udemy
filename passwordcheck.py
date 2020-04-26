import requests
import hashlib
import sys


def callApi(char):
    url = "https://api.pwnedpasswords.com/range/" + char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"you havnet entered the right url, the response code is {res.status_code} plese check!")
    return res


def checkPassword(allhashes, mytail):
    allhashes = (line.split(':') for line in allhashes.text.splitlines())
    for h, count in allhashes:
        if h == mytail:
            return count
    return 0


def hashedPassword(password):
    sha1pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5, rest = sha1pass[:5], sha1pass[5:]
    result = callApi(first5)
    return checkPassword(result, rest)


def main(args):
    for password in args:
        count = hashedPassword(password)
        if count:
            print(
                f"{password} exits, used {count} times, probably you wanna change it!")
        else:
            print(f"No usage even once, go ahead it is a strong password")
    return "done"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
