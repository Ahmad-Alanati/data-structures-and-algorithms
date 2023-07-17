import pytest
from object_comparison import Movie, sort_by_title, most_recent_movies

list_movies = [Movie("Transformers: Rise of the Beasts", 2023, ["str1", "str2", "str3"]),
               Movie("A Good Day to Die Hard", 2013, ["str1", "str2", "str3"]),
               Movie("Fast X", 2023, ["str1", "str2", "str3"]),
               Movie("The Conjuring: The Devil Made Me Do It",2021, ["str1", "str2", "str3"]),
               Movie("Sound of Freedom", 2023, ["str1", "str2", "str3"]),
               Movie("San Andreas", 2015, ["str1", "str2", "str3"]),
               Movie("The Out-Laws", 2023, ["str1", "str2", "str3"]),
               Movie("John Wick: Chapter 4", 2023, ["str1", "str2", "str3"]),
               Movie("The Super Mario Bros. Movie",2023, ["str1", "str2", "str3"]),
               Movie("The Darkest Minds", 2018, ["str1", "str2", "str3"]),
               Movie("Insidious: The Last Key",2018, ["str1", "str2", "str3"]),
               ]


def test_object_sorting_by_years_one():
    actual = most_recent_movies(list_movies)
    expected = [list_movies[0],
               list_movies[2],
               list_movies[4],
               list_movies[6],
               list_movies[7],
               list_movies[8],
               list_movies[3],
               list_movies[9],
               list_movies[10],
               list_movies[5],
               list_movies[1],
               ]
    assert actual == expected


def test_object_sorting_by_title_one():
    actual = sort_by_title(list_movies)
    expected = [list_movies[3],
                list_movies[9],
                list_movies[2],
                list_movies[1],
                list_movies[10],
                list_movies[7],
                list_movies[6],
                list_movies[5],
                list_movies[4],
                list_movies[8],
                list_movies[0],
               ]
    assert actual == expected