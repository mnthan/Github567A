#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:23:11 2021

@author: drasty
"""

import json,requests

def RepoLister(name):
    #name = input("Enter the username: ")
    url = "https://api.github.com/users/{}/repos".format(name)

    res = requests.get(url)
    res_json = res.json()
    repository_list = []

    for repo in res_json:
        repository_list.append(repo["name"])

    for repo in repository_list:
        
        url2="https://api.github.com/repos/{}/{}/commits".format(name, repo)
        res2 = requests.get(url2)
        res2_json = res2.json()
        print("Repo: "+repo+" Number of commits: "+str(len(res2_json)))

    return("200")

print(RepoLister("mnthan"))
