# coding=utf-8
import pyrestful.rest
from pyrestful.rest import get, post
from pyrestful import mediatypes
import pandas as pd

from app.utils.DBconnection import excute_query, excute_update, excute_delete
from app.utils.tools import JsonUtils

class NetaList(pyrestful.rest.RestHandler):
    @get('/neta/list')
    def getNetaList(self):
        """
        获取捏他列表
        不加入搜索条件时默认展示最新更新的15条
        :return:
        """
        sql = """select neta_name,
                        neta_content,
                        editor,
                        update_time 
                        from t_neta
                        order by update_time desc 
                        limit 0,15"""
        result = excute_query(sql)

        columns = ["neta_name", "neta_content", "editor", "update_time"]
        df = pd.DataFrame(data=result, columns=columns)
        data = df[columns[:]].to_dict(orient='recodes')

        return JsonUtils.returm_json_response(code=200, msg="success", data=data)

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
    @get('/neta/content/{id}', _produces=mediatypes.APPLICATION_JSON)
    def getNetaContent(self, id):
        sql = """select neta_name,
                        neta_content,
                        author,
                        create_time,
                        editor,
                        update_time
                        from t_neta
                        where id = :id"""
        result = excute_query(sql, {"id": id})

        columns = ["neta_name", "neta_content", "author", "create_time", "editor", "update_time"]
        df = pd.DataFrame(data=result, columns=columns)
        data = df[columns[:]].to_dict(orient='recodes')

        return JsonUtils.returm_json_response(code=200, msg="success", data=data)

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
