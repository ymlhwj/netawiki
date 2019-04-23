import pyrestful.rest

from pyrestful.rest import get,post

class NetaContent(pyrestful.rest.RestHandler):
    @get('/neta/content/{id}')
    def getNetaContent(self, name):
        pass

    @post('/neta/content/edit')
    def editNetaContent(self):
        pass

    @post('/neta/content/add')
    def addNeta(self):
        pass

    @post('/neta/content/delete')
    def deleteNeta(self):
        pass

class NetaComment(pyrestful.rest.RestHandler):
    @get('/neta/comment')
    def getCommentList(self):
        pass

    @post('/neta/comment/add')
    def addComment(self):
        pass

    @post('/neta/comment/delete')
    def deleteComment(self):
        pass
