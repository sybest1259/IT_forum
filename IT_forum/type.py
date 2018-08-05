import pymysql

con = pymysql.connect('127.0.0.1','root','s89681114','test')
con.set_charset('utf8')
cursor = con.cursor()

# 添加顶级分类
def addTopType():
    typename = input('输入类别名称')
    sql = 'insert into type values(null,"{}",0,"0,")'.format(typename)
    cursor.execute(sql)
    con.commit()
    if cursor.rowcount:
        print('顶级分类添加成功')
# def add():
#     sql = 'create table type(id int primary key auto_increment,typename varchar(10),pid int,path varchar(100))'
#     cursor.execute(sql)
#     con.commit()
# 添加子分类
def addSonType():
    id = input('输入类别id：')
    sql = 'select * from type where id={}'.format(id)
    cursor.execute(sql)
    result = cursor.fetchone()#(1, '服装', 0, '0,')
    print(result)
    typename = input('输入类别名称：')
    sql = 'insert into type values(null,"{}",{},"{}")'.format(typename,result[0],result[-1]+str(result[0])+',')
    cursor.execute(sql)
    con.commit()
    if cursor.rowcount:
        print('子分类添加成功')
#展示分类
def showType():
    sql = 'select * from type order by concat(path,id)'
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        repeat = row[-1].count(',')*'|-'
        print(repeat,row[0],row[1],row[-1])



while True:
    print('1：添加顶级分类')
    print('2：添加子分类')
    print('3：显示分类')

    choose = input('输入选择的分类：')
    if choose == '1':
        addTopType()
    elif choose == '2':
        addSonType()
    else:
        showType()

# add()