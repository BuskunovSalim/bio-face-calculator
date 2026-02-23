from decimal import Decimal
from random import randint
from pandas import DataFrame, read_csv

def generate_sample():
    result = []
    
    for __ in range(10000):
        data = tuple(
            randint(1, 1000) / 100
            for _ in range(12)
        )
        result.append(data)
    df = DataFrame(result)
    df.to_csv("file.csv", index=False, header=False, sep=";")


def front_ratio_index_1(mandibula: tuple[Decimal, ...], maxilla: tuple[Decimal, ...]) -> Decimal:
    if len(mandibula) != 6 or len(maxilla) != 6:
        raise ValueError("Передано неверное количество ширин зубов. Нужно передавать 6 ширин зубов для каждой челюсти.")
    sum_maxilla = sum(maxilla)
    sum_mandibula = sum(mandibula)
    return Decimal(round(sum_mandibula / sum_maxilla * 100, 3))

def from_csv():
    data = read_csv("file.csv", sep=";", header=None)
    rows = data.to_records(index=False)
    result = list(
        tuple(i for i in row)
        for row in rows
    )
    return result

def main():
    data = from_csv()
    result_data = []
    headers = (
        "Верхний зуб 1",
        "Верхний зуб 2",
        "Верхний зуб 3",
        "Верхний зуб 4",
        "Верхний зуб 5",
        "Верхний зуб 6",
        "Нижний зуб 1",
        "Нижний зуб 2",
        "Нижний зуб 3",
        "Нижний зуб 4",
        "Нижний зуб 5",
        "Нижний зуб 6",
        "Индекс 1",
    )
    for row in data:
        mandibula_raw, maxilla_raw = row[:6], row[6:]
        mandibula = tuple(
            Decimal(num)
            for num in mandibula_raw
        )
        maxilla = tuple(
            Decimal(num)
            for num in maxilla_raw
        )
        result = front_ratio_index_1(maxilla=maxilla, mandibula=mandibula)
        final_row = {
            headers[index]: person
            for index, person in enumerate([*row, result])
        }
        print(final_row)
        result_data.append(final_row)
    result_df = DataFrame(result_data)
    result_df.to_csv("result.csv", index=False, sep=";")
    


if __name__ == "__main__":
    main()
