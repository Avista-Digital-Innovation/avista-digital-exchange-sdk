
from ..exceptions import *
from .. import globals
import requests
import os


class IotQueryExport:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def __str__(self):
        return f"""Query Export File Info:
    fileFormat: {self.fileFormat}
    fileSizeBytes: {self.fileSizeBytes}
    url: {self.url}
"""

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.queryId = dict['queryId']
        self.fileFormat = dict['fileFormat']
        self.fileSizeBytes = dict['fileSizeBytes']
        self.url = dict['url']

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}queryId
{tabStr}fileFormat
{tabStr}fileSizeBytes
{tabStr}url
{tabStr[0:-4]}}} """

    def getFilename(self):
        if self.fileFormat == "CSV":
            return "result.csv"
        elif self.fileFormat == "JSON":
            return "result.json"
        else:
            return f"result.{self.fileFormat}"

    def downloadAndWriteFile(self, url, writeLocation=None):
        if writeLocation is None:
            writeLocation = f'./'
        response = requests.get(url)
        fullWritePath = self.createWritePath(writeLocation, self.getFilename())
        open(fullWritePath, "wb").write(response.content)
        print('Wrote query export file to ' + fullWritePath)

    @staticmethod
    def createWritePath(writeLocation, cloudFilename):
        # if location is a directory, append the cloudFilename
        if os.path.isdir(writeLocation):
            return os.path.join(writeLocation, cloudFilename)
        # if not, use the writeLocation
        elif os.path.isfile(writeLocation):
            return writeLocation
        else:
            return writeLocation
