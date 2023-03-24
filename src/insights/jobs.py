from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents
    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """

    with open(path, encoding="utf-8") as file:
        content = csv.reader(file)
        keys = next(content)
        result = []
        for row in content:
            dict = {}
            for i in range(len(keys)):
                dict[keys[i]] = row[i]
            result.append(dict)
        return result


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_dict = read(path)
    jobs_dict_with_only_job_type = [
        {"job_type": d["job_type"]} for d in jobs_dict
    ]
    jobs_dict_with_only_unique_job_type = [
        dict(t)
        for t in set([tuple(d.items()) for d in jobs_dict_with_only_job_type])
    ]
    job_types_list = [
        d["job_type"] for d in jobs_dict_with_only_unique_job_type
    ]
    print(job_types_list)
    return job_types_list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    jobs_filtered_by_type = [d for d in jobs if d["job_type"] == job_type]
    print(jobs_filtered_by_type)
    return jobs_filtered_by_type
