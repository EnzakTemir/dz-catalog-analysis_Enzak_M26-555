import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},  # noqa: E501
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


def rating_tier(rating):
    if rating >= 7:
        tier = "шедевр" if rating >= 9 else "хорошо"
    elif rating >= 5:
        tier = "средне"
    else:
        tier = "слабо"
    return tier


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def no_comedy(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies):
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    words = title.split()
    normalized = [word[0].upper() + word[1:] for word in words]
    return " ".join(normalized)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


def titles_sorted_by_rating(movies):
    ordered = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [movie["title"] for movie in ordered]


def top_n_by_rating(movies, n=3):
    ordered = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in ordered[:n]]


def count_by_genre(movies):
    result = {}
    for movie in movies:
        for genre in movie["genres"]:
            result[genre] = result.get(genre, 0) + 1
    return result


def actor_filmography(movies):
    result = {}
    for movie in movies:
        for actor in movie["actors"]:
            result.setdefault(actor, []).append(movie["title"])
    return result


def dict_compr(movies):
    avg = average_rating(movies)
    return {movie["title"]: movie["rating"] for movie in movies if movie["rating"] > avg}  # noqa: E501


def all_genres(movies):
    result = set()
    for movie in movies:
        result.update(movie["genres"])
    return result


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    genres_a = set()
    for movie in movies_a:
        genres_a.update(movie["genres"])
    genres_b = set()
    for movie in movies_b:
        genres_b.update(movie["genres"])
    return genres_a - genres_b


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


if __name__ == "__main__":
    print("Средняя оценка:", average_rating(movies))
    print("Статистика по возрасту:", catalog_age_stats(movies))
    print("Длительность первого фильма:", duration_in_hours(movies[0]["duration_min"]))
    
    
    print("_______________________")
    for movie in movies:
        print(
            movie["title"],
            " ",
            movie["rating"],
            "=",
            rating_tier(movie["rating"]),
            "and",
            movie["year"],
            "=",
            decade_label(movie["year"]),
        )


    print("_______________________")
    print("Не комедии:")
    no_comedy(movies)
    

    print("_______________________")
    print("Первый шедевр:")
    find_first_masterpiece(movies)


    print("_______________________")
    print("Фильмов длиннее 120 минут:", count_long_movies(movies))


    print("_______________________")
    print("normalize_title:", normalize_title("silent hours"))
    print("make_slug:", make_slug("Silent Hours"))
    print("format_report_line:", format_report_line(movies[7]))


    print("_______________________")
    print("titles_sorted_by_rating:")
    for title in titles_sorted_by_rating(movies):
        print(" ", title)


    print("_______________________")
    print("top_n_by_rating:", top_n_by_rating(movies, 3))


    print("_______________________")
    print("count_by_genre:", count_by_genre(movies))


    print("_______________________")
    print("actor_filmography:", actor_filmography(movies))


    print("_______________________")
    print("dict_compr:", dict_compr(movies))


    print("_______________________")
    print("all_genres:", all_genres(movies))


    print("_______________________")
    print("common_actors:", common_actors(movies[0], movies[3]))


    print("_______________________")
    print("genres_only_in_one:", genres_only_in_one(movies[5:6], movies[:5]))


    print("_______________________")
    print("iter_high_rated:")
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))


    print("_______________________")
    print("Суммарная длительность фильмов с рейтингом выше 7:",
          sum(m["duration_min"] for m in movies if m["rating"] > 7))