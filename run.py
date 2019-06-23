"""
Created on Jun 22nd, 2019

@author: xiangrana2

HeyJobs Python test.
API endpoint used: https://www.heyjobs.de/en/jobs-in-berlin
"""
import json

import bs4
import psycopg2
import requests

# connect to the PostgreSQL server
conn = psycopg2.connect(host="db", dbname="heyjobs",
                        user="test", password="testpass",
                        port="5432")


def get_ads():
    """
    get ads with their uids and titles from heyjobs site

    :return: a list of dictionaries with the ad id and title information
    """
    response = requests.get('https://www.heyjobs.de/en/jobs-in-berlin')
    soup_obj = bs4.BeautifulSoup(response.text, 'html.parser')
    links = soup_obj.find(
        attrs={'id': 'job-search-container'}).find_all('a', recursive=True)
    ads = list()
    for link in links:
        if '/en-de/jobs/' in link.get('href'):
            uid = link.get('href').split('/', 3)[3]
            title = link.find("h2", {"class": "job-card-title"}).string
            ads.append({'uid': uid, 'title': title})
    return ads


def create_ads_table():
    """
    create the ads table with the fields id, uid and title

    """
    table_cmd = """CREATE TABLE ads (id SERIAL PRIMARY KEY, uid VARCHAR(255) NOT NULL, title VARCHAR(255) NOT NULL)"""

    with conn.cursor() as cur:
        # create table
        cur.execute(table_cmd)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()


def insert_ads(data):
    """
    load ads with their uids and titles to the ads table

    :param data: list of dicts that holds ads information
    """
    query = """INSERT INTO ads (uid, title) SELECT uid, title FROM json_populate_recordset(null::ads, %s)"""
    with conn.cursor() as cur:
        # create table
        cur.execute(query, (json.dumps(data),))
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()


if __name__ == '__main__':
    ads_info = get_ads()
    create_ads_table()
    insert_ads(ads_info)
