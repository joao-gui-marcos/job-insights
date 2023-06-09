from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_dict = read(path)
    jobs_dict_with_only_salary = [
        {"max_salary": d["max_salary"]}
        for d in jobs_dict
        if d["max_salary"].isdigit()
    ]
    # jobs_salary_list = []
    # for d in jobs_dict_with_only_salary:
    #     try:
    #         salary = int(d["max_salary"])
    #         jobs_salary_list.append(salary)
    #     except ValueError:
    #         pass
    jobs_salary_list = [
        int(d["max_salary"])
        for d in jobs_dict_with_only_salary  # se n converter pra int falha
    ]
    print(max(jobs_salary_list))
    return max(jobs_salary_list)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_dict = read(path)
    jobs_dict_with_only_salary = [
        {"min_salary": d["min_salary"]}
        for d in jobs_dict
        if d["min_salary"].isdigit()
    ]
    jobs_salary_list = [
        int(d["min_salary"])
        for d in jobs_dict_with_only_salary  # se n converter pra int falha
    ]
    print(min(jobs_salary_list))
    return min(jobs_salary_list)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
