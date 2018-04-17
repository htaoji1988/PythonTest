def content_formate(file_path):
    with open(file_path, 'r') as content:
        line_list = (content.read().split(","))
        return line_list


def get_url(content):
    for i in content:
        url = i.split('\"')[5]
        print(url)


if __name__ == "__main__":
    file = "/Users/tt/Downloads/test.txt"
    get_url(content_formate(file))
