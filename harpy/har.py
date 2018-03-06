"""
Created on Mar 02 11:11:36 2018

.. sectionauthor:: Lyle Collins <Lyle.Collins@csiro.au>
.. codeauthor:: Lyle Collins <Lyle.Collins@csiro.au>
"""
from collections import OrderedDict

from .har_file_io import HarFileIO

class HarFileMemObj(dict):
    """
    HAR file memory object - the equivalent of a HAR file stored in memory.
    """

    def __init__(self, *args, filename: str=None, **kwargs):
        super().__init__(*args, **kwargs)

        if isinstance(filename, str):
            self.update(HarFileIO.readHarFileInfo(filename))

    def getHeaderNames(self):
        return list(self["headers"].keys())

    def getHeader(self):
        """**Not implemented**.
        Retrieve a HeaderArrayMemObj. If the object has not been read into memory, this will initiate a read operation."""
        pass

    def writeToDisk(self, filename: str=None):
        """
        :param filename: If provided, writes to ``filename`` instead of overwriting the file read to.
        :return:
        """
        pass

    # def write_HAR_File(self):
    #     """
    #     Write the content of the HAR object to the file associated with it
    #
    #     :return:
    #     """
    #     for name in self._HeaderList:
    #         if not name in self._HeaderDict:
    #             self.getHeader(name)
    #     self.f.seek(0)
    #     self.f.truncate()
    #     for name in self._HeaderList:
    #         Header=self._HeaderDict[name]
    #         if Header.is_valid:
    #             Header.HeaderToFile(self.f)
    #     self.f.f.flush()

    @staticmethod
    def loadFromDisk(self):
        """NOT Implemented."""
        pass

class HeaderArrayMemObj(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# class HAR(object):
#     """
#     This class is for loading HAR files into memory, manipulating the loaded HAR file virtually, and then writing \
#     the manipulated version to disk.
#     """
#
#     def __init__(self, filename: str=None, headers: List[str]=None):
#         """
#         Connects the file fname to the HAR object and parsers the Headers on this file.
#         If mode w is chosen, file can be edited.
#         All headers on the file are registered with the HAR object. Upon write all Headers are rewritten.
#
#         :param fname: name of the HAR file
#         :param mode: "w" or "r" for write or read
#         """
#         self._HeaderDict = OrderedDict()
#         if filename:
#             # Load headers from a file
#             if isinstance(headers, list):
#                 # TODO: Load only requested headers
#                 pass
#             elif headers is not None:
#                 raise ValueError("'headers' must be provided as a list.")
#             else:
#                 # Load entire file
#                 HAR.loadHarFile(filename)
#
#     def loadHarFile(self, filename):
#         pass
#
#     def loadHarHeaders(self, filename: str, header_names: List[str]):
#         for header in header_names:
#             self.loadHarHeader(filename, header)
#
#     def loadHarHeader(self, filename: str, header_name: str):
#         if not isinstance(header_name, str):
#             raise ValueError("Invalid value provided for '%s'." % header_name)
#         self._HeaderDict[header_name] = HAR_IO.getHeader()
#
#
#     def getHeader(self, name, getDeepCopy=True):
#         # type: (str, bool) -> Header
#         """
#         Returns the Header with the name name from the file object associated with the HAR object.
#         The default behaviour returns a pointer to the HEader object on the HAR file, i.e. modifying this
#         object changes the associated object in the HAR object(not the file).
#         If an independent copy is required, set getDeepCopy=True
#         :param name: str
#         :param getDeepCopy: bool
#         :returns: Header: Header
#         :rtype: Header
#         """
#
#         name=name.strip()
#
#         if name in self.f.getHeaderNames():
#             self._HeaderDict[name] = Header.HeaderFromFile(name, self.f)
#             try:
#                 assert(isinstance(self._HeaderDict[name], Header))
#             except AssertionError:
#                 raise TypeError("Invalid return type - return type attempting to get " +
#                                 "header '%s' is of type %s (id:%d), not '%s' (id:%d)." % (name,
#                                                                                           self._HeaderDict[name].__class__,
#                                                                                           id(self._HeaderDict[name].__class__),
#                                                                                           Header,
#                                                                                           id(Header)))
#         # if name not in self._HeaderList:
#         else:
#             print("Header " + name + " was not found on file " + self.getFileName())
#             return None
#
#         if getDeepCopy:
#             return self._HeaderDict[name].copy_header()
#         else:
#             return self._HeaderDict[name]