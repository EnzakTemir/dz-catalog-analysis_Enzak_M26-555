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


def build_report(movies):
    print("ОТЧЕТ АНАЛИТИКИ ПО КАТАЛОГУ ФИЛЬМОВ")
    print(f"Средний рейтинг: {average_rating(movies)}")

    _, _, avg_age = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {avg_age} лет")

    print("\nТоп-3 фильма:")
    for title, rating in top_n_by_rating(movies, 3):
        movie = next(m for m in movies if m["title"] == title)
        print("  " + format_report_line(movie))

    print("\nФильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    for genre, count in sorted(
        genre_counts.items(), key=lambda item: (-item[1], item[0])
    ):
        print(f"  {genre} — {count}")

    print("\nВсе жанры каталога:", ", ".join(sorted(all_genres(movies))))

    print(f"\nФильмов длиннее 120 минут: {count_long_movies(movies)}")
    for movie in movies:
        if movie["duration_min"] > 120:
            print(
                f'  "{normalize_title(movie["title"])}" — '
                f'{movie["duration_min"]} мин'
            )

    print("\nВсе фильмы по убыванию рейтинга:")
    ordered = sorted(movies, key=lambda m: m["rating"], reverse=True)
    for movie in ordered:
        print("   ", format_report_line(movie))

    print("\nТоп по каждому жанру:")
    for genre in sorted(all_genres(movies)):
        genre_movies = [m for m in movies if genre in m["genres"]]
        best = sorted(genre_movies, key=lambda m: m["rating"], reverse=True)[:3]
        print(f"  {genre}:")
        for movie in best:
            print(f"    {format_report_line(movie)}")

    print("\nСредний рейтинг и средняя длительность по жанрам:")
    for genre in sorted(all_genres(movies)):
        genre_movies = [m for m in movies if genre in m["genres"]]
        avg_r = average_rating(genre_movies)
        avg_d = round(
            sum(m["duration_min"] for m in genre_movies) / len(genre_movies)
        )
        print(
            f"  {genre}: рейтинг {avg_r}, "
            f"длительность {duration_in_hours(avg_d)}"
        )

    print("\nТоп-актёры по числу фильмов:")
    filmography = actor_filmography(movies)
    by_count = sorted(
        filmography.items(), key=lambda kv: len(kv[1]), reverse=True
    )
    for actor, titles in by_count:
        print(f"  {actor} — {len(titles)} фильмов")

    print("\nТоп-актёры по среднему рейтингу фильмов:")
    actors_avg = []
    for actor, titles in filmography.items():
        actor_movies = [m for m in movies if m["title"] in titles]
        actors_avg.append((actor, average_rating(actor_movies)))
    actors_avg.sort(key=lambda item: item[1], reverse=True)
    for actor, avg in actors_avg:
        print(f"  {actor} — средний рейтинг {avg}")

    print("\nРаспределение по категориям рейтинга:")
    tiers = {}
    for movie in movies:
        tier = rating_tier(movie["rating"])
        tiers[tier] = tiers.get(tier, 0) + 1
    for tier, count in sorted(
        tiers.items(), key=lambda kv: kv[1], reverse=True
    ):
        print(f"  {tier} — {count}")

    print("\nРаспределение по десятилетним меткам:")
    labels = {}
    for movie in movies:
        label = decade_label(movie["year"])
        labels[label] = labels.get(label, 0) + 1
    for label, count in sorted(
        labels.items(), key=lambda kv: kv[1], reverse=True
    ):
        print(f"  {label} — {count}")

    print("\nРедкие жанры (встречаются 1 раз):")
    rare = {g: c for g, c in genre_counts.items() if c == 1}
    if rare:
        for genre, count in rare.items():
            print(f"  {genre} — {count}")
    else:
        print("  Нет редких жанров")

    print("\nФильмы с рейтингом выше среднего:")
    above = dict_compr(movies)
    for title, rating in sorted(
        above.items(), key=lambda kv: kv[1], reverse=True
    ):
        print(f"  {normalize_title(title)} — {rating}")


if __name__ == "__main__":
    build_report(movies)
