import getData.getUrl
import getData.getData
import getData.SQLdb


def main(name):
    # 输入电影名
    movieName = name

    # 初始化对象
    geturl = getData.getUrl.Html_GetUrl()
    getdata = getData.getData.Html_Data()
    sqldb = getData.SQLdb.MySql_Connect()

    # 获取要查取的电影的url
    url = geturl.getUrl(movieName)

    #获取包含电影信息的字典和电影的url
    list, url, movieName = getdata.get_html(url)
    sqldb.insert(list, 'movie_info')

    #获取评论

    comment_lists = getdata.get_comment(url)
    for i in range(len(comment_lists)):
        comment_lists[i].insert(0, movieName)
        sqldb.insert(comment_lists[i], 'comment_info')

    #获取评分级别
    score_list = getdata.get_movie_score(url)
    sqldb.insert(score_list, 'movie_score')

    #获取播放地址
    play_list = getdata.get_movie_play(url)
    for lis in play_list:
        sqldb.insert(lis, 'movie_play')

    #获取奖项
    awardDic = getdata.get_movie_awards(url)
    for dic in awardDic:
        sqldb.insert([movieName, dic, awardDic[dic]], 'movie_awards')
    return movieName
    
if __name__ == '__main__':
    main("星际穿越")