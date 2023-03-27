from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    INPUT = [
        {
            "title": "Web developer",
            "min_salary": "500",
            "max_salary": "800",
            "date_posted": "2021-01-04",
        },
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "1500",
            "date_posted": "2021-01-02",
        },
        {
            "title": "Back end developer",
            "min_salary": "1100",
            "max_salary": "3000",
            "date_posted": "2021-01-01",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2021-01-03",
        },
    ]
    OUTPUT1 = [
        {
            "title": "Web developer",
            "min_salary": "500",
            "max_salary": "800",
            "date_posted": "2021-01-04",
        },
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "1500",
            "date_posted": "2021-01-02",
        },
        {
            "title": "Back end developer",
            "min_salary": "1100",
            "max_salary": "3000",
            "date_posted": "2021-01-01",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2021-01-03",
        },
    ]
    sort_by(INPUT, "min_salary")
    assert INPUT == OUTPUT1
    OUTPUT2 = [
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2021-01-03",
        },
        {
            "title": "Back end developer",
            "min_salary": "1100",
            "max_salary": "3000",
            "date_posted": "2021-01-01",
        },
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "1500",
            "date_posted": "2021-01-02",
        },
        {
            "title": "Web developer",
            "min_salary": "500",
            "max_salary": "800",
            "date_posted": "2021-01-04",
        },
    ]
    sort_by(INPUT, "max_salary")
    assert INPUT == OUTPUT2
    OUTPUT3 = [
        {
            "title": "Web developer",
            "min_salary": "500",
            "max_salary": "800",
            "date_posted": "2021-01-04",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2021-01-03",
        },
        {
            "title": "Front end developer",
            "min_salary": "1000",
            "max_salary": "1500",
            "date_posted": "2021-01-02",
        },
        {
            "title": "Back end developer",
            "min_salary": "1100",
            "max_salary": "3000",
            "date_posted": "2021-01-01",
        },
    ]
    sort_by(INPUT, "date_posted")
    assert INPUT == OUTPUT3
