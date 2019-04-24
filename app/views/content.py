# coding=utf-8
import pyrestful.rest

from pyrestful.rest import get,post

class NetaList(pyrestful.rest.RestHandler):
    @get('/neta/list')
    def getNetaList(self):
        """
        获取捏他列表
        不加入搜索条件时默认展示最新更新的15条
        :return:
        """
        pass

    @get('/neta/top5')
    def getTop(self):
        """
        展示浏览次数最多的5条
        :return:
        """
        pass


class NetaContent(pyrestful.rest.RestHandler):
    """
    捏他详情页内容
    """
    @get('/neta/content/{id}')
    def getNetaContent(self, name):
        pass

    @post('/neta/content/edit')
    def editNetaContent(self):
        """
        修改neta内容
        :return:
        """
        pass

    @post('/neta/content/add')
    def addNeta(self):
        """
        新增neta
        :return:
        """
        pass

    @post('/neta/content/delete')
    def deleteNeta(self):
        pass

class NetaComment(pyrestful.rest.RestHandler):
    """
    捏他评论
    """
    @get('/neta/comment')
    def getCommentList(self):
        pass

    @post('/neta/comment/add')
    def addComment(self):
        pass

    @post('/neta/comment/delete')
    def deleteComment(self):
        pass
