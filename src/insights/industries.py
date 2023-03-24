from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    with open(path, encoding="utf-8") as file:
        content = csv.reader(file)
        keys = next(content)
        result = []
        for row in content:
            empty_dict = {}
            for i in range(len(keys)):
                empty_dict[keys[i]] = row[i]
            result.append(empty_dict)

    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_dict = result
    jobs_dict_with_only_industry = [
        {"industry": d["industry"]} for d in jobs_dict if d["industry"]
    ]
    jobs_dict_with_only_unique_industry = [
        dict(t)
        for t in set([tuple(d.items()) for d in jobs_dict_with_only_industry])
    ]
    jobs_industry_list = [
        d["industry"] for d in jobs_dict_with_only_unique_industry
    ]
    print(jobs_industry_list)
    return jobs_industry_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
