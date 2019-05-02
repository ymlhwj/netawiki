# coding=utf-8
import pyrestful.rest
from pyrestful.rest import get, post
from pyrestful import mediatypes
import pandas as pd
import json
from datetime import datetime

from app.utils.DBconnection import excute_query, excute_update, excute_delete
from app.utils.tools import Response, format_data, ComplexEncoder

class NetaList(pyrestful.rest.RestHandler):
    @get('/neta/list', _produces=mediatypes.APPLICATION_JSON)
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
        data = format_data(columns, result)
        response = Response.return_response(code=200, msg="success", data=data)
        return json.dumps(response, cls=ComplexEncoder)

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
                        where neta_id = :id"""
        result = excute_query(sql, {"id": id})
        columns = ["neta_name", "neta_content", "author", "create_time", "editor", "update_time"]
        data = format_data(columns, result)
        response = Response.return_response(code=200, msg="success", data=data)
        return json.dumps(response, cls=ComplexEncoder)

    @post('/neta/content/add', _produces=mediatypes.APPLICATION_JSON)
    def addNeta(self, request):
        """
        新增neta
        :return:
        """
        print(request)
        params = {}
        params["neta_name"] = request["neta_name"]
        params["neta_content"] = request["neta_content"]
        params["author"] = request["author"]
        params["create_time"] = str(datetime.now())
        query_sql = """select neta_name from netawiki.t_neta where neta_name=:neta_name;"""
        result = excute_query(query_sql, params={"neta_name": params["neta_name"]})
        if len(result):
            return Response.return_response(code=200, msg="neta has already existed")

        update_sql = """insert into netawiki.t_neta (neta_name, neta_content, author, create_time, editor, update_time, version)
                  values (:neta_name, :neta_content, :author, :create_time, :author, :create_time, 0); """
        excute_update(update_sql, params=params)

        return Response.return_response(code=200, msg="success")

    @post('/neta/content/edit')
    def editNetaContent(self):
        """
        修改neta内容
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


class Test(pyrestful.rest.RestHandler):
    @post('/neta/test',  _produces=mediatypes.APPLICATION_JSON)
    def test(self, test_info):
        print(test_info)
        print(type(test_info))
        neta_name = test_info.get("neta_name", "")
        print(neta_name)
        sql = """select * from netawiki.t_neta where neta_name= :neta_name ;"""
        result = excute_query(sql, {"neta_name": neta_name})
        print(result)
        return Response.return_response(code="200", msg="succeed", data=[{"info": "hello!"}])
