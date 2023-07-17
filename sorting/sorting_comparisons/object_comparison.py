import re

class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

    def __str__(self):
        return f"title: {self.title}, release date: {self.year}"


def most_recent_movies(list_movies):
    length = len(list_movies)
    if length == 1:
        return list_movies

    mid = int(length/2)
    left = list_movies[:mid]
    right = list_movies[mid:]
    left = most_recent_movies(left)
    right = most_recent_movies(right)
    sorted_array = []
    merge_years(left, right, sorted_array)
    return sorted_array


def merge_years(left, right, array):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i].year >= right[j].year:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1
        k += 1

    if i == len(left):
        while j != len(right):
            array.append(right[j])
            j += 1
    else:
        while i != len(left):
            array.append(left[i])
            i += 1


def sort_by_title(list_movies):
    length = len(list_movies)
    if length == 1:
        return list_movies
    
    mid = int(length/2)
    left = list_movies[:mid]
    right = list_movies[mid:]
    left = sort_by_title(left)
    right = sort_by_title(right)
    sorted_array = []
    merge_title(left, right, sorted_array)
    return sorted_array

def merge_title(left, right, array):
    i = j = k = 0
    pattern = r'^(A|An|The)\s'
    left[i].title >= right[j].title
    while i < len(left) and j < len(right):
        if re.sub(pattern, '', left[i].title, flags=re.IGNORECASE)<=re.sub(pattern, '', right[j].title, flags=re.IGNORECASE):
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1
        k += 1

    if i == len(left):
        while j != len(right):
            array.append(right[j])
            j += 1
    else:
        while i != len(left):
            array.append(left[i])
            i += 1


if __name__ == "__main__":
    list_movies = [Movie("Transformers: Rise of the Beasts", 2023, ["str1", "str2", "str3"]),
                   Movie("A Good Day to Die Hard", 2013, ["str1", "str2", "str3"]),
                   Movie("Fast X", 2023, ["str1", "str2", "str3"]),
                   Movie("The Conjuring: The Devil Made Me Do It", 2021, ["str1", "str2", "str3"]),
                   Movie("Sound of Freedom", 2023, ["str1", "str2", "str3"]),
                   Movie("San Andreas", 2015, ["str1", "str2", "str3"]),
                   Movie("The Out-Laws", 2023, ["str1", "str2", "str3"]),
                   Movie("John Wick: Chapter 4", 2023, ["str1", "str2", "str3"]),
                   Movie("The Super Mario Bros. Movie", 2023, ["str1", "str2", "str3"]),
                   Movie("The Darkest Minds", 2018, ["str1", "str2", "str3"]),
                   Movie("Insidious: The Last Key", 2018, ["str1", "str2", "str3"]),
                   ]
    # for movie in most_recent_movies(list_movies):
    #     print(str(movie))
    for movie in sort_by_title(list_movies):
        print(str(movie))

    
