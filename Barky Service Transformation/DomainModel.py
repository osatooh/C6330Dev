"""
seperating(decoupling) the business logic layer from the persistent layer and presentation layerby introducing abstraction and encapsulation 
#will remove the response back to the presentation layer. 
#The service layer becomes dependent on the abstract repository
"""

from datetime import datetime
import sys

import requests

import Repository
from abc import ABC, abstractmethod
from Barkyapp import db
'''
below are the child class responsible for providing the service layer implementation to parent abstract class. 
 Enforcing the childclasses to compulsorily implement the abstract methods
'''

class Command(ABC):   
    @abc.abstractmethod
    def execute(self, data):
        raise NotImplementedError
    
class AddBookmarkCommand(Command):
    def execute(self, data, timestamp=None):
        data["date_added"] = datetime.utcnow().isoformat()
        AbstractRepository.add( data)
        return True, None


class ListBookmarksCommand(Command):
    def __init__(self, order_by="date_added"):
        self.order_by = order_by

    def execute(self):
        return True, AbstractRepository.list(order_by=self.order_by)


class DeleteBookmarkCommand(Command):
    def execute(self, data):
        SqlAlchemyRepository.delete(data)
        return True, None


class ImportGitHubStarsCommand(Command):
    """
    Import starred repos in Github - credit Dane Hillard
    """

    def _extract_bookmark_info(self, repo):
        return {
            "title": repo["name"],
            "url": repo["html_url"],
            "notes": repo["description"],
        }

    def execute(self, data):
        bookmarks_imported = 0

        github_username = data["github_username"]
        next_page_of_results = f"https://api.github.com/users/{github_username}/starred"
        while next_page_of_results:
            stars_response = requests.get(
                next_page_of_results,
                headers={"Accept": "application/vnd.github.v3.star+json"},
            )
            next_page_of_results = stars_response.links.get("next", {}).get("url")

            for repo_info in stars_response.json():
                repo = repo_info["repo"]

                if data["preserve_timestamps"]:
                    timestamp = datetime.strptime(
                        repo_info["starred_at"], "%Y-%m-%dT%H:%M:%SZ"
                    )
                else:
                    timestamp = None

                bookmarks_imported += 1
                AddBookmarkCommand().execute(
                    self._extract_bookmark_info(repo),
                    timestamp=timestamp,
                )

        return f"Imported {bookmarks_imported} bookmarks from starred repos!"


class EditBookmarkCommand(Command):
    def execute(self, data):
        AbstractRepository(data['id'],data['update'])
        return True,None


class QuitCommand(Command):
    def execute(self,data=None):
        sys.exit()
